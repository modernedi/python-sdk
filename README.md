# ModernEDI Python SDK

Server-side Python clients for the [ModernEDI Integration API](https://www.modernedi.com/integration-api/),
including mappings, mapped outputs, transactions, configuration-as-code, and optional scenarios.

**Preview 0.2.0:** the API may evolve before 1.0. Install the official package from PyPI:

```sh
python -m pip install modernedi-sdk==0.2.0
```

Requires Python 3.10 or newer. Both synchronous and native asynchronous clients are included.

## Get started

Create an Integration API key in your workspace with only the scopes your application needs.
Keep it in a server-side secret store; never embed it in browser, mobile, or desktop
distributions, or commit it to Git or logs.
See [Integration API authentication](https://www.modernedi.com/integration-api/).

```python
import os
from modernedi import ModernEdiClient

with ModernEdiClient(api_key=os.environ["MODERNEDI_API_KEY"]) as client:
    response = client.partners.list_integration_partners()
    print(response.data)
    print("Support request ID:", response.request_id)
```

An incoming or outgoing mapping is enough to process a partner document. You do not need a
scenario, Git repository, or configuration runner to use this client. Scenarios add conversation
verification; configuration-as-code adds repeatable review and deployment of those same resources.

The client groups match the TypeScript SDK: `partners`, `mappings`, `mapped_outputs`,
`transactions`, `outbound_as2`, `as2_connections`, `configuration_as_code`, `scenario_runs`,
`mapping_runtime`, `integration_events`, `account`, and `x12`. Methods use snake_case and
keyword arguments. Their parameters and models come from the same OpenAPI contract.

```python
from modernedi import AsyncModernEdiClient

async def list_partners(key):
    async with AsyncModernEdiClient(api_key=key) as client:
        return (await client.partners.list_integration_partners()).data
```

Reuse one client for connection pooling. Context managers close owned clients. If you inject an
HTTPX client using `http_client=`, you remain responsible for closing it; do not put authentication
in its default headers. The SDK chooses exactly one `api_key` or `bearer_token`, does not follow
redirects, verifies TLS by default, and uses a 30-second per-attempt timeout. Production requests
use `https://api.modernedi.com`. A custom `base_url` must use HTTPS except for loopback tests.
`bearer_token` sends the same Integration API key as `Authorization: Bearer`; it is not a
browser sign-in session token.

## Models, configuration, and exact wire data

```python
from modernedi import models

with ModernEdiClient(api_key=os.environ["MODERNEDI_API_KEY"]) as client:
    exported = client.configuration_as_code.export_integration_configuration()
    request = models.ConfigurationPlanRequest.from_dict({"files": exported.data.to_dict()["files"]})
    planned = client.configuration_as_code.plan_integration_configuration(body=request)
    print(planned.request_id)  # A plan changes no configuration and sends no EDI.
```

`models` contains generated Pydantic models. Use `from_dict()`/`from_json()` for wire input and
`to_dict()`/`to_json()` for wire output, including nested union types; do not substitute Pydantic's
internal `model_dump()` for the wire serializer. Omitted optional fields stay omitted, and explicit
null/false values remain distinct. Configuration file contents and hashes are retained. Date-time
fields stay strings so nine-digit timestamp precision is not lost. Scenario parameter sets, Test
and Production bindings, and bindings with omitted syntax-tree pins are supported.

Configuration `apply` remains an explicit operation requiring the reviewed plan, current snapshot
precondition, and an idempotency key. This SDK does not apply automatically or bypass verification.
See [configuration-as-code](https://www.modernedi.com/integration-api/#tag/Configuration-as-Code) and the
[read-only example](examples/configuration_plan.py).

## Send source documents without changing their media type

For endpoints that accept XML, JSON, text, or X12, use an explicit `RequestBody`:

```python
from modernedi import RequestBody

source = RequestBody.text("<invoice><number>INV-1</number></invoice>", "application/xml")
envelope = RequestBody.json(
    {"input": "<invoice/>", "contentType": "application/xml", "params": {"invoiceNumber": "INV-1"}},
    "application/vnd.modernedi.outbound+json",
)
# Pass one as body= to outbound_as2.send_as2_message(...) or reply_to_inbound_as2_message(...).
# test=True uses the partner's Test AS2 configuration; it still sends a real test message.
```

Use the generated-X12 methods only when you already have X12. Ordinary send/reply methods apply
the selected outgoing map. Mapper-editor params are fixtures; supply required live params in the
envelope. Polling mapped outputs does not acknowledge them: acknowledge only after durable custody.

## Responses, errors, and retries

Every call returns `ApiResponse`: `data`, `status_code`, `headers`, and exact `raw_body` bytes,
plus `request_id`, `etag`, `location`, `retry_after`, `idempotency_replayed`, and `content_sha256`.
Use `raw_body` when checking a scenario evidence report's digest, not re-serialized JSON.
Conditional `304` responses have `data=None`.

`ModernEdiApiError` exposes `status_code`, `code`, `request_id`, `retryable`, `details`,
`retry_after`, and `raw_body`. Do not log raw partner documents or credentials indiscriminately.
Non-JSON errors still produce a structured exception with the status and available request ID.

Retries are **off by default**. Opt in with `retry=RetryOptions(max_attempts=3)`. Retries cover
transport failures and HTTP 429/502/503/504 only. Safe reads, configuration plans, and transaction
watch/unwatch operations can retry; other mutations must support and supply an `Idempotency-Key`
in the API contract. Adding that header to an unsupported operation does not enable retries. The SDK never
retries before `Retry-After`; a delay above its configured cap returns the error to your application.
Pass request-specific headers/timeouts through `RequestOptions`. Cancellation of an async task
also cancels retry waits.

`paginate_cursor` and `paginate_cursor_async` accept page-loading, item, and next-cursor functions.
They preserve opaque cursors, detect cycles, and default to a 1,000-page limit. Repeat the same
filters on every page. Lower `max_pages` to bound work for your use case.

For the lease-acquiring mapped-output queue, use `iterate_mapped_outputs` (or
`iterate_mapped_outputs_async`), not ordinary list pagination:

```python
from modernedi import iterate_mapped_outputs

for output in iterate_mapped_outputs(
    lambda cursor: client.mapped_outputs.poll_mapped_outputs(cursor=cursor, environment="test"),
    max_polls=20,
):
    # Durably save/deduplicate output.id, then acknowledge its latest receipt_handle.
    print(output.id)
```

The helper accepts repeated cursors, continues past empty pages with a cursor, and stops
at the end of the scan or `max_polls` (default 1,000). It does not acknowledge, deduplicate,
or continuously watch. Queue polls are never automatically retried: a lost response can
already have acquired leases, which expire at the visibility timeout. Single-output
acknowledgment details are under `response.data.acknowledgment`, not duplicated at the top level.
Conditional configuration export returns status `304` with `data is None` and the ETag
when unchanged; this is a normal result, not an exception.

## Verify mapped-output webhooks

```python
from modernedi import verify_mapped_output_webhook

event = verify_mapped_output_webhook(raw_body, request_headers, signing_secret)
```

Pass the original bytes before JSON parsing. Verification checks the timestamp (five-minute
default tolerance), HMAC-SHA-256 with constant-time comparison, duplicate headers, event shape,
and header/body identity. `WebhookVerificationError.code` explains rejection. Your application
must durably deduplicate `deliveryId`; for business processing, also deduplicate `message.id`
because legitimate redelivery has a new delivery ID. A successful verification is not proof that
your ERP accepted the document.

No hosted workflow, provider login, or generator is needed by SDK consumers.

## Build and test this repository

This is complete, standalone package source with offline tests and synthetic fixtures.
No ModernEDI account, private repository, API key, or generator is needed.

```sh
python -m pip install . build
python -m unittest discover -s tests
python -m build
```

Generated API files come from ModernEDI's canonical contract. Please report issues here;
changes are made upstream and exported as reviewed snapshots. PUBLIC_SOURCE.json records
the exact source revision and hashes. Normal CI never publishes or calls your workspace.
