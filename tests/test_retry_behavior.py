"""Run the language-neutral HTTP behavior corpus through both public Python clients."""
import asyncio
import json
from pathlib import Path
import re
import unittest

import httpx
from modernedi import ModernEdiClient, AsyncModernEdiClient, ModernEdiApiError, RequestBody, RequestOptions, RetryOptions

CORPUS = json.loads((Path(__file__).parent / "fixtures/retry-behavior.json").read_text(encoding="utf-8"))
GROUPS = {"getIntegrationUsage": "account", "planIntegrationConfiguration": "configuration_as_code",
          "testMappedOutputWebhook": "mapped_outputs", "sendGeneratedX12Message": "outbound_as2",
          "watchIntegrationTransaction": "transactions", "unwatchIntegrationTransaction": "transactions"}


def snake(value):
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value).lower()


def call(client, row, request):
    arguments = {snake(key): value for key, value in request["parameters"].items()}
    if "body" in request:
        arguments["body"] = (RequestBody.text(request["body"], request["contentType"])
                             if "contentType" in request else request["body"])
    if "idempotencyKey" in row:
        arguments["idempotency_key"] = row["idempotencyKey"]
    arguments["options"] = RequestOptions(headers=row.get("headers", {}))
    return getattr(getattr(client, GROUPS[row["operationId"]]), snake(row["operationId"]))(**arguments)


class RetryBehaviorTests(unittest.TestCase):
    def test_shared_behavior_for_sync_and_async_clients(self):
        for row in CORPUS["cases"]:
            for asynchronous in (False, True):
                with self.subTest(case=row["id"], asynchronous=asynchronous):
                    request = CORPUS["requests"][row["operationId"]]
                    calls = []

                    def respond(sent):
                        calls.append(sent)
                        response = row["responses"][min(len(calls) - 1, len(row["responses"]) - 1)]
                        if response.get("networkError"):
                            raise httpx.ConnectError("Synthetic network failure", request=sent)
                        return httpx.Response(response["status"], headers=response.get("headers"))

                    options = dict(api_key=CORPUS["apiKey"], base_url=CORPUS["baseUrl"],
                                   retry=None if row.get("retry") is False else RetryOptions(base_delay=0))
                    result = failure = None
                    try:
                        if asynchronous:
                            async def run():
                                async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http:
                                    async with AsyncModernEdiClient(**options, http_client=http) as client:
                                        return await call(client, row, request)
                            result = asyncio.run(run())
                        else:
                            with httpx.Client(transport=httpx.MockTransport(respond)) as http:
                                with ModernEdiClient(**options, http_client=http) as client:
                                    result = call(client, row, request)
                    except (ModernEdiApiError, httpx.TransportError) as error:
                        failure = error
                    self.assertEqual(len(calls), row["attempts"])
                    for sent in calls:
                        self.assertEqual(sent.method, request["method"])
                        self.assertEqual(sent.url.raw_path.split(b"?")[0].decode(), "/edi" + request["path"])
                        self.assertEqual(sent.headers["X-API-Key"], CORPUS["apiKey"])
                        self.assertNotIn("Authorization", sent.headers)
                        expected_key = row.get("idempotencyKey", next(iter(row.get("headers", {}).values()), None))
                        self.assertEqual(sent.headers.get("Idempotency-Key", "").strip(), (expected_key or "").strip())
                        self.assertEqual(sent.url, calls[0].url)
                        self.assertEqual(sent.content, calls[0].content)
                        if "contentType" in request:
                            self.assertEqual(sent.content.decode(), request["body"])
                        elif "body" in request:
                            self.assertEqual(json.loads(sent.content), request["body"])
                    if row.get("networkError"):
                        self.assertIsInstance(failure, httpx.TransportError)
                    elif row["status"] >= 400:
                        self.assertIsInstance(failure, ModernEdiApiError)
                        self.assertEqual(failure.status_code, row["status"])
                        self.assertEqual(failure.retry_after, row.get("retryAfter"))
                    else:
                        self.assertIsNone(failure)
                        self.assertEqual(result.status_code, row["status"])
