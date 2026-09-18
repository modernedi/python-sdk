import asyncio
import hashlib
import inspect
from importlib.resources import files
import json
from pathlib import Path
import unittest

import httpx
from modernedi import ModernEdiClient, AsyncModernEdiClient, ModernEdiApiError, RequestBody, RequestOptions, RetryOptions, models

CORPUS = json.loads((Path(__file__).resolve().parent / "fixtures/cases.json").read_text(encoding="utf-8"))
CONTRACT = json.loads(files("modernedi.generated").joinpath("contract.json").read_text(encoding="utf-8"))


class ContractTests(unittest.TestCase):
    def test_same_contract(self):
        self.assertEqual(CORPUS["bundledSpecificationSha256"], CONTRACT["bundledSpecificationSha256"])
        self.assertIn("OpenAPI Generator " + CONTRACT["generatorVersion"], inspect.getmodule(models.ScenarioEvidenceReport).__doc__)

    def test_all_operations_route_and_authenticate_once(self):
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(204))) as http:
            with ModernEdiClient(api_key="synthetic-test-key", http_client=http) as client:
                methods = {}
                for name, member in inspect.getmembers(type(client)):
                    if isinstance(member, property):
                        api = getattr(client, name)
                        for method_name, method in inspect.getmembers(api, inspect.ismethod):
                            if not method_name.startswith("_"):
                                methods[method_name] = method
                for operation in CONTRACT["operations"]:
                    import re
                    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", operation["operationId"]).lower()
                    method = methods[name]
                    kwargs = {}
                    for parameter in inspect.signature(method).parameters.values():
                        if parameter.default is inspect.Parameter.empty:
                            kwargs[parameter.name] = (RequestBody.text("ST*850~", "application/edi-x12") if parameter.annotation == "RequestBody"
                                else {} if parameter.name == "body" else 7 if parameter.annotation == "int" else "fixture")
                    response = method(**kwargs)
                    self.assertEqual(response.status_code, 204)
                    request = requests[-1]
                    self.assertEqual(request.method, operation["method"])
                    expected_path = re.sub(r"\{([^}]+)\}", lambda match: str(kwargs[
                        re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", match[1]).lower()]), operation["path"])
                    self.assertEqual(request.url.path, expected_path)
                    self.assertEqual(request.headers.get("X-API-Key"), "synthetic-test-key")
                    self.assertNotIn("Authorization", request.headers)
                self.assertEqual(len(requests), len(CONTRACT["operations"]))
            self.assertFalse(http.is_closed, "caller-owned HTTP client must stay open")

    def test_full_export_through_typed_plan_preserves_hashes(self):
        exported = next(case["value"] for case in CORPUS["cases"] if case["id"] == "configuration-export-response")
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(200, json=exported))) as http:
            client = ModernEdiClient(api_key="synthetic", http_client=http)
            response = client.configuration_as_code.export_integration_configuration()
            plan = models.ConfigurationPlanRequest.from_dict({"files": json.loads(response.data.to_json())["files"]})
            with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(204))) as plan_http:
                ModernEdiClient(api_key="synthetic", http_client=plan_http).configuration_as_code.plan_integration_configuration(body=plan)
            actual = json.loads(requests[-1].content)
            self.assertEqual(actual["files"], exported["files"])
            for file in actual["files"]:
                content = file["content"] if file["format"] == "TEXT" else json.dumps(file["content"], sort_keys=True, separators=(",", ":"), ensure_ascii=False)
                self.assertEqual(hashlib.sha256(content.encode()).hexdigest(), file["contentSha256"])

    def test_raw_body_and_metadata(self):
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(204,
            headers={"X-Request-Id": "req-1", "Idempotency-Replayed": "true", "ETag": '"tag"', "X-Content-Sha256": "abc"}))) as http:
            response = ModernEdiClient(api_key="synthetic", http_client=http).outbound_as2.send_as2_message(
                body=RequestBody.text("<invoice>é</invoice>\r\n", "application/xml"), partner_id=1, x12_version="4010",
                functional_group_type="IN", transaction_group_type=810, test=True)
            self.assertEqual(requests[0].content, "<invoice>é</invoice>\r\n".encode())
            self.assertEqual(requests[0].headers["Content-Type"], "application/xml")
            self.assertEqual(requests[0].url.params["test"], "true")
            self.assertEqual(response.request_id, "req-1")
            self.assertTrue(response.idempotency_replayed)
            self.assertEqual(response.etag, '"tag"')
            self.assertEqual(response.content_sha256, "abc")

    def test_encoded_path_and_bearer(self):
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(204))) as http:
            ModernEdiClient(bearer_token="synthetic", http_client=http).scenario_runs.get_scenario_run(run_id="run/a?#b")
            self.assertIn(b"run%2Fa%3F%23b", requests[0].url.raw_path)
            self.assertEqual(requests[0].headers["Authorization"], "Bearer synthetic")
            self.assertNotIn("X-API-Key", requests[0].headers)

    def test_repeated_typed_filters_use_wire_values(self):
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(204))) as http:
            ModernEdiClient(api_key="synthetic", http_client=http).transactions.list_integration_transactions(
                mapping_status=[models.FilterableTransactionMappingStatus.FAILED, models.FilterableTransactionMappingStatus.RECOVERED])
            self.assertEqual(requests[0].url.params.get_list("mappingStatus"), ["FAILED", "RECOVERED"])

    def test_retries_are_opt_in_and_mutations_require_identity(self):
        for retry, idempotency, expected in [(None, None, 1), (RetryOptions(base_delay=0), None, 1), (RetryOptions(base_delay=0), "command-1", 3)]:
            requests = []
            with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(503, json={"error": {
                "code": "busy", "message": "Try later", "requestId": "req-error", "retryable": True, "details": {"lane": "test"}}}))) as http:
                with self.assertRaises(ModernEdiApiError) as raised:
                    ModernEdiClient(api_key="synthetic", http_client=http, retry=retry).scenario_runs.start_scenario_run(
                        body={}, idempotency_key=idempotency)
                self.assertEqual(len(requests), expected)
                self.assertEqual(raised.exception.code, "busy")
                self.assertEqual(raised.exception.request_id, "req-error")
                self.assertTrue(raised.exception.retryable)

    def test_retry_after_is_never_shortened(self):
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(429, headers={"Retry-After": "60"}))) as http:
            with self.assertRaises(ModernEdiApiError) as raised:
                ModernEdiClient(api_key="synthetic", http_client=http, retry=RetryOptions(base_delay=0)).account.get_integration_usage()
            self.assertEqual(len(requests), 1)
            self.assertEqual(raised.exception.retry_after, "60")

    def test_unsupported_idempotency_header_does_not_enable_mutation_retries(self):
        requests = []
        with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(503))) as http:
            with self.assertRaises(ModernEdiApiError):
                ModernEdiClient(api_key="synthetic", http_client=http, retry=RetryOptions(base_delay=0)).mapped_outputs.test_mapped_output_webhook(
                    partner_id=1, options=RequestOptions(headers={"Idempotency-Key": "not-supported-here"}))
            self.assertEqual(len(requests), 1)

    def test_plan_retries_but_conflicts_do_not(self):
        for status, expected in [(503, 3), (409, 1)]:
            requests = []
            with httpx.Client(transport=httpx.MockTransport(lambda request: requests.append(request) or httpx.Response(status))) as http:
                with self.assertRaises(ModernEdiApiError):
                    ModernEdiClient(api_key="synthetic", http_client=http, retry=RetryOptions(base_delay=0)).configuration_as_code.plan_integration_configuration(body={})
                self.assertEqual(len(requests), expected)

    def test_evidence_digest_uses_original_bytes(self):
        evidence = next(case["value"] for case in CORPUS["cases"] if case["schema"] == "ScenarioEvidenceReport")
        raw = json.dumps(evidence, indent=2, ensure_ascii=False).encode() + b"\n"
        digest = hashlib.sha256(raw).hexdigest()
        with httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, content=raw, headers={"X-Content-SHA256": digest}))) as http:
            response = ModernEdiClient(api_key="synthetic", http_client=http).scenario_runs.download_scenario_evidence_report(run_id="run-1")
            self.assertEqual(response.content_sha256, hashlib.sha256(response.raw_body).hexdigest())
            self.assertEqual(json.loads(response.data.to_json()), evidence)

    def test_unsafe_auth_and_redirect_overrides_rejected(self):
        for kwargs in ({}, {"api_key": "a", "bearer_token": "b"}, {"api_key": ""}, {"api_key": "a", "base_url": "http://example.com"}):
            with self.assertRaises(ValueError):
                ModernEdiClient(**kwargs)
        with httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(302, headers={"Location": "https://other.invalid"}))) as http:
            client = ModernEdiClient(api_key="a", http_client=http)
            with self.assertRaises(ModernEdiApiError):
                client.account.get_integration_usage()
            with self.assertRaises(ValueError):
                client.account.get_integration_usage(options=RequestOptions(headers={"X-API-Key": "b"}))


class AsyncTests(unittest.IsolatedAsyncioTestCase):
    async def test_async_native_transport(self):
        calls = []
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda request: calls.append(request) or httpx.Response(204))) as http:
            async with AsyncModernEdiClient(api_key="synthetic", http_client=http) as client:
                result = await client.scenario_runs.get_scenario_run(run_id="test-run")
                self.assertEqual(result.status_code, 204)
            self.assertFalse(http.is_closed)
        self.assertEqual(len(calls), 1)

    async def test_async_retries_and_cancellation(self):
        calls = []
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda request: calls.append(request) or httpx.Response(503))) as http:
            client = AsyncModernEdiClient(api_key="synthetic", http_client=http, retry=RetryOptions(base_delay=0))
            with self.assertRaises(ModernEdiApiError):
                await client.account.get_integration_usage()
            self.assertEqual(len(calls), 3)

            reached = asyncio.Event()
            def response(request):
                reached.set()
                return httpx.Response(503)
            async with httpx.AsyncClient(transport=httpx.MockTransport(response)) as delayed:
                client = AsyncModernEdiClient(api_key="synthetic", http_client=delayed, retry=RetryOptions(base_delay=5))
                task = asyncio.create_task(client.account.get_integration_usage())
                await asyncio.wait_for(reached.wait(), timeout=1)
                task.cancel()
                with self.assertRaises(asyncio.CancelledError):
                    await task


def _round_trip(case):
    def test(self):
        model = getattr(models, case["schema"])
        parsed = model.from_dict(case["value"])
        self.assertEqual(json.loads(parsed.to_json()), case["value"], case["id"])
    return test

for index, case in enumerate(CORPUS["cases"]):
    setattr(ContractTests, f"test_wire_case_{index:03d}", _round_trip(case))
