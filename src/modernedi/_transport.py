"""Shared HTTP behavior; operation paths and models are generated from OpenAPI."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from enum import Enum
import json
import math
import re
import time
from typing import Any, Generic, Mapping, TypeVar
from urllib.parse import quote, urlsplit

import httpx
from ._wire import to_wire_value

T = TypeVar("T")


@dataclass(frozen=True)
class RequestBody:
    """An explicit media type for source documents, envelopes, and generated X12."""
    content: bytes
    content_type: str

    @classmethod
    def json(cls, value: Any, content_type: str = "application/json") -> RequestBody:
        return cls(json.dumps(to_wire_value(value), ensure_ascii=False, allow_nan=False,
                              separators=(",", ":")).encode("utf-8"), content_type)

    @classmethod
    def text(cls, value: str, content_type: str = "text/plain") -> RequestBody:
        return cls(value.encode("utf-8"), content_type)


@dataclass(frozen=True)
class RequestOptions:
    headers: Mapping[str, str] = field(default_factory=dict)
    timeout: float | None = None


@dataclass(frozen=True)
class RetryOptions:
    """Opt-in retries. Mutations need Idempotency-Key unless documented as read-only/idempotent."""
    max_attempts: int = 3
    base_delay: float = 0.25
    max_delay: float = 10.0

    def __post_init__(self) -> None:
        if type(self.max_attempts) is not int or not 1 <= self.max_attempts <= 10:
            raise ValueError("max_attempts must be an integer between 1 and 10")
        for name in ("base_delay", "max_delay"):
            if not math.isfinite(getattr(self, name)) or getattr(self, name) < 0:
                raise ValueError(f"{name} must be finite and non-negative")


@dataclass(frozen=True)
class ApiResponse(Generic[T]):
    data: T | None
    status_code: int
    headers: httpx.Headers
    raw_body: bytes

    @property
    def request_id(self) -> str | None:
        return self.headers.get("X-Request-Id")

    @property
    def retry_after(self) -> str | None:
        return self.headers.get("Retry-After")

    @property
    def idempotency_replayed(self) -> bool | None:
        return {"true": True, "false": False}.get(self.headers.get("Idempotency-Replayed", "").strip().lower())

    @property
    def etag(self) -> str | None:
        return self.headers.get("ETag")

    @property
    def location(self) -> str | None:
        return self.headers.get("Location")

    @property
    def content_sha256(self) -> str | None:
        return self.headers.get("X-Content-SHA256")


class ModernEdiApiError(Exception):
    def __init__(self, response: httpx.Response):
        self.status_code = response.status_code
        self.headers = response.headers
        self.raw_body = response.content
        try:
            self.response_body = response.json()
        except ValueError:
            self.response_body = None
        error = self.response_body.get("error", {}) if isinstance(self.response_body, dict) else {}
        if not isinstance(error, dict):
            error = {}
        self.code = error.get("code", "http_error")
        self.request_id = error.get("requestId") or response.headers.get("X-Request-Id")
        self.retry_after = response.headers.get("Retry-After")
        self.retryable = error.get("retryable") is True
        self.details = error.get("details")
        super().__init__(error.get("message") or f"ModernEDI returned HTTP {self.status_code}")


def _header(headers: dict[str, str], name: str, value: str) -> None:
    if name.lower() in {"authorization", "x-api-key", "host", "content-length"}:
        raise ValueError(f"{name} cannot override client authentication or routing")
    if any(c in str(value) for c in "\r\n"):
        raise ValueError("Header values cannot contain newlines")
    headers[name.lower()] = str(value)


def _query_value(value: Any) -> str:
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


class _BaseTransport:
    def __init__(self, *, api_key: str | None = None, bearer_token: str | None = None,
                 base_url: str = "https://api.modernedi.com", timeout: float = 30,
                 retry: RetryOptions | None = None):
        if (api_key is None) == (bearer_token is None):
            raise ValueError("Provide exactly one of api_key or bearer_token")
        credential = api_key if api_key is not None else bearer_token
        if not isinstance(credential, str) or not credential.strip() or any(c in credential for c in "\r\n"):
            raise ValueError("Credential must be a non-empty single-line string")
        url = urlsplit(base_url)
        if (not url.hostname or url.username or url.password or url.query or url.fragment or
                (url.scheme != "https" and not (url.scheme == "http" and url.hostname in {"localhost", "127.0.0.1", "::1"}))):
            raise ValueError("base_url must use HTTPS (HTTP is allowed only for loopback testing), without credentials, query, or fragment")
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be finite and positive")
        self._base_url = base_url.rstrip("/")
        self._auth = {"X-API-Key": credential} if api_key is not None else {"Authorization": f"Bearer {credential}"}
        self._timeout = timeout
        self._retry = retry or RetryOptions(max_attempts=1)

    def _prepare(self, method, path, path_params, query, headers, body, options):
        options = options or RequestOptions()
        request_headers: dict[str, str] = {"accept": "application/json"}
        for name, value in options.headers.items():
            _header(request_headers, name, value)
        for name, value in headers.items():
            if value is not None:
                _header(request_headers, name, value)
        if body is not None and not isinstance(body, RequestBody):
            body = RequestBody.json(body)
        if body is not None:
            if "content-type" in request_headers and request_headers["content-type"] != body.content_type:
                raise ValueError("Content-Type must match RequestBody.content_type")
            _header(request_headers, "content-type", body.content_type)
        retry_safe = (method in {"GET", "HEAD", "OPTIONS"} and path != "/v1/mapped-outputs") or (
            method == "POST" and path == "/v1/configuration/plan") or (
            method in {"PUT", "DELETE"} and path == "/v1/integration/transactions/{messageId}/{transactionKey}/watch") or (
            any(name.lower() == "idempotency-key" for name in headers) and
            bool(request_headers.get("idempotency-key", "").strip()))
        for name, value in path_params.items():
            if value is None or str(value) in {"", ".", ".."}:
                raise ValueError(f"Invalid path parameter: {name}")
            path = path.replace("{" + name + "}", quote(str(value), safe=""))
        params = [(name, _query_value(item)) for name, value in query.items() if value is not None
                  for item in (value if isinstance(value, list) else [value])]
        timeout = options.timeout if options.timeout is not None else self._timeout
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("Request timeout must be finite and positive")
        return dict(method=method, url=self._base_url + path, params=params,
                    headers={**request_headers, **self._auth}, content=body.content if body else None,
                    timeout=timeout, follow_redirects=False, auth=None), retry_safe

    def _delay(self, attempt: int, response: httpx.Response | None = None) -> float | None:
        delay = min(self._retry.base_delay * 2 ** (attempt - 1), self._retry.max_delay)
        if response is not None:
            if response.status_code not in {429, 502, 503, 504}:
                return None
            retry_after = response.headers.get("Retry-After", "").strip()
            if retry_after:
                try:
                    if re.fullmatch(r"\d+(?:\.\d+)?", retry_after):
                        delay = float(retry_after)
                    else:
                        date = parsedate_to_datetime(retry_after)
                        delay = max(0.0, (date - datetime.now(timezone.utc)).total_seconds())
                except (ValueError, TypeError, OverflowError):
                    pass
        return delay if delay <= self._retry.max_delay else None

    @staticmethod
    def _decode(response, response_type, raw):
        if not 200 <= response.status_code < 300 and response.status_code != 304:
            raise ModernEdiApiError(response)
        data = None
        if response.content and response.status_code not in {204, 304}:
            if raw:
                data = response.content
            else:
                data = response.json()
                if response_type is not None:
                    data = response_type.from_dict(data)
        return ApiResponse(data, response.status_code, response.headers, response.content)


class Transport(_BaseTransport):
    def __init__(self, *, api_key: str | None = None, bearer_token: str | None = None,
                 base_url: str = "https://api.modernedi.com", timeout: float = 30,
                 retry: RetryOptions | None = None, http_client: httpx.Client | None = None):
        super().__init__(api_key=api_key, bearer_token=bearer_token, base_url=base_url, timeout=timeout, retry=retry)
        if http_client is not None and any(name.lower() in {"authorization", "x-api-key"} for name in http_client.headers):
            raise ValueError("Pass credentials to ModernEdiClient, not HTTP client default headers")
        self._owns_client = http_client is None
        self._http = http_client or httpx.Client()

    def request(self, operation, method, path, *, path_params, query, headers, body, response_type, raw, options):
        request, retry_safe = self._prepare(method, path, path_params, query, headers, body, options)
        for attempt in range(1, self._retry.max_attempts + 1):
            try:
                response = self._http.request(**request)
            except httpx.TransportError:
                if not retry_safe or attempt == self._retry.max_attempts:
                    raise
                time.sleep(self._delay(attempt))
                continue
            delay = self._delay(attempt, response) if retry_safe and attempt < self._retry.max_attempts else None
            if delay is None:
                return self._decode(response, response_type, raw)
            response.close()
            time.sleep(delay)
        raise RuntimeError("Retry loop exhausted")

    def close(self):
        if self._owns_client:
            self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncTransport(_BaseTransport):
    def __init__(self, *, api_key: str | None = None, bearer_token: str | None = None,
                 base_url: str = "https://api.modernedi.com", timeout: float = 30,
                 retry: RetryOptions | None = None, http_client: httpx.AsyncClient | None = None):
        super().__init__(api_key=api_key, bearer_token=bearer_token, base_url=base_url, timeout=timeout, retry=retry)
        if http_client is not None and any(name.lower() in {"authorization", "x-api-key"} for name in http_client.headers):
            raise ValueError("Pass credentials to ModernEdiClient, not HTTP client default headers")
        self._owns_client = http_client is None
        self._http = http_client or httpx.AsyncClient()

    async def request(self, operation, method, path, *, path_params, query, headers, body, response_type, raw, options):
        request, retry_safe = self._prepare(method, path, path_params, query, headers, body, options)
        for attempt in range(1, self._retry.max_attempts + 1):
            try:
                response = await self._http.request(**request)
            except httpx.TransportError:
                if not retry_safe or attempt == self._retry.max_attempts:
                    raise
                await asyncio.sleep(self._delay(attempt))
                continue
            delay = self._delay(attempt, response) if retry_safe and attempt < self._retry.max_attempts else None
            if delay is None:
                return self._decode(response, response_type, raw)
            await response.aclose()
            await asyncio.sleep(delay)
        raise RuntimeError("Retry loop exhausted")

    async def close(self):
        if self._owns_client:
            await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
