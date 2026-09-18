"""Verify mapped-output webhooks before parsing or processing their payloads."""
import hashlib
import hmac
import json
import math
import re
import time
from collections.abc import Mapping


class WebhookVerificationError(ValueError):
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(message)


def _header(headers, name):
    entries = headers.multi_items() if hasattr(headers, "multi_items") else headers.items() if isinstance(headers, Mapping) else headers
    values = [value for key, value in entries if key.lower() == name.lower()]
    if len(values) > 1:
        raise WebhookVerificationError("duplicate_header", f"{name} must occur exactly once")
    value = values[0] if values else None
    if isinstance(value, (list, tuple)):
        if len(value) != 1:
            raise WebhookVerificationError("duplicate_header", f"{name} must occur exactly once")
        value = value[0]
    if not isinstance(value, str) or not value:
        raise WebhookVerificationError("missing_header", f"Required header {name} is missing")
    if "," in value:
        raise WebhookVerificationError("duplicate_header", f"{name} must occur exactly once")
    return value


def verify_mapped_output_webhook(raw_body: bytes, headers, signing_secret: str, *,
                                 tolerance_seconds: int = 300, now: float | None = None) -> dict:
    """Verify HMAC over original bytes. Caller must durably deduplicate deliveryId and message.id."""
    if not isinstance(raw_body, bytes):
        raise TypeError("raw_body must be the original request bytes")
    if not signing_secret:
        raise ValueError("signing_secret must not be empty")
    if type(tolerance_seconds) is not int or tolerance_seconds < 0:
        raise ValueError("tolerance_seconds must be a non-negative integer")
    now = time.time() if now is None else now
    if not math.isfinite(now):
        raise ValueError("now must be finite Unix epoch seconds")
    timestamp = _header(headers, "X-ModernEDI-Timestamp")
    signature = _header(headers, "X-ModernEDI-Signature")
    event_type = _header(headers, "X-ModernEDI-Event")
    delivery_id = _header(headers, "X-ModernEDI-Delivery-Id")
    if not re.fullmatch(r"(?:0|[1-9][0-9]*)", timestamp) or len(timestamp) > 16 or int(timestamp) > 9007199254740991:
        raise WebhookVerificationError("invalid_timestamp", "Expected whole Unix epoch seconds")
    if abs(math.floor(now) - int(timestamp)) > tolerance_seconds:
        raise WebhookVerificationError("timestamp_outside_tolerance", "Webhook timestamp is outside the accepted window")
    if not re.fullmatch(r"sha256=[0-9a-f]{64}", signature):
        raise WebhookVerificationError("invalid_signature_format", "Expected sha256 and 64 lowercase hexadecimal characters")
    expected = hmac.new(signing_secret.encode("utf-8"), timestamp.encode("ascii") + b"." + raw_body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature[7:], expected):
        raise WebhookVerificationError("signature_mismatch", "Webhook signature does not match")
    def invalid_constant(value):
        raise ValueError(f"Non-JSON number: {value}")
    try:
        event = json.loads(raw_body, parse_constant=invalid_constant)
    except (ValueError, UnicodeError) as error:
        raise WebhookVerificationError("invalid_json", "Verified body is not JSON") from error
    def invalid():
        raise WebhookVerificationError("invalid_event", "Verified body does not match a mapped-output webhook event")
    def text(value, key):
        return isinstance(value.get(key), str) and bool(value[key])
    if not isinstance(event, dict) or any(not text(event, key) for key in ("deliveryId", "createdAt")):
        invalid()
    if any(type(event.get(key)) is not int or not 1 <= event[key] <= 9007199254740991 for key in ("tenantId", "partnerId")):
        invalid()
    if event.get("event") != event_type or event["deliveryId"] != delivery_id:
        invalid()
    if event_type == "mapped_output.test":
        if event.get("test") is not True or "message" in event or not text(event, "requestId") or not text(event, "description"):
            invalid()
    elif event_type == "mapped_output.available":
        message = event.get("message")
        if not isinstance(message, dict) or any(not text(message, key) for key in
            ("id", "receiptHandle", "messageId", "transactionKey", "environment", "mappedOutputKey", "purpose")):
            invalid()
        if any(type(message.get(key)) is not int or not 0 <= message[key] <= 9007199254740991 for key in ("deliveryCount", "sequenceNumber")):
            invalid()
    else:
        invalid()
    return event
