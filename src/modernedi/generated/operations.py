# Generated from the complete bundled Integration API. Do not edit.
from __future__ import annotations
from typing import Any
from . import models
from modernedi._transport import Transport, AsyncTransport, ApiResponse, RequestBody, RequestOptions

class MappedOutputQueueApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def acknowledge_mapped_output(self, *, body: models.MappedOutputAckRequest, x_request_id: str | None = None, id: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputAckResponse]:
        "Mark mapped output as received\n\n**Required key scope:** `messages:write`.\nRecords that your integration acknowledged custody of a previously returned mapped output message. Call this after the mapped output has been durably stored or enqueued for reliable processing in your system. This acknowledgment does not prove later ERP or business processing. The receipt handle must match the latest poll response for this mapped output id. A retry with the same id and receipt handle is idempotent: it returns the original acknowledgment and `ackedAt` value instead of failing. If a call ends without a definitive response, retry that same acknowledgment before polling. Poll for a new receipt only when the old lease is rejected or the message becomes available again; an acknowledged item is no longer returned by polling.\n"
        return self._transport.request(
            "acknowledgeMappedOutput", "POST", "/v1/mapped-outputs/{id}/ack",
            path_params={"id": id},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.MappedOutputAckResponse, raw=False, options=options)

    def acknowledge_mapped_outputs(self, *, body: models.MappedOutputBulkAckRequest, x_request_id: str | None = None, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputBulkAckResponse]:
        "Atomically acknowledge multiple mapped outputs\n\n**Required key scope:** `messages:write`.\nAcknowledges between 1 and 100 mapped-output receipts in one database transaction. If any id or receipt handle is invalid, none of the items are acknowledged. Repeating an already successful request with the same id and receipt handles is idempotent and returns the original acknowledgment timestamps. Retry the same batch first when a call ends without a definitive response; already acknowledged items are not returned by polling. All items must belong to the environment selected by the `environment` query parameter.\n"
        return self._transport.request(
            "acknowledgeMappedOutputs", "POST", "/v1/mapped-outputs/ack",
            path_params={},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.MappedOutputBulkAckResponse, raw=False, options=options)

    def get_mapped_output_webhook_status(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputWebhookStatusResponse]:
        "Get mapped-output webhook status\n\n**Required key scope:** `configuration:read`.\nReturns the current mapped-output webhook configuration and recent delivery health for a partner. This read-only endpoint never returns the signing secret; it reports whether a secret is configured and only its last four characters so operators can identify the active credential. Save the response `ETag` header or `webhook.etag` before updating.\n"
        return self._transport.request(
            "getMappedOutputWebhookStatus", "GET", "/v1/partners/{partnerId}/mapped-output-webhook",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappedOutputWebhookStatusResponse, raw=False, options=options)

    def poll_mapped_outputs(self, *, x_request_id: str | None = None, environment: str | None = None, start_date: str | None = None, end_date: str | None = None, cursor: str | None = None, limit: int | None = None, visibility_timeout_seconds: int | None = None, direction: str | None = None, partner_name: str | None = None, partner_id: int | None = None, transaction_set: str | None = None, business_key: str | None = None, message_id: str | None = None, reply_to_message_id: str | None = None, transaction_control_number: str | None = None, functional_group_control_number: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputQueueResponse]:
        "Poll mapped inbound output\n\n**Required key scope:** `transactions:read`.\nReturns server-managed mapped inbound documents for this tenant and temporarily marks them in progress. Transaction-record-only results and legacy direct-to-SQS or direct-to-DynamoDB outputs are not duplicated into this queue. If a returned message is not acknowledged before the visibility timeout expires, ModernEDI may return it again on a later poll. Push delivery uses the same queue state: a successful 2xx webhook response acknowledges the message, while a failed push leaves it available through this endpoint. Each request performs a bounded scan. When `hasMore` is true, send `nextCursor` as the next request's `cursor` so polling advances past unavailable or output-free transactions instead of rescanning them. A cursor may repeat while new leases advance through outputs in the same scan window; an empty page with `nextCursor` is not the end of the scan. Use the SDK's bounded mapped-output iterator, not ordinary list pagination. Despite using GET, a poll acquires leases and the SDKs do not automatically retry it. If a response is lost, its outputs become available again after the visibility timeout. This endpoint runs on the shared ModernEDI API host, not on the tenant AS2 hostname.\n"
        return self._transport.request(
            "pollMappedOutputs", "GET", "/v1/mapped-outputs",
            path_params={},
            query={"environment": environment, "startDate": start_date, "endDate": end_date, "cursor": cursor, "limit": limit, "visibilityTimeoutSeconds": visibility_timeout_seconds, "direction": direction, "partnerName": partner_name, "partnerId": partner_id, "transactionSet": transaction_set, "businessKey": business_key, "messageId": message_id, "replyToMessageId": reply_to_message_id, "transactionControlNumber": transaction_control_number, "functionalGroupControlNumber": functional_group_control_number},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappedOutputQueueResponse, raw=False, options=options)

    def test_mapped_output_webhook(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputWebhookTestResponse]:
        "Send a synthetic mapped-output webhook test\n\n**Required key scope:** `configuration:write`.\n\nSends one signed `mapped_output.test` event to the partner's saved HTTPS webhook endpoint using the same DNS validation, pinned public-address transport, timeout, and HMAC signing path as normal mapped-output delivery. The test event is explicitly marked `test: true`, contains no mapped-output `message`, queue id, receipt handle, or business document, and never creates, leases, acknowledges, retries, or changes a real mapped-output queue item. It also does not replace the webhook's recorded production delivery health.\n\nThe webhook may be disabled while this connectivity test runs, but an endpoint and signing secret must already be saved. The API returns `200` after every completed attempt; inspect `delivered`, `statusCode`, and `error` for the destination outcome. `requestId` matches the `X-Request-Id` response header and is also included in the signed synthetic event for correlation.\n"
        return self._transport.request(
            "testMappedOutputWebhook", "POST", "/v1/partners/{partnerId}/mapped-output-webhook/test",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappedOutputWebhookTestResponse, raw=False, options=options)

    def update_mapped_output_webhook(self, *, body: models.MappedOutputWebhookUpdateRequest, x_request_id: str | None = None, partner_id: int, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputWebhookUpdateResponse]:
        "Configure mapped-output webhook delivery\n\n**Required key scope:** `configuration:write`.\n\nEnables, disables, or rotates a partner's HTTPS mapped-output webhook. Send the current configuration ETag in `If-Match`. `endpointUrl` is required when enabling delivery and must be an absolute HTTPS URL without user information or a fragment and use a publicly routable host. Localhost, private, link-local, multicast, carrier-grade NAT, documentation, benchmark, and other reserved address targets are rejected. ModernEDI resolves the hostname again before every webhook delivery and sends only when all resolved addresses are publicly routable. Enabling a webhook without an existing signing secret creates one; `rotateSigningSecret: true` replaces it.\n\nThe request body is strict JSON: unknown fields are rejected; `enabled` and `rotateSigningSecret` must be booleans; and `endpointUrl` must be a string or `null`. Type mismatches return `400 invalid_request` with the offending JSON pointer.\n\nA newly created or rotated `plainTextSigningSecret` appears only in this successful response. Save it immediately. Later reads expose only `signingSecretConfigured` and `signingSecretLastFour`.\n"
        return self._transport.request(
            "updateMappedOutputWebhook", "PUT", "/v1/partners/{partnerId}/mapped-output-webhook",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id, "If-Match": if_match},
            body=body, response_type=models.MappedOutputWebhookUpdateResponse, raw=False, options=options)

class ScenarioRunsApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def advance_scenario_run(self, *, body: dict[str, Any], run_id: str, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Advance adapter work or reevaluate graph deadlines\n\nAdvances server-controlled adapter work or refreshes/re-evaluates the existing graph, using the same runtime as the browser. Every fresh external dispatch, including ModernEDI test-partner-originated traffic, additionally requires messages:write on the authenticated key. The same key is reused automatically; no second credential is accepted in the body. Reconciliation and observation-only evaluation need no send scope. retry.requiresApiKey describes the browser's supplemental credential, not API authorization: false never exempts a dispatch from messages:write. A lost-response retry must reuse the original Idempotency-Key and If-Match. An already-recorded failed operation is replayed without another dispatch; to attempt a retryable failed action again, fetch the current ETag and use a fresh key. Follow structured guidance rather than hard-coding bundled step names."
        return self._transport.request(
            "advanceScenarioRun", "POST", "/v1/scenario-runs/{runId}/advance",
            path_params={"runId": run_id},
            query={},
            headers={"Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

    def attach_scenario_run_observation(self, *, body: models.ScenarioRunObservationRequest, run_id: str, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Attach or refresh a persisted transaction observation\n\nAttaches one exact workspace-visible ModernEDI transaction to an attachable runtime-mapping or observation-only occurrence. The body identifies persisted transaction metadata; raw X12 is never accepted. The transaction must carry the exact partner-configuration fingerprint frozen into the applied binding; legacy or mismatched transactions are ineligible, while acknowledgments and receipts produced under a different configuration remain pending. Repeating the same slot and transaction with the current ETag and a new Idempotency-Key re-reads trusted transaction detail, refreshes pending mapping or acknowledgment evidence, and reevaluates the graph atomically. Reusing the original key is a pure replay and does not refresh evidence. Adapter-controlled steps reject client attachment. Mapper-derived facts use ordinary X12 Mapper semantics, with dynamic durability limits enforced before SQL persistence: collections contain at most 1000 scalar values; text scalars contain at most 4096 UTF-8 bytes; one canonical typed value contains at most 32768 bytes; and one observation's facts JSON contains at most 262144 bytes. A fact provenance receipt contains at most 4096 bytes. Each evidence document contains at most 8192 bytes, with at most 8 non-fact evidence documents and 524288 bytes of aggregate evidence JSON per observation. Capacity failures use fact_value_limit_exceeded, transaction_observation_capacity_exceeded, transaction_fact_evidence_capacity_exceeded, or transaction_evidence_capacity_exceeded. fact_evaluation_timeout and fact_evaluation_busy_or_limited return HTTP 409 with retryable=true and operationStatus=failed; reload the run if needed, then retry with its current ETag and a fresh Idempotency-Key to re-read trusted transaction evidence."
        return self._transport.request(
            "attachScenarioRunObservation", "POST", "/v1/scenario-runs/{runId}/observations",
            path_params={"runId": run_id},
            query={},
            headers={"Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

    def cancel_scenario_run(self, *, body: dict[str, Any], run_id: str, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Cancel an active scenario run\n\nRecords an actor-attributed operator cancellation as an inconclusive terminal result while preserving all evidence already gathered. Cancellation is optimistic-concurrency controlled and idempotent, and it does not interrupt a command that still owns the run. If a command stops without saving a result and its temporary ownership period expires, ModernEDI records that attempt as failed and claims cancellation as one durable change. If the abandoned command may already have affected an external system, its failed timeline entry remains available for manual reconciliation. Each run can store at most 256 command records. The initial start and all later ordinary commands share 253 records; the remaining three are held for one retry record, cancellation, and a retry of cancellation. Result documents for ordinary commands share a 32 MiB budget, with additional space held for those same three reserved records."
        return self._transport.request(
            "cancelScenarioRun", "POST", "/v1/scenario-runs/{runId}/cancel",
            path_params={"runId": run_id},
            query={},
            headers={"Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

    def download_scenario_evidence_report(self, *, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioEvidenceReport]:
        "Download the immutable evidence report for a terminal run\n\nCreates the report once from terminal durable state and thereafter returns the exact persisted canonical JSON. It records the frozen authority and redacted evidence needed to substantiate the bounded implementation-verification claim; it is not editable scenario source, raw X12, or a compliance certificate. Stable failure codes are included, while detailed failure messages remain in the run timeline so the credential-free proof stays within its fixed export bound. If a retry creates another audit record for the same successful state change, the report counts that change once and keeps its earliest record; the timeline still shows every attempt."
        return self._transport.request(
            "downloadScenarioEvidenceReport", "GET", "/v1/scenario-runs/{runId}/evidence-report",
            path_params={"runId": run_id},
            query={},
            headers={},
            body=None, response_type=models.ScenarioEvidenceReport, raw=False, options=options)

    def get_scenario_run(self, *, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunViewResponse]:
        "Read current scenario run state and evidence\n\nReturns the current durable revision, evidence-bearing observations, checks, outcome, and strong ETag. Sensitive fact values are redacted from the public representation."
        return self._transport.request(
            "getScenarioRun", "GET", "/v1/scenario-runs/{runId}",
            path_params={"runId": run_id},
            query={},
            headers={},
            body=None, response_type=models.ScenarioRunViewResponse, raw=False, options=options)

    def get_scenario_run_timeline(self, *, run_id: str, limit: int | None = None, cursor: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunTimelineResponse]:
        "Read the actor-attributed operation timeline for a run\n\nReturns a bounded, newest-first audit timeline without idempotency hashes, attempt tokens, transient credentials, or operation result payloads. The cursor is opaque and bound to both the workspace and run."
        return self._transport.request(
            "getScenarioRunTimeline", "GET", "/v1/scenario-runs/{runId}/timeline",
            path_params={"runId": run_id},
            query={"limit": limit, "cursor": cursor},
            headers={},
            body=None, response_type=models.ScenarioRunTimelineResponse, raw=False, options=options)

    def list_scenario_runs(self, *, limit: int | None = None, cursor: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCollection]:
        "List recent scenario conversations\n\nReturns a bounded workspace-scoped summary of recent runs for discovery and navigation without exposing fact values or evidence payloads."
        return self._transport.request(
            "listScenarioRuns", "GET", "/v1/scenario-runs",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            headers={},
            body=None, response_type=models.ScenarioRunCollection, raw=False, options=options)

    def start_scenario_run(self, *, body: models.StartScenarioRunRequest, idempotency_key: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Start a run from an exact applied binding\n\nStarts a durable run from exact definition and binding hashes in the binding's production or test traffic environment. Both environments share deployed mappings, but transactions, dispatch, acknowledgments, and evidence remain in the selected environment. Optional typed parameters are checked against the definition before any operation is accepted. Registered adapter targets prepare their selected-profile runtime dependencies before the run is inserted; temporary preparation failures are retryable and return Retry-After. Does not send EDI. It uses an already applied binding and never publishes authored definitions or applies desired configuration. The reserved browser-managed binding cannot be selected here; apply your own binding (including one using a managed example). The key is scoped to operations in this workspace, not restricted to Test traffic."
        return self._transport.request(
            "startScenarioRun", "POST", "/v1/scenario-runs",
            path_params={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

class ConfigurationAsCodeApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def apply_integration_configuration(self, *, body: models.ConfigurationApplyRequest, x_request_id: str | None = None, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationApplyOperationResponse]:
        "Apply a planned workspace configuration\n\n**Required key scope:** `configuration:write`.\n\nAtomically applies the exact desired bundle represented by a successful `POST /v1/configuration/plan` response. Send that response's non-null `planSha256` in the body and its exact quoted `currentSnapshotEtag` in `If-Match`. The body accepts the same `files` array as planning, including the optional exported `_state/snapshot.json` advisory file. The advisory file remains untrusted and never overrides live workspace state.\n\nModernEDI revalidates the package, current snapshot, active syntax-tree catalog, complete scenario impact, and planned operations while holding workspace configuration locks. Any drift fails closed; apply never silently substitutes a newer plan. Database mutations commit as one aggregate change, mapping updates retain immutable revision history, creates use the caller-supplied stable resource keys, and a desired Partner whose key was retired is restored under that same key. Public operations remain `CREATE`, `UPDATE`, and `DELETE`; there is no separate reactivation verb.\n\n`Idempotency-Key` is required and scoped to the authenticated API key within the workspace. Persist one stable key with the intended change and reuse it only with the identical `planSha256`, `If-Match`, and logical files. A replay through that same API key returns the same operation and sets `Idempotency-Replayed: true`; using the key for a different semantic request returns `409 idempotency_key_conflict`, with the original operation's ID in `error.details.operationId`. A different API key has a separate idempotency namespace, even for the same workspace.\n\nLocked revalidation failures return the complete freshly evaluated `ConfigurationPlanResponse` under `error.details.plan`. A `412 configuration_plan_stale` means the submitted snapshot or plan identity is no longer current. A `422 configuration_apply_not_applicable` means the refreshed plan has semantic blockers. Neither response mutates workspace configuration; resolve the refreshed diagnostics and call the planning endpoint again before another apply.\n\nA `200` response has `operation.status: SUCCEEDED`. A `202` response has `operation.status: PENDING`: the database transaction has already committed, but the one workspace runtime publication is still being retried. Do not submit a new apply. Poll the URL in `Location` or call `GET /v1/configuration/apply-operations/{operationId}` until the stored operation is `SUCCEEDED`. Request bodies may be at most 16 MiB (16,777,216 bytes).\n"
        return self._transport.request(
            "applyIntegrationConfiguration", "POST", "/v1/configuration/apply",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ConfigurationApplyOperationResponse, raw=False, options=options)

    def cancel_integration_configuration_verification(self, *, x_request_id: str | None = None, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationVerificationResponse]:
        "Cancel configuration verification\n\n**Required key scope:** `configuration:read`.\n\nOnly the API key that started the run can cancel it. Cancellation is persistent and prevents subsequent cases; the current bounded case may finish. Terminal results are unchanged."
        return self._transport.request(
            "cancelIntegrationConfigurationVerification", "POST", "/v1/configuration/verification-runs/{runId}/cancel",
            path_params={"runId": run_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationVerificationResponse, raw=False, options=options)

    def export_integration_configuration(self, *, x_request_id: str | None = None, if_none_match: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationExportResponse]:
        "Export the current workspace configuration bundle\n\n**Required key scope:** `configuration:read`.\n\nReturns the workspace's current AS2 connections, active partners, published mappings, and optional scenario definitions and bindings as a deterministic logical file bundle. The response is JSON; ModernEDI does not create a ZIP archive, temporary download, or server-side filesystem tree. A caller may materialize the returned paths locally. Commit the portable `MANIFEST`, `RESOURCE`, and `SOURCE` files when using source control; `_state/snapshot.json` is observed server state and is normally kept outside desired configuration.\n\nScenario documents use `spec.source` for their complete authored JSON. Bindings refer to the bundle's stable `partnerKey` and `mappingKey` UUIDs, never another workspace's numeric IDs. Optional syntax-tree pins remain optional. Retired scenario configuration, immutable runtime revisions and run evidence are excluded. See the [scenario configuration guide](https://www.modernedi.com/docs/scenarios/reference#configuration-and-git) and the linked resource schemas for examples and lifecycle rules.\n\nEvery file carries a SHA-256 digest over its logical bytes. JSON file hashes use UTF-8 canonical JSON with object keys sorted recursively and array order preserved. Text file hashes use the exact stored UTF-8 source text, including its line endings. Files are sorted lexicographically by `path`.\n\n`modernedi.json` is the desired-state manifest and its digest is `bundleSha256`. `_state/snapshot.json` records the current database ids and public API ETags that correspond to the portable resource keys; its digest is `snapshotSha256`. `snapshotEtag` is the quoted snapshot digest returned in the HTTP `ETag` header. The manifest, resource documents, and snapshot state use `apiVersion: modernedi.com/v1`.\n\nServer-managed secrets are excluded. Public partner certificates and mapping source are configuration and are included. Treat the result as sensitive workspace configuration, keep the API key on a trusted server, and review customer-authored map source before sharing it.\n"
        return self._transport.request(
            "exportIntegrationConfiguration", "GET", "/v1/configuration/export",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id, "If-None-Match": if_none_match},
            body=None, response_type=models.ConfigurationExportResponse, raw=False, options=options)

    def get_configuration_scenario_run_selection(self, *, x_request_id: str | None = None, operation_id: str, binding_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationScenarioRunSelectionResponse]:
        "Select a scenario run from an exact configuration apply\n\n**Required key scope:** `configuration:read`.\n\nAfter an aggregate apply reaches `SUCCEEDED`, resolve the authored binding ID from `ScenarioBinding` source `metadata.id` into the exact `selection` accepted by `POST /v1/scenario-runs`. The response contains frozen runtime hashes, not source-file hashes. No browser visit, configuration mutation, run creation, or EDI dispatch occurs. Unchanged bindings are selectable after a no-op apply too.\n\nThe complete current configuration snapshot must still equal this operation's `appliedSnapshotEtag`. A pending apply returns `409 configuration_apply_pending` with `Retry-After`; a different snapshot returns non-retryable `409 configuration_snapshot_changed`. A binding whose referenced runtime inputs are no longer current returns `409 scenario_binding_not_current`. Never silently substitute a later apply or recalculate hashes. Missing, retired, or reserved browser-managed bindings have no public selection.\n\nThis is a point-in-time selection, not a workspace lock, a run, or a guarantee of runtime readiness. Run admission rechecks the selected binding and its referenced inputs. Unrelated configuration changes after discovery do not automatically invalidate a run start. Supply any required definition parameters, and persist the final start body and a new run idempotency key before starting. Starting requires `scenario-runs:write`; run reads and actual sends have separate scopes.\n"
        return self._transport.request(
            "getConfigurationScenarioRunSelection", "GET", "/v1/configuration/apply-operations/{operationId}/scenario-run-selections/{bindingId}",
            path_params={"operationId": operation_id, "bindingId": binding_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationScenarioRunSelectionResponse, raw=False, options=options)

    def get_integration_configuration_applied_verification(self, *, x_request_id: str | None = None, operation_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationAppliedVerificationResponse]:
        "Read verification linked to an apply\n\n**Required key scope:** `configuration:read`.\n\nReturns the server run explicitly selected by verificationRunId during apply, or null when none is retained. Ordinary applies do not require verification."
        return self._transport.request(
            "getIntegrationConfigurationAppliedVerification", "GET", "/v1/configuration/apply-operations/{operationId}/verification",
            path_params={"operationId": operation_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationAppliedVerificationResponse, raw=False, options=options)

    def get_integration_configuration_apply_operation(self, *, x_request_id: str | None = None, operation_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationApplyOperationResponse]:
        "Get a configuration apply operation\n\n**Required key scope:** `configuration:read`.\n\nReturns the workspace-scoped immutable result of one aggregate apply. Operation ids use `apply-` followed by a canonical UUID. `PENDING` means the database change already committed and only runtime publication remains; `SUCCEEDED` is terminal. Poll only when a prior POST returned `202`, honoring its `Retry-After` value.\n"
        return self._transport.request(
            "getIntegrationConfigurationApplyOperation", "GET", "/v1/configuration/apply-operations/{operationId}",
            path_params={"operationId": operation_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationApplyOperationResponse, raw=False, options=options)

    def get_integration_configuration_context(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationContextResponse]:
        "Identify the calling workspace and API key\n\n**Required key scope:** `configuration:read`.\n\nConfirms the workspace ID, calling key ID, label, and currently granted scopes using the same authentication as every configuration operation. Automation can compare these IDs with its approved target before proceeding. The workspace is derived from the key, not a request parameter. This does not enumerate users, other workspaces, or other keys, and never returns the key value, prefix, hash, or credentials. It is not an authorization lease; every subsequent request is independently authorized.\n"
        return self._transport.request(
            "getIntegrationConfigurationContext", "GET", "/v1/configuration/context",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationContextResponse, raw=False, options=options)

    def get_integration_configuration_external_repository(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationExternalRepositoryResponse]:
        "Read external repository synchronization status\n\n**Required key scope:** `configuration:read`.\n\nReturns the connection already configured by a workspace owner, its automatic synchronization status, last synchronized commits, and optional import-test reference. `connected: false` is normal when Git is not configured. This is a database status read, not a remote Git fetch or synchronization trigger. The commit fields describe the last successful synchronization; they are not an attestation of the current remote branch HEAD. Connecting, disconnecting, changing import-test policy, retrying, and resolving conflicts remain owner actions in the browser. Provider tokens, usernames, secret-store references, and internal lease state are excluded.\n"
        return self._transport.request(
            "getIntegrationConfigurationExternalRepository", "GET", "/v1/configuration/external-repository",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationExternalRepositoryResponse, raw=False, options=options)

    def get_integration_configuration_import_verification(self, *, x_request_id: str | None = None, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationImportVerificationResponse]:
        "Read the current external import's saved-case evidence\n\n**Required key scope:** `configuration:read`.\n\nUse the `importVerification.runId` from the connection status. Returns the existing server-owned verification result for that connection's current import attempt. A `200` with `run: null` means the attempt was reserved but no retained result is available (for example, admission did not succeed or evidence expired); it never means a pass. A different attempt, disconnected repository, unknown ID, or another workspace's ID returns `404 verification_not_found`. Re-read connection status if the attempt changes. This endpoint does not run cases, retry an import, apply configuration, or send EDI. Previously retained results can still be read using the ordinary verification-run endpoint.\n"
        return self._transport.request(
            "getIntegrationConfigurationImportVerification", "GET", "/v1/configuration/external-repository/verification/{runId}",
            path_params={"runId": run_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationImportVerificationResponse, raw=False, options=options)

    def get_integration_configuration_verification(self, *, x_request_id: str | None = None, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationVerificationResponse]:
        "Read configuration verification\n\n**Required key scope:** `configuration:read`.\n\nReturns persisted outcomes and freshly checked configuration, evaluator and catalog identity. Any read-capable key in the same workspace can read a run."
        return self._transport.request(
            "getIntegrationConfigurationVerification", "GET", "/v1/configuration/verification-runs/{runId}",
            path_params={"runId": run_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationVerificationResponse, raw=False, options=options)

    def list_integration_configuration_apply_operations(self, *, x_request_id: str | None = None, limit: int | None = None, cursor: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationApplyOperationHistoryResponse]:
        "List workspace configuration changes\n\n**Required key scope:** `configuration:read`.\n\nLists the same workspace-wide change history shown in the browser, including browser, API, and automatic Git imports. Newest requests come first, with operation ID breaking timestamp ties. Entries are compact summaries; fetch the existing operation endpoint for its full change list. Pass `nextCursor` unchanged to retrieve the next page and stop when it is null. Cursors belong to one workspace. Pagination is not a frozen snapshot: new changes can arrive during a scan, so re-read the first page when checking for drift. This endpoint does not advance pending publications or mutate configuration.\n"
        return self._transport.request(
            "listIntegrationConfigurationApplyOperations", "GET", "/v1/configuration/apply-operations",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationApplyOperationHistoryResponse, raw=False, options=options)

    def plan_integration_configuration(self, *, body: models.ConfigurationPlanRequest, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationPlanResponse]:
        "Plan desired workspace configuration\n\n**Required key scope:** `configuration:read`.\n\nCompares a portable desired configuration bundle with the workspace's current AS2 connections, active partners, published mappings, and optional scenario definitions and bindings. Planning is read-only: it does not create, update, retire, publish, or reapply anything, and it does not require an idempotency key.\n\nSubmit exactly one `MANIFEST` at `modernedi.json` plus every `RESOURCE` and `SOURCE` file inventoried by that manifest. You may pass the `files` array from configuration export unchanged: its single `_state/snapshot.json` `STATE` file is accepted as advisory context, but current workspace configuration remains authoritative. A stale advisory snapshot adds the `BASE_SNAPSHOT_STALE` warning; it does not make old database ids or ETags desired state. ModernEDI verifies safe paths, closed JSON objects, canonical file hashes, manifest inventory, stable resource keys, cross-resource references, mapping source, aggregate runtime limits, and the active syntax-tree catalog before comparing desired and current state.\n\nA structurally valid bundle always receives `200`, even when the desired state cannot be applied. Inspect `applicable` and every entry in `diagnostics`; each diagnostic carries an RFC 6901 JSON Pointer into the submitted request. `operations` contains only `CREATE`, `UPDATE`, and `DELETE` entries. `summary.unchanged` reports resources omitted from that array because their complete portable configuration is already current.\n\nScenario bindings are compiled against the complete proposed configuration, so one apply can create their partners and maps too. Changing a referenced resource adds a binding `UPDATE` with unchanged authored content hashes: this creates a fresh runtime revision in the same transaction. `refreshScenarioBindings` explicitly requests that behavior for otherwise unchanged binding resource keys; include the same array in the apply request. Export followed by plan without refresh requests is a no-op.\n\n`scenarioImpactComplete` is false when ModernEDI could not safely determine every affected applied scenario. `affectedScenarios` distinguishes bindings refreshed by this apply (`REAPPLIED_BY_APPLY`), retired by it (`RETIRED_BY_APPLY`), or requiring a separate reapplication (`REAPPLY_REQUIRED`). `affectedRuns` identifies ACTIVE runs pinned to impacted binding revisions; those runs must be cancelled or completed before re-planning. `planSha256` is present only when the plan is applicable and binds the desired bundle, current snapshot, validation context, operations, and scenario impact. A later apply request must still prove that exact plan is current; this endpoint grants no mutation authority.\n\nCommon planning diagnostics have deliberate recovery paths:\n\n- `BASE_SNAPSHOT_STALE` is a warning that the optional exported snapshot no longer matches the workspace. The returned plan still uses live current state.\n- `STAGED_CHANGE_REQUIRED` is an error when a natural identity such as an AS2 identifier or X12 sender identity belongs to another stable resource key. Release it from the current owner in a separate apply, export again, and then plan the transfer.\n- `ACTIVE_SCENARIO_RUNS_AFFECTED` is an error when a change would alter authority used by an ACTIVE scenario run. Complete or cancel every listed `affectedRuns` entry and plan again.\n\nMalformed envelopes, unsafe or duplicate paths, unsupported file roles, a noncanonical advisory `STATE` file, hash mismatches, and inconsistent manifests return `400 configuration_plan_invalid` with the same diagnostic shape in `error.details.diagnostics`. Request bodies may be at most 16 MiB (16,777,216 bytes).\n"
        return self._transport.request(
            "planIntegrationConfiguration", "POST", "/v1/configuration/plan",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.ConfigurationPlanResponse, raw=False, options=options)

    def verify_integration_configuration(self, *, body: models.ConfigurationVerificationRequest, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationVerificationResponse]:
        "Verify saved cases in an exact configuration plan\n\n**Required key scope:** `configuration:read`.\n\nOptional and side-effect-free: re-plans the submitted bundle and verifies all saved mapping cases on the server. Supports up to 25 tested mappings and 100 cases in a 30-second suite. Uses the same incoming/JSLT/XSLT engines as Mapper reviews. Mappings without cases are counted explicitly. No raw input/output is retained. One active verification and 30 starts per workspace per hour are shared with browser reviews. Same requestId and identical content replay the persisted run. This endpoint never applies configuration or executes AS2/scenarios. A network interruption does not imply cancellation; GET the deterministic verify-{requestId} run before retrying."
        return self._transport.request(
            "verifyIntegrationConfiguration", "POST", "/v1/configuration/verification-runs",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.ConfigurationVerificationResponse, raw=False, options=options)

class OutboundAS2Api:
    def __init__(self, transport: Transport):
        self._transport = transport

    def carbon_copy_generated_x12(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, original_message_id: str, original_transaction_key: str | None = None, copy_to_partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send already-generated X12 to a carbon-copy partner\n\n**Required key scope:** `messages:write`.\nSends supplied X12 to a second partner while preserving the original transaction context. ModernEDI validates the X12 but does not apply an outgoing map. Select the original partner with `partnerId` and the recipient with `copyToPartnerId`. Use `originalTransactionKey` when the original AS2 message contains more than one transaction set.\n"
        return self._transport.request(
            "carbonCopyGeneratedX12", "POST", "/v1/as2/x12/carbonCopy",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key, "copyToPartnerId": copy_to_partner_id},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    def preview_outbound_x12(self, *, body: RequestBody, x_request_id: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, options: RequestOptions | None = None) -> ApiResponse[models.OutboundPreviewResponse]:
        "Transform and validate an outbound document without sending it\n\n**Required key scope:** `messages:write`.\nUses the same partner, X12 metadata, content type, source body, params, and business-key contract as `/v1/as2/send`, but stops after mapping and X12 validation. It returns generated X12, validation details, mapping provenance, the resolved partner, and the optional business key. It does not contact the trading partner, create an outbound transaction, or require the partner's AS2 endpoint to be configured. Use it to validate a production-shaped request before the first live send.\n"
        return self._transport.request(
            "previewOutboundX12", "POST", "/v1/as2/preview",
            path_params={},
            query={"partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.OutboundPreviewResponse, raw=False, options=options)

    def reply_to_inbound_as2_message(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int | None = None, x12_version: str | None = None, functional_group_type: str | None = None, transaction_group_type: int | None = None, original_message_id: str, original_transaction_key: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send a follow-up document tied to an inbound message\n\n**Required key scope:** `messages:write`.\nSends a follow-up document such as an ASN or invoice in response to a previously received inbound message. Send the source XML, JSON, or text input as the HTTP request body. ModernEDI looks up the original message by `originalMessageId`, and uses unambiguous metadata from that inbound transaction to recover an omitted partner selector and `x12Version`. When the inbound AS2 message contains more than one transaction set, send `originalTransactionKey` to bind the reply to the exact `GS06#ST02` transaction. ModernEDI validates that composite reference before transforming or sending; an unknown or non-inbound reference returns `404`. When it is omitted, ModernEDI resolves and persists the key only if the message contains exactly one inbound transaction; an ambiguous multi-transaction message returns `400`. This lookup uses production transaction history by default; send `test=true` to infer from and link to isolated test history. ModernEDI uses the persisted `partnerId`, so the reply still selects the same partner after its configured name changes. Transactions without a persisted partner id do not supply inferred partner metadata. An explicit `partnerId` always overrides inferred partner metadata. After the partner id, X12 version, and request `Content-Type` are known, ModernEDI can also fill omitted `functionalGroupType` and `transactionGroupType` when those selectors match exactly one outgoing reply map. ModernEDI then selects the matching outgoing map by partner, X12 version, functional group, transaction set, and request `Content-Type`, generates and validates X12, then sends the reply through the configured AS2 connection. Send `x12Version` explicitly when a partner requires reply documents on a different X12 version than the one they send; explicit query parameters override inferred metadata. If multiple reply maps could match, send `functionalGroupType` and `transactionGroupType` explicitly. The original inbound document type is not reused as the reply type; these fields identify the generated reply document, such as `IN`/`810` for an invoice. JSON source maps can use XSLT with Saxon `json-to-xml($json)` or JSLT. For JSLT, ModernEDI sets the current input `.` to a wrapper object, so the source document is read through `.input` paths. If the outgoing map needs extra runtime parameters, send the JSON envelope shape with `input`, `contentType`, and `params`; XSLT maps receive those values as top-level stylesheet parameters, JSLT maps read them from `.params`, and mapper-editor params files are not used as live defaults. Use the envelope's optional `businessKey` field when the reply has a stable identifier, such as an invoice number, that should be stored on the outbound transaction record.\n"
        return self._transport.request(
            "replyToInboundAs2Message", "POST", "/v1/as2/reply",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    def reply_with_generated_x12(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int | None = None, x12_version: str | None = None, functional_group_type: str, transaction_group_type: int, original_message_id: str, original_transaction_key: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Reply to an inbound message with already-generated X12\n\n**Required key scope:** `messages:write`.\nSends X12 that your system generated as a reply tied to an inbound AS2 message. ModernEDI does not apply an outgoing map. When the partner or X12 version is omitted, `originalMessageId` can recover it from the selected transaction history. Use `originalTransactionKey` to bind a reply to one exact transaction in a multi-ST message; the composite reference is validated before delivery. Production history is the default; send `test=true` to infer from and link to isolated test history. The functional group and transaction-set identifiers describe the reply document and remain required because they are not copied from the original inbound document.\n"
        return self._transport.request(
            "replyWithGeneratedX12", "POST", "/v1/as2/x12/reply",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    def send_as2_carbon_copy(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, original_message_id: str, original_transaction_key: str | None = None, copy_to_partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send a carbon copy of an inbound message flow to another partner\n\n**Required key scope:** `messages:write`.\nSends a generated X12 document to a second partner while preserving context from a previously received inbound message. Send the source XML, JSON, or text input as the HTTP request body. The `partnerId` query parameter identifies the source/original partner whose outgoing map should generate the X12, and `copyToPartnerId` identifies the destination partner for the copied AS2 envelope. ModernEDI selects the matching outgoing map for that original/source partner, generates and validates X12, then forwards the carbon copy through the configured AS2 connection. Example: to generate an 856 ASN for Retailer One and copy it to Broker One, send `partnerId=1` and `copyToPartnerId=2`; ModernEDI uses partner 1's outgoing 856 map. `copyToPartnerId` does not select the outgoing map. JSON source maps can use XSLT with Saxon `json-to-xml($json)` or JSLT. For JSLT, ModernEDI sets the current input `.` to a wrapper object, so the source document is read through `.input` paths. If the outgoing map needs extra runtime parameters, send the JSON envelope shape with `input`, `contentType`, and `params`; the map is still selected by `partnerId`, not by `copyToPartnerId`. XSLT maps receive params as top-level stylesheet parameters, JSLT maps read them from `.params`, and mapper-editor params files are test fixtures only and are not read by live carbon-copy calls. The envelope's optional `businessKey` is recorded on the copied outbound transaction, but it does not affect map selection. Send `originalTransactionKey` when the source message contains multiple transaction sets and this copy belongs to one exact transaction.\n"
        return self._transport.request(
            "sendAs2CarbonCopy", "POST", "/v1/as2/carbonCopy",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key, "copyToPartnerId": copy_to_partner_id},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    def send_as2_message(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send a standalone outbound document\n\n**Required key scope:** `messages:write`.\nSends a standalone outbound document to the configured trading partner. Send the source XML, JSON, or text input as the HTTP request body. ModernEDI looks up the matching outgoing map by partner, X12 version, functional group, transaction set, and request `Content-Type`, applies that map to generate X12, syntax-checks the generated X12, then sends it through the configured AS2 connection. JSON source maps can use XSLT with Saxon `json-to-xml($json)` or JSLT. For JSLT, ModernEDI sets the current input `.` to a wrapper object, so the source document is read through `.input` paths. Send `partnerId` to select the partner; use `GET /v1/partners` when your integration client needs to discover stable partner ids. If the outgoing map needs extra runtime parameters such as a bill-of-lading number, pallet list, or generated control number, send the JSON envelope shape with `input`, `contentType`, and `params`. The envelope can also include `businessKey` when your system knows a stable purchase order, shipment, BOL, or other business identifier that should appear on the outbound transaction record. XSLT maps receive those params as top-level stylesheet parameters; JSLT maps receive them under `.params`. Mapper-editor params files are test fixtures only; live API calls must provide required params in this request envelope.\n"
        return self._transport.request(
            "sendAs2Message", "POST", "/v1/as2/send",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    def send_generated_x12_message(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send an already-generated X12 document\n\n**Required key scope:** `messages:write`.\nSends X12 that your system generated without applying a ModernEDI outgoing map. ModernEDI parses and validates the supplied X12, builds the AS2 message, and delivers it through the selected partner connection. Supply the X12 directly with `Content-Type: application/edi-x12` (or `text/plain`), or use the JSON envelope when you also want to record a business key. The partner selector and X12 metadata remain explicit so ModernEDI can choose and audit the correct destination. Use `/v1/as2/send` instead when ModernEDI should map your business document into X12 first.\n"
        return self._transport.request(
            "sendGeneratedX12Message", "POST", "/v1/as2/x12/send",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

class AS2ConnectionsApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def get_integration_as2_connection(self, *, x_request_id: str | None = None, connection_id: int, options: RequestOptions | None = None) -> ApiResponse[models.As2ConnectionResponse]:
        "Get a partner AS2 connection\n\n**Required key scope:** `configuration:read`.\n\nReturns one public AS2 connection configuration and the ETag that identifies this observed resource version. To change or remove the connection, use the aggregate export–plan–apply workflow.\n"
        return self._transport.request(
            "getIntegrationAs2Connection", "GET", "/v1/as2/connections/{connectionId}",
            path_params={"connectionId": connection_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.As2ConnectionResponse, raw=False, options=options)

    def list_integration_as2_connections(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.As2ConnectionListResponse]:
        "List partner AS2 connections\n\n**Required key scope:** `configuration:read`.\n\nReturns every partner AS2 connection in this tenant. Certificates are partner public X.509 certificates formatted as PEM. Private keys and secret locations are never returned.\n"
        return self._transport.request(
            "listIntegrationAs2Connections", "GET", "/v1/as2/connections",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.As2ConnectionListResponse, raw=False, options=options)

class PartnersApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def get_integration_as2_profile(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.As2ProfileResponse]:
        "Get the tenant's public AS2 profile\n\n**Required key scope:** `configuration:read`.\nReturns the safe connection sheet your trading partners need: production and test AS2 URLs and identifiers, X12 sender identities, static network addresses included in the current plan, and active or next public certificates. Private keys, secret ARNs, billing contacts, and internal infrastructure identifiers are never returned. Network capability status is `ready`, `pending`, or `not_included`.\n"
        return self._transport.request(
            "getIntegrationAs2Profile", "GET", "/v1/as2/profile",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.As2ProfileResponse, raw=False, options=options)

    def get_integration_partner(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.PartnerResponse]:
        "Get a trading partner\n\n**Required key scope:** `configuration:read`.\n\nReturns the complete active public partner configuration. Retired partners return `404`; their retained rows are used only for historical transaction authorization. The response never exposes internal header overrides or infrastructure settings. The `ETag` header and `partner.etag` identify this observed resource version. To change or retire the partner, export the workspace configuration, edit its portable partner resource, plan the aggregate change, and apply that exact plan.\n"
        return self._transport.request(
            "getIntegrationPartner", "GET", "/v1/partners/{partnerId}",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.PartnerResponse, raw=False, options=options)

    def get_integration_partner_capabilities(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.PartnerCapabilitiesResponse]:
        "Inspect a partner's published mapping capabilities\n\n**Required key scope:** `configuration:read`.\nReturns the selected partner plus its published incoming and outgoing mapping capabilities. Use this before sending to discover the exact X12 version, functional group, transaction set, source content type, and transform type that are currently configured. `productionReady` and `testReady` report whether the corresponding AS2 destination endpoint is configured; a published mapping can exist before either endpoint is ready.\n"
        return self._transport.request(
            "getIntegrationPartnerCapabilities", "GET", "/v1/partners/{partnerId}/capabilities",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.PartnerCapabilitiesResponse, raw=False, options=options)

    def list_integration_partners(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.PartnerListResponse]:
        "List configured trading partners\n\n**Required key scope:** `configuration:read`.\nReturns the tenant's active configured trading partners in workspace order. Retired partners are excluded. Use `partnerId` from this response as the `partnerId` query parameter on `/v1/as2/send`, `/v1/as2/reply`, or `/v1/as2/carbonCopy` when your integration selects the outbound partner. The returned `name` is display metadata; use `copyToPartnerId` for the carbon-copy recipient. Partners can appear before their AS2 profile is complete so teams can publish and test maps during onboarding; `as2ConnectionConfigured` tells you whether live AS2 delivery can use that partner yet.\n"
        return self._transport.request(
            "listIntegrationPartners", "GET", "/v1/partners",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.PartnerListResponse, raw=False, options=options)

class MappingsApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def get_integration_mapping(self, *, x_request_id: str | None = None, mapping_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappingResponse]:
        "Get a published mapping\n\n**Required key scope:** `configuration:read`.\n\nReturns one published map, its complete source text, safe output configuration, delivery category, and observed resource ETag. To change or retire the map, use the aggregate export–plan–apply workflow or the browser editor's reviewed deployment flow.\n"
        return self._transport.request(
            "getIntegrationMapping", "GET", "/v1/mappings/{mappingId}",
            path_params={"mappingId": mapping_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingResponse, raw=False, options=options)

    def get_integration_mapping_configuration_revision(self, *, x_request_id: str | None = None, mapping_id: int, revision_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappingConfigurationRevisionResponse]:
        "Get a historical mapping configuration revision\n\n**Required key scope:** `configuration:read`.\n\nReturns the identity, syntax-tree provenance, and complete stored configuration for one immutable historical mapping-configuration revision. The revision must belong to the tenant-scoped mapping in the path.\n"
        return self._transport.request(
            "getIntegrationMappingConfigurationRevision", "GET", "/v1/mappings/{mappingId}/revisions/{revisionId}",
            path_params={"mappingId": mapping_id, "revisionId": revision_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingConfigurationRevisionResponse, raw=False, options=options)

    def list_integration_mapping_configuration_revisions(self, *, x_request_id: str | None = None, mapping_id: int, cursor: str | None = None, limit: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingConfigurationRevisionListResponse]:
        "List a mapping's configuration history\n\n**Required key scope:** `configuration:read`.\n\nReturns one page of immutable mapping-configuration revisions, newest first. A configuration-only change creates a distinct revision even when its transform source is unchanged. Page entries intentionally omit source text; fetch one revision by id to preview or diff its transform. Follow `nextCursor` while `hasMore` is true. Cursors are opaque and must be sent back unchanged.\n\n`currentRevision` always contains the complete currently published transform source and exact configuration identity, even when that configuration's chronological entry is outside this page. It and `currentEtag` are read from the same locked configuration snapshot, so clients can use them as an authoritative diff baseline. If `currentEtag` changes between page requests, restart from the first page before presenting a coherent history view.\n\n`sourceHash` identifies only transform text. `configurationSha256` identifies the complete immutable mapping configuration and may be `null` for a legacy revision recorded before exact configuration identities. `current` compares the complete configuration identity. The API exposes the retained transform and configuration for inspection, diffing, and reviewed desired-configuration workflows.\n"
        return self._transport.request(
            "listIntegrationMappingConfigurationRevisions", "GET", "/v1/mappings/{mappingId}/revisions",
            path_params={"mappingId": mapping_id},
            query={"cursor": cursor, "limit": limit},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingConfigurationRevisionListResponse, raw=False, options=options)

    def list_integration_mappings(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingListResponse]:
        "List published mappings\n\n**Required key scope:** `configuration:read`.\n\nReturns the tenant's published incoming and outgoing maps, including the full transform source, delivery category, and each resource ETag. Infrastructure details are never exposed.\n"
        return self._transport.request(
            "listIntegrationMappings", "GET", "/v1/mappings",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingListResponse, raw=False, options=options)

class MappingRuntimeApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def get_integration_mapping_runtime_failure(self, *, x_request_id: str | None = None, failure_id: str, options: RequestOptions | None = None) -> ApiResponse[models.MappingRuntimeFailureResponse]:
        "Get one mapping runtime failure\n\n**Required key scope:** `transactions:read`.\nReturns one safe diagnostic by its opaque `failureId`. The id is still checked against the authenticated tenant; knowing another tenant's id never grants access.\n"
        return self._transport.request(
            "getIntegrationMappingRuntimeFailure", "GET", "/v1/integration/mapping-runtime/failures/{failureId}",
            path_params={"failureId": failure_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingRuntimeFailureResponse, raw=False, options=options)

    def get_integration_mapping_runtime_health(self, *, x_request_id: str | None = None, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingRuntimeHealthResponse]:
        "Get mapping runtime health\n\n**Required key scope:** `transactions:read`.\nReturns aggregate unresolved and recovered mapping outcomes for the selected environment. This view includes failures that occurred before an X12 transaction could be created, so its totals can be non-zero even when no corresponding transaction appears in the transaction list. `truncated=true` means the bounded health scan could not summarize every retained attempt; use the paginated failures endpoint for investigation.\n"
        return self._transport.request(
            "getIntegrationMappingRuntimeHealth", "GET", "/v1/integration/mapping-runtime/health",
            path_params={},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingRuntimeHealthResponse, raw=False, options=options)

    def list_integration_mapping_runtime_failures(self, *, x_request_id: str | None = None, environment: str | None = None, mapping_id: int | None = None, direction: str | None = None, resolved: bool | None = None, cursor: str | None = None, limit: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingRuntimeFailuresResponse]:
        "List mapping runtime failures\n\n**Required key scope:** `transactions:read`.\nReturns safe, tenant-scoped mapping failure diagnostics in reverse chronological order. The response deliberately omits raw source input, generated output, stack traces, and internal exception text. A failure whose `transactionReference` is null occurred before a transaction existed. For those pre-transaction outbound failures, `correlationId` is a ModernEDI request-correlation identifier rather than an AS2 Message-Id, and `transactionKey` is `outbound-request`.\nUse `failureId` as the stable investigation and deduplication key. `resolved=true` means a later equivalent mapping attempt succeeded; it does not mean an AS2 document was sent, delivered, or acknowledged.\n"
        return self._transport.request(
            "listIntegrationMappingRuntimeFailures", "GET", "/v1/integration/mapping-runtime/failures",
            path_params={},
            query={"environment": environment, "mappingId": mapping_id, "direction": direction, "resolved": resolved, "cursor": cursor, "limit": limit},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingRuntimeFailuresResponse, raw=False, options=options)

class TransactionViewerApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def get_integration_transaction(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionDetailResponse]:
        "Get transaction detail\n\n**Required key scope:** `transactions:read`.\nReturns a metadata-first transaction aggregate: the summary, mapped output provenance and managed handoff state, normalized acknowledgment status, a document index, timeline events, compact linked-reply summaries, and the complete mapping-attempt history used to explain `needsAttention`. Document bodies are returned only by the individual document endpoint.\n"
        return self._transport.request(
            "getIntegrationTransaction", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionDetailResponse, raw=False, options=options)

    def get_integration_transaction_document(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, document_id: str, options: RequestOptions | None = None) -> ApiResponse[models.TransactionDocumentResponse]:
        "Get one transaction document\n\n**Required key scope:** `transactions:read`.\nReturns one complete retained artifact selected by the stable transaction-local `documentId` from the document list. A document id is not a mapped-output queue id and cannot be used to acknowledge delivery. The returned body is untrusted external content and must be rendered as untrusted external content: escape text, sanitize any supported markup, and sandbox richer previews instead of inserting it directly into a page.\n"
        return self._transport.request(
            "getIntegrationTransactionDocument", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/documents/{documentId}",
            path_params={"messageId": message_id, "transactionKey": transaction_key, "documentId": document_id},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionDocumentResponse, raw=False, options=options)

    def get_integration_transaction_documents(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionDocumentsResponse]:
        "Get transaction documents\n\n**Required key scope:** `transactions:read`.\nReturns a lightweight metadata index for raw X12, mapped inbound outputs, MDN reports, acknowledgements, and HTTP responses recorded for the transaction. It never returns document bodies. Fetch one selected body from the individual document endpoint when an operator opens it.\n"
        return self._transport.request(
            "getIntegrationTransactionDocuments", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/documents",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionDocumentsResponse, raw=False, options=options)

    def get_integration_transaction_events(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionEventsResponse]:
        "Get transaction events\n\n**Required key scope:** `transactions:read`.\nReturns a normalized timeline for the transaction, including receipt or send events, mapping events, MDNs, acknowledgements, mapped-output availability/delivery/redelivery/attention/acknowledgment, and linked replies. These entries are derived from current persisted evidence; an output acknowledgment means acknowledged by your integration, not accepted by a downstream business system.\n"
        return self._transport.request(
            "getIntegrationTransactionEvents", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/events",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionEventsResponse, raw=False, options=options)

    def get_related_integration_transactions(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.RelatedTransactionsResponse]:
        "Get linked reply transactions\n\n**Required key scope:** `transactions:read`.\nReturns compact summaries of outbound reply transactions linked to an inbound transaction. Follow a summary's `messageId` and `transactionKey` to fetch its metadata-first detail or document index. Replies are included only when `replyToTransactionKey` identifies that exact transaction inside `replyToMessageId`. Use the returned linkage fields rather than inferring relationships from document type.\n"
        return self._transport.request(
            "getRelatedIntegrationTransactions", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/related",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.RelatedTransactionsResponse, raw=False, options=options)

    def list_integration_transactions(self, *, x_request_id: str | None = None, environment: str | None = None, needs_attention: bool | None = None, attention_reason: list[models.TransactionAttentionReason] | None = None, mapping_status: list[models.FilterableTransactionMappingStatus] | None = None, functional_ack_status: list[models.FilterableFunctionalAcknowledgmentStatus] | None = None, implementation_ack_status: list[models.FilterableImplementationAcknowledgmentStatus] | None = None, mdn_status: list[models.FilterableTransactionMdnStatus] | None = None, start_date: str | None = None, end_date: str | None = None, cursor: str | None = None, limit: int | None = None, direction: str | None = None, partner_name: str | None = None, partner_id: int | None = None, transaction_set: str | None = None, business_key: str | None = None, message_id: str | None = None, reply_to_message_id: str | None = None, transaction_control_number: str | None = None, functional_group_control_number: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionListResponse]:
        "List transactions\n\n**Required key scope:** `transactions:read`.\nReturns a pageable transaction history for custom transaction viewers, dashboards, and reconciliation workflows. Outbound replies include `replyToMessageId` so they can be shown underneath the inbound document they answer. Each row includes the stable `needsAttention` operator signal, machine-readable `attentionReasons`, and a compact `mappingStatus` so unattended integrations can route failures without fetching every transaction detail. `functionalAckStatus`, `implementationAckStatus`, and `mdnStatus` expose the same compact status values used by their exact list filters. The root `attentionSummary` is an environment-wide count and reconciliation-freshness signal; it is not restricted to the requested page or date window. Exact mapping, functional-acknowledgment, implementation-acknowledgment, and MDN filters use that same asynchronous projection, so check `attentionSummary.freshness.complete` before treating an empty filtered page as proof that no matching transaction exists.\n"
        return self._transport.request(
            "listIntegrationTransactions", "GET", "/v1/integration/transactions",
            path_params={},
            query={"environment": environment, "needsAttention": needs_attention, "attentionReason": attention_reason, "mappingStatus": mapping_status, "functionalAckStatus": functional_ack_status, "implementationAckStatus": implementation_ack_status, "mdnStatus": mdn_status, "startDate": start_date, "endDate": end_date, "cursor": cursor, "limit": limit, "direction": direction, "partnerName": partner_name, "partnerId": partner_id, "transactionSet": transaction_set, "businessKey": business_key, "messageId": message_id, "replyToMessageId": reply_to_message_id, "transactionControlNumber": transaction_control_number, "functionalGroupControlNumber": functional_group_control_number},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionListResponse, raw=False, options=options)

    def replay_integration_transaction(self, *, body: models.TransactionReplayRequest, x_request_id: str | None = None, message_id: str, transaction_key: str, idempotency_key: str, options: RequestOptions | None = None) -> ApiResponse[models.TransactionReplayResponse]:
        "Replay an inbound transaction without redelivery\n\n**Required key scope:** `transactions:replay`.\n\nRe-runs mapping for one tenant-visible inbound transaction with the currently published maps and returns the regenerated mapped outputs directly. Historical map revision replay is not part of the public API.\n\nThe only supported delivery is `response_only`. ModernEDI does not put regenerated outputs on the mapped-output queue, invoke mapped-output webhooks, or generate outbound acknowledgements. This endpoint is therefore suitable for inspection and controlled recovery without repeating downstream delivery side effects.\n\nReplay re-applies the currently active inbound protection policy. The stored inbound row must contain successful `signatureVerified` and `encryptionDecrypted` evidence for every protection required in the selected environment. A missing or `false` evidence value fails closed with an `insufficient-message-security:` replay error; consequently, older transactions without that evidence are not replayable while the corresponding protection remains required.\n\n`Idempotency-Key` is required. Repeating the same key and request returns the stored successful replay with `Idempotency-Replayed: true` and does not invoke mapping again. Reusing the key for different replay input returns `409 idempotency_key_conflict`; retry while the same replay is still processing returns `409 idempotency_key_in_progress` with `retryable: true`.\n\nThe replay body is strict JSON: unknown fields are rejected, and `environment`, `mode`, `delivery`, and `reason` must be strings when present (`reason` may also be `null`). Type mismatches return `400 invalid_request` with the offending JSON pointer.\n"
        return self._transport.request(
            "replayIntegrationTransaction", "POST", "/v1/integration/transactions/{messageId}/{transactionKey}/replays",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.TransactionReplayResponse, raw=False, options=options)

    def unwatch_integration_transaction(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionWatchResponse]:
        "Stop watching a transaction\n\n**Required key scope:** `transactions:write`.\nIdempotently removes a tenant-visible transaction from the selected environment's operator watchlist. The response reports `onWatchlist: false` even when the transaction was already unwatched, so retrying after a network failure is safe. Workspace-wide attention counts and status-filter projections are asynchronous; use their `freshness` object when reconciling an immediately following list response.\n"
        return self._transport.request(
            "unwatchIntegrationTransaction", "DELETE", "/v1/integration/transactions/{messageId}/{transactionKey}/watch",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionWatchResponse, raw=False, options=options)

    def validate_integration_transaction_x12(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionX12ValidationResponse]:
        "Validate the X12 retained for a transaction\n\n**Required key scope:** `transactions:read`.\nParses and validates the X12 content ModernEDI retained for this transaction and returns the same structured validation model as `POST /v1/x12/validate`. Invalid X12 is a successful analysis response with `validation.valid=false`, not an HTTP error. The retained X12 can be a complete interchange containing more than one transaction set; use the returned group and transaction indexes when displaying errors. This read-only endpoint lets transaction-viewer keys inspect stored content without granting message-send or transaction-replay authority. It does not rerun mappings, create mapped outputs, replay the transaction, or resend a document.\n"
        return self._transport.request(
            "validateIntegrationTransactionX12", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/x12/validation",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionX12ValidationResponse, raw=False, options=options)

    def watch_integration_transaction(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionWatchResponse]:
        "Watch a transaction\n\n**Required key scope:** `transactions:write`.\nIdempotently adds a tenant-visible transaction to the selected environment's operator watchlist. Public API watch entries do not expire and remain active until the DELETE operation removes them. The response reports the resulting state, so retrying the same request is safe. Workspace-wide attention counts and status-filter projections are asynchronous; use their `freshness` object when reconciling an immediately following list response.\n"
        return self._transport.request(
            "watchIntegrationTransaction", "PUT", "/v1/integration/transactions/{messageId}/{transactionKey}/watch",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionWatchResponse, raw=False, options=options)

class AccountApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def get_integration_usage(self, *, x_request_id: str | None = None, days: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.UsageResponse]:
        "Get plan usage and enforcement status\n\n**Required key scope:** `transactions:read`.\nReturns the tenant's current AS2 message usage, plan thresholds, daily history, and operational signals. Use `rejectionActive`, `status`, and the threshold fields to warn operators before additional messages are rejected. The quota date and `timeZone` are reported in UTC and usage includes both inbound and outbound AS2 messages. Hour bucket labels use `HH:00` values such as `18:00`.\n"
        return self._transport.request(
            "getIntegrationUsage", "GET", "/v1/usage",
            path_params={},
            query={"days": days},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.UsageResponse, raw=False, options=options)

class IntegrationEventsApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def list_integration_change_events(self, *, x_request_id: str | None = None, environment: str | None = None, cursor: str | None = None, limit: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.IntegrationChangeEventsResponse]:
        "Poll transaction-state changes\n\n**Required key scope:** `transactions:read`.\n\nReturns a small invalidation feed for transaction state detected after an initial snapshot, including late mapping results, MDNs, 997 and 999 evaluations, mapped-output handoff changes, and attention changes. Events do not duplicate transaction detail. Refetch the referenced transaction to read authoritative current state.\n\nWhen `cursor` is omitted, ModernEDI returns no historical events, `bootstrap=true`, and a `nextCursor` positioned at the current high-water mark. A race-safe custom viewer should:\n\n1. Request this endpoint without a cursor and retain `nextCursor`.\n2. Load its current transaction snapshot from `/v1/integration/transactions`.\n3. Poll this endpoint again using the retained cursor.\n4. Refetch every transaction named by events that arrived while the snapshot loaded.\n\nThereafter, keep sending each `nextCursor` back unchanged. `observedAt` is when the reconciliation sweep detected the change, not necessarily the partner's event time; event order is detection order. The feed is eventually consistent, so inspect `freshness.complete` and `freshness.status` before treating an empty poll as proof that no changes are pending.\n\nChange events have a rolling 30-day retention independent of retained transaction documents. Polling successfully refreshes the cursor's age. A client that resumes with an expired cursor receives `410 cursor_expired`; request a new bootstrap cursor and repeat the snapshot sequence.\n"
        return self._transport.request(
            "listIntegrationChangeEvents", "GET", "/v1/integration/events",
            path_params={},
            query={"environment": environment, "cursor": cursor, "limit": limit},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.IntegrationChangeEventsResponse, raw=False, options=options)

class X12ToolsApi:
    def __init__(self, transport: Transport):
        self._transport = transport

    def list_x12_transaction_sets(self, *, x_request_id: str | None = None, x12_version: str, options: RequestOptions | None = None) -> ApiResponse[models.X12TransactionSetsResponse]:
        "List transaction sets for an X12 version\n\n**Required key scope:** `configuration:read`.\nReturns the transaction-set identifiers and descriptions available for the normalized X12 version. Both `4010` and `004010` style version values are accepted.\n"
        return self._transport.request(
            "listX12TransactionSets", "GET", "/v1/x12/versions/{x12Version}/transaction-sets",
            path_params={"x12Version": x12_version},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.X12TransactionSetsResponse, raw=False, options=options)

    def list_x12_versions(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.X12VersionsResponse]:
        "List available X12 versions\n\n**Required key scope:** `configuration:read`.\n\nReturns X12 versions for which the tenant has reference syntax trees.\n"
        return self._transport.request(
            "listX12Versions", "GET", "/v1/x12/versions",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.X12VersionsResponse, raw=False, options=options)

    def validate_x12(self, *, body: RequestBody, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.X12ValidationResponse]:
        "Parse and validate an X12 interchange\n\n**Required key scope:** `transactions:read`.\nParses an X12 interchange and returns structural, group, transaction, segment, and element validation results without sending anything. Send X12 directly as `application/edi-x12` or `text/plain`, or wrap it in an `x12` field when JSON is more convenient. A syntactically invalid X12 document still returns a 200 validation result; malformed request shapes return a standard 400 error. Request bodies are limited to 3 MiB. Validation is available to read-only viewers and does not grant authority to send X12.\n"
        return self._transport.request(
            "validateX12", "POST", "/v1/x12/validate",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.X12ValidationResponse, raw=False, options=options)

class ModernEdiClient(Transport):
    @property
    def mapped_outputs(self) -> MappedOutputQueueApi:
        return MappedOutputQueueApi(self)

    @property
    def scenario_runs(self) -> ScenarioRunsApi:
        return ScenarioRunsApi(self)

    @property
    def configuration_as_code(self) -> ConfigurationAsCodeApi:
        return ConfigurationAsCodeApi(self)

    @property
    def outbound_as2(self) -> OutboundAS2Api:
        return OutboundAS2Api(self)

    @property
    def as2_connections(self) -> AS2ConnectionsApi:
        return AS2ConnectionsApi(self)

    @property
    def partners(self) -> PartnersApi:
        return PartnersApi(self)

    @property
    def mappings(self) -> MappingsApi:
        return MappingsApi(self)

    @property
    def mapping_runtime(self) -> MappingRuntimeApi:
        return MappingRuntimeApi(self)

    @property
    def transactions(self) -> TransactionViewerApi:
        return TransactionViewerApi(self)

    @property
    def account(self) -> AccountApi:
        return AccountApi(self)

    @property
    def integration_events(self) -> IntegrationEventsApi:
        return IntegrationEventsApi(self)

    @property
    def x12(self) -> X12ToolsApi:
        return X12ToolsApi(self)

class AsyncMappedOutputQueueApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def acknowledge_mapped_output(self, *, body: models.MappedOutputAckRequest, x_request_id: str | None = None, id: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputAckResponse]:
        "Mark mapped output as received\n\n**Required key scope:** `messages:write`.\nRecords that your integration acknowledged custody of a previously returned mapped output message. Call this after the mapped output has been durably stored or enqueued for reliable processing in your system. This acknowledgment does not prove later ERP or business processing. The receipt handle must match the latest poll response for this mapped output id. A retry with the same id and receipt handle is idempotent: it returns the original acknowledgment and `ackedAt` value instead of failing. If a call ends without a definitive response, retry that same acknowledgment before polling. Poll for a new receipt only when the old lease is rejected or the message becomes available again; an acknowledged item is no longer returned by polling.\n"
        return await self._transport.request(
            "acknowledgeMappedOutput", "POST", "/v1/mapped-outputs/{id}/ack",
            path_params={"id": id},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.MappedOutputAckResponse, raw=False, options=options)

    async def acknowledge_mapped_outputs(self, *, body: models.MappedOutputBulkAckRequest, x_request_id: str | None = None, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputBulkAckResponse]:
        "Atomically acknowledge multiple mapped outputs\n\n**Required key scope:** `messages:write`.\nAcknowledges between 1 and 100 mapped-output receipts in one database transaction. If any id or receipt handle is invalid, none of the items are acknowledged. Repeating an already successful request with the same id and receipt handles is idempotent and returns the original acknowledgment timestamps. Retry the same batch first when a call ends without a definitive response; already acknowledged items are not returned by polling. All items must belong to the environment selected by the `environment` query parameter.\n"
        return await self._transport.request(
            "acknowledgeMappedOutputs", "POST", "/v1/mapped-outputs/ack",
            path_params={},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.MappedOutputBulkAckResponse, raw=False, options=options)

    async def get_mapped_output_webhook_status(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputWebhookStatusResponse]:
        "Get mapped-output webhook status\n\n**Required key scope:** `configuration:read`.\nReturns the current mapped-output webhook configuration and recent delivery health for a partner. This read-only endpoint never returns the signing secret; it reports whether a secret is configured and only its last four characters so operators can identify the active credential. Save the response `ETag` header or `webhook.etag` before updating.\n"
        return await self._transport.request(
            "getMappedOutputWebhookStatus", "GET", "/v1/partners/{partnerId}/mapped-output-webhook",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappedOutputWebhookStatusResponse, raw=False, options=options)

    async def poll_mapped_outputs(self, *, x_request_id: str | None = None, environment: str | None = None, start_date: str | None = None, end_date: str | None = None, cursor: str | None = None, limit: int | None = None, visibility_timeout_seconds: int | None = None, direction: str | None = None, partner_name: str | None = None, partner_id: int | None = None, transaction_set: str | None = None, business_key: str | None = None, message_id: str | None = None, reply_to_message_id: str | None = None, transaction_control_number: str | None = None, functional_group_control_number: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputQueueResponse]:
        "Poll mapped inbound output\n\n**Required key scope:** `transactions:read`.\nReturns server-managed mapped inbound documents for this tenant and temporarily marks them in progress. Transaction-record-only results and legacy direct-to-SQS or direct-to-DynamoDB outputs are not duplicated into this queue. If a returned message is not acknowledged before the visibility timeout expires, ModernEDI may return it again on a later poll. Push delivery uses the same queue state: a successful 2xx webhook response acknowledges the message, while a failed push leaves it available through this endpoint. Each request performs a bounded scan. When `hasMore` is true, send `nextCursor` as the next request's `cursor` so polling advances past unavailable or output-free transactions instead of rescanning them. A cursor may repeat while new leases advance through outputs in the same scan window; an empty page with `nextCursor` is not the end of the scan. Use the SDK's bounded mapped-output iterator, not ordinary list pagination. Despite using GET, a poll acquires leases and the SDKs do not automatically retry it. If a response is lost, its outputs become available again after the visibility timeout. This endpoint runs on the shared ModernEDI API host, not on the tenant AS2 hostname.\n"
        return await self._transport.request(
            "pollMappedOutputs", "GET", "/v1/mapped-outputs",
            path_params={},
            query={"environment": environment, "startDate": start_date, "endDate": end_date, "cursor": cursor, "limit": limit, "visibilityTimeoutSeconds": visibility_timeout_seconds, "direction": direction, "partnerName": partner_name, "partnerId": partner_id, "transactionSet": transaction_set, "businessKey": business_key, "messageId": message_id, "replyToMessageId": reply_to_message_id, "transactionControlNumber": transaction_control_number, "functionalGroupControlNumber": functional_group_control_number},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappedOutputQueueResponse, raw=False, options=options)

    async def test_mapped_output_webhook(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputWebhookTestResponse]:
        "Send a synthetic mapped-output webhook test\n\n**Required key scope:** `configuration:write`.\n\nSends one signed `mapped_output.test` event to the partner's saved HTTPS webhook endpoint using the same DNS validation, pinned public-address transport, timeout, and HMAC signing path as normal mapped-output delivery. The test event is explicitly marked `test: true`, contains no mapped-output `message`, queue id, receipt handle, or business document, and never creates, leases, acknowledges, retries, or changes a real mapped-output queue item. It also does not replace the webhook's recorded production delivery health.\n\nThe webhook may be disabled while this connectivity test runs, but an endpoint and signing secret must already be saved. The API returns `200` after every completed attempt; inspect `delivered`, `statusCode`, and `error` for the destination outcome. `requestId` matches the `X-Request-Id` response header and is also included in the signed synthetic event for correlation.\n"
        return await self._transport.request(
            "testMappedOutputWebhook", "POST", "/v1/partners/{partnerId}/mapped-output-webhook/test",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappedOutputWebhookTestResponse, raw=False, options=options)

    async def update_mapped_output_webhook(self, *, body: models.MappedOutputWebhookUpdateRequest, x_request_id: str | None = None, partner_id: int, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.MappedOutputWebhookUpdateResponse]:
        "Configure mapped-output webhook delivery\n\n**Required key scope:** `configuration:write`.\n\nEnables, disables, or rotates a partner's HTTPS mapped-output webhook. Send the current configuration ETag in `If-Match`. `endpointUrl` is required when enabling delivery and must be an absolute HTTPS URL without user information or a fragment and use a publicly routable host. Localhost, private, link-local, multicast, carrier-grade NAT, documentation, benchmark, and other reserved address targets are rejected. ModernEDI resolves the hostname again before every webhook delivery and sends only when all resolved addresses are publicly routable. Enabling a webhook without an existing signing secret creates one; `rotateSigningSecret: true` replaces it.\n\nThe request body is strict JSON: unknown fields are rejected; `enabled` and `rotateSigningSecret` must be booleans; and `endpointUrl` must be a string or `null`. Type mismatches return `400 invalid_request` with the offending JSON pointer.\n\nA newly created or rotated `plainTextSigningSecret` appears only in this successful response. Save it immediately. Later reads expose only `signingSecretConfigured` and `signingSecretLastFour`.\n"
        return await self._transport.request(
            "updateMappedOutputWebhook", "PUT", "/v1/partners/{partnerId}/mapped-output-webhook",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id, "If-Match": if_match},
            body=body, response_type=models.MappedOutputWebhookUpdateResponse, raw=False, options=options)

class AsyncScenarioRunsApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def advance_scenario_run(self, *, body: dict[str, Any], run_id: str, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Advance adapter work or reevaluate graph deadlines\n\nAdvances server-controlled adapter work or refreshes/re-evaluates the existing graph, using the same runtime as the browser. Every fresh external dispatch, including ModernEDI test-partner-originated traffic, additionally requires messages:write on the authenticated key. The same key is reused automatically; no second credential is accepted in the body. Reconciliation and observation-only evaluation need no send scope. retry.requiresApiKey describes the browser's supplemental credential, not API authorization: false never exempts a dispatch from messages:write. A lost-response retry must reuse the original Idempotency-Key and If-Match. An already-recorded failed operation is replayed without another dispatch; to attempt a retryable failed action again, fetch the current ETag and use a fresh key. Follow structured guidance rather than hard-coding bundled step names."
        return await self._transport.request(
            "advanceScenarioRun", "POST", "/v1/scenario-runs/{runId}/advance",
            path_params={"runId": run_id},
            query={},
            headers={"Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

    async def attach_scenario_run_observation(self, *, body: models.ScenarioRunObservationRequest, run_id: str, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Attach or refresh a persisted transaction observation\n\nAttaches one exact workspace-visible ModernEDI transaction to an attachable runtime-mapping or observation-only occurrence. The body identifies persisted transaction metadata; raw X12 is never accepted. The transaction must carry the exact partner-configuration fingerprint frozen into the applied binding; legacy or mismatched transactions are ineligible, while acknowledgments and receipts produced under a different configuration remain pending. Repeating the same slot and transaction with the current ETag and a new Idempotency-Key re-reads trusted transaction detail, refreshes pending mapping or acknowledgment evidence, and reevaluates the graph atomically. Reusing the original key is a pure replay and does not refresh evidence. Adapter-controlled steps reject client attachment. Mapper-derived facts use ordinary X12 Mapper semantics, with dynamic durability limits enforced before SQL persistence: collections contain at most 1000 scalar values; text scalars contain at most 4096 UTF-8 bytes; one canonical typed value contains at most 32768 bytes; and one observation's facts JSON contains at most 262144 bytes. A fact provenance receipt contains at most 4096 bytes. Each evidence document contains at most 8192 bytes, with at most 8 non-fact evidence documents and 524288 bytes of aggregate evidence JSON per observation. Capacity failures use fact_value_limit_exceeded, transaction_observation_capacity_exceeded, transaction_fact_evidence_capacity_exceeded, or transaction_evidence_capacity_exceeded. fact_evaluation_timeout and fact_evaluation_busy_or_limited return HTTP 409 with retryable=true and operationStatus=failed; reload the run if needed, then retry with its current ETag and a fresh Idempotency-Key to re-read trusted transaction evidence."
        return await self._transport.request(
            "attachScenarioRunObservation", "POST", "/v1/scenario-runs/{runId}/observations",
            path_params={"runId": run_id},
            query={},
            headers={"Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

    async def cancel_scenario_run(self, *, body: dict[str, Any], run_id: str, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Cancel an active scenario run\n\nRecords an actor-attributed operator cancellation as an inconclusive terminal result while preserving all evidence already gathered. Cancellation is optimistic-concurrency controlled and idempotent, and it does not interrupt a command that still owns the run. If a command stops without saving a result and its temporary ownership period expires, ModernEDI records that attempt as failed and claims cancellation as one durable change. If the abandoned command may already have affected an external system, its failed timeline entry remains available for manual reconciliation. Each run can store at most 256 command records. The initial start and all later ordinary commands share 253 records; the remaining three are held for one retry record, cancellation, and a retry of cancellation. Result documents for ordinary commands share a 32 MiB budget, with additional space held for those same three reserved records."
        return await self._transport.request(
            "cancelScenarioRun", "POST", "/v1/scenario-runs/{runId}/cancel",
            path_params={"runId": run_id},
            query={},
            headers={"Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

    async def download_scenario_evidence_report(self, *, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioEvidenceReport]:
        "Download the immutable evidence report for a terminal run\n\nCreates the report once from terminal durable state and thereafter returns the exact persisted canonical JSON. It records the frozen authority and redacted evidence needed to substantiate the bounded implementation-verification claim; it is not editable scenario source, raw X12, or a compliance certificate. Stable failure codes are included, while detailed failure messages remain in the run timeline so the credential-free proof stays within its fixed export bound. If a retry creates another audit record for the same successful state change, the report counts that change once and keeps its earliest record; the timeline still shows every attempt."
        return await self._transport.request(
            "downloadScenarioEvidenceReport", "GET", "/v1/scenario-runs/{runId}/evidence-report",
            path_params={"runId": run_id},
            query={},
            headers={},
            body=None, response_type=models.ScenarioEvidenceReport, raw=False, options=options)

    async def get_scenario_run(self, *, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunViewResponse]:
        "Read current scenario run state and evidence\n\nReturns the current durable revision, evidence-bearing observations, checks, outcome, and strong ETag. Sensitive fact values are redacted from the public representation."
        return await self._transport.request(
            "getScenarioRun", "GET", "/v1/scenario-runs/{runId}",
            path_params={"runId": run_id},
            query={},
            headers={},
            body=None, response_type=models.ScenarioRunViewResponse, raw=False, options=options)

    async def get_scenario_run_timeline(self, *, run_id: str, limit: int | None = None, cursor: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunTimelineResponse]:
        "Read the actor-attributed operation timeline for a run\n\nReturns a bounded, newest-first audit timeline without idempotency hashes, attempt tokens, transient credentials, or operation result payloads. The cursor is opaque and bound to both the workspace and run."
        return await self._transport.request(
            "getScenarioRunTimeline", "GET", "/v1/scenario-runs/{runId}/timeline",
            path_params={"runId": run_id},
            query={"limit": limit, "cursor": cursor},
            headers={},
            body=None, response_type=models.ScenarioRunTimelineResponse, raw=False, options=options)

    async def list_scenario_runs(self, *, limit: int | None = None, cursor: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCollection]:
        "List recent scenario conversations\n\nReturns a bounded workspace-scoped summary of recent runs for discovery and navigation without exposing fact values or evidence payloads."
        return await self._transport.request(
            "listScenarioRuns", "GET", "/v1/scenario-runs",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            headers={},
            body=None, response_type=models.ScenarioRunCollection, raw=False, options=options)

    async def start_scenario_run(self, *, body: models.StartScenarioRunRequest, idempotency_key: str, options: RequestOptions | None = None) -> ApiResponse[models.ScenarioRunCommandResponse]:
        "Start a run from an exact applied binding\n\nStarts a durable run from exact definition and binding hashes in the binding's production or test traffic environment. Both environments share deployed mappings, but transactions, dispatch, acknowledgments, and evidence remain in the selected environment. Optional typed parameters are checked against the definition before any operation is accepted. Registered adapter targets prepare their selected-profile runtime dependencies before the run is inserted; temporary preparation failures are retryable and return Retry-After. Does not send EDI. It uses an already applied binding and never publishes authored definitions or applies desired configuration. The reserved browser-managed binding cannot be selected here; apply your own binding (including one using a managed example). The key is scoped to operations in this workspace, not restricted to Test traffic."
        return await self._transport.request(
            "startScenarioRun", "POST", "/v1/scenario-runs",
            path_params={},
            query={},
            headers={"Idempotency-Key": idempotency_key},
            body=body, response_type=models.ScenarioRunCommandResponse, raw=False, options=options)

class AsyncConfigurationAsCodeApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def apply_integration_configuration(self, *, body: models.ConfigurationApplyRequest, x_request_id: str | None = None, idempotency_key: str, if_match: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationApplyOperationResponse]:
        "Apply a planned workspace configuration\n\n**Required key scope:** `configuration:write`.\n\nAtomically applies the exact desired bundle represented by a successful `POST /v1/configuration/plan` response. Send that response's non-null `planSha256` in the body and its exact quoted `currentSnapshotEtag` in `If-Match`. The body accepts the same `files` array as planning, including the optional exported `_state/snapshot.json` advisory file. The advisory file remains untrusted and never overrides live workspace state.\n\nModernEDI revalidates the package, current snapshot, active syntax-tree catalog, complete scenario impact, and planned operations while holding workspace configuration locks. Any drift fails closed; apply never silently substitutes a newer plan. Database mutations commit as one aggregate change, mapping updates retain immutable revision history, creates use the caller-supplied stable resource keys, and a desired Partner whose key was retired is restored under that same key. Public operations remain `CREATE`, `UPDATE`, and `DELETE`; there is no separate reactivation verb.\n\n`Idempotency-Key` is required and scoped to the authenticated API key within the workspace. Persist one stable key with the intended change and reuse it only with the identical `planSha256`, `If-Match`, and logical files. A replay through that same API key returns the same operation and sets `Idempotency-Replayed: true`; using the key for a different semantic request returns `409 idempotency_key_conflict`, with the original operation's ID in `error.details.operationId`. A different API key has a separate idempotency namespace, even for the same workspace.\n\nLocked revalidation failures return the complete freshly evaluated `ConfigurationPlanResponse` under `error.details.plan`. A `412 configuration_plan_stale` means the submitted snapshot or plan identity is no longer current. A `422 configuration_apply_not_applicable` means the refreshed plan has semantic blockers. Neither response mutates workspace configuration; resolve the refreshed diagnostics and call the planning endpoint again before another apply.\n\nA `200` response has `operation.status: SUCCEEDED`. A `202` response has `operation.status: PENDING`: the database transaction has already committed, but the one workspace runtime publication is still being retried. Do not submit a new apply. Poll the URL in `Location` or call `GET /v1/configuration/apply-operations/{operationId}` until the stored operation is `SUCCEEDED`. Request bodies may be at most 16 MiB (16,777,216 bytes).\n"
        return await self._transport.request(
            "applyIntegrationConfiguration", "POST", "/v1/configuration/apply",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key, "If-Match": if_match},
            body=body, response_type=models.ConfigurationApplyOperationResponse, raw=False, options=options)

    async def cancel_integration_configuration_verification(self, *, x_request_id: str | None = None, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationVerificationResponse]:
        "Cancel configuration verification\n\n**Required key scope:** `configuration:read`.\n\nOnly the API key that started the run can cancel it. Cancellation is persistent and prevents subsequent cases; the current bounded case may finish. Terminal results are unchanged."
        return await self._transport.request(
            "cancelIntegrationConfigurationVerification", "POST", "/v1/configuration/verification-runs/{runId}/cancel",
            path_params={"runId": run_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationVerificationResponse, raw=False, options=options)

    async def export_integration_configuration(self, *, x_request_id: str | None = None, if_none_match: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationExportResponse]:
        "Export the current workspace configuration bundle\n\n**Required key scope:** `configuration:read`.\n\nReturns the workspace's current AS2 connections, active partners, published mappings, and optional scenario definitions and bindings as a deterministic logical file bundle. The response is JSON; ModernEDI does not create a ZIP archive, temporary download, or server-side filesystem tree. A caller may materialize the returned paths locally. Commit the portable `MANIFEST`, `RESOURCE`, and `SOURCE` files when using source control; `_state/snapshot.json` is observed server state and is normally kept outside desired configuration.\n\nScenario documents use `spec.source` for their complete authored JSON. Bindings refer to the bundle's stable `partnerKey` and `mappingKey` UUIDs, never another workspace's numeric IDs. Optional syntax-tree pins remain optional. Retired scenario configuration, immutable runtime revisions and run evidence are excluded. See the [scenario configuration guide](https://www.modernedi.com/docs/scenarios/reference#configuration-and-git) and the linked resource schemas for examples and lifecycle rules.\n\nEvery file carries a SHA-256 digest over its logical bytes. JSON file hashes use UTF-8 canonical JSON with object keys sorted recursively and array order preserved. Text file hashes use the exact stored UTF-8 source text, including its line endings. Files are sorted lexicographically by `path`.\n\n`modernedi.json` is the desired-state manifest and its digest is `bundleSha256`. `_state/snapshot.json` records the current database ids and public API ETags that correspond to the portable resource keys; its digest is `snapshotSha256`. `snapshotEtag` is the quoted snapshot digest returned in the HTTP `ETag` header. The manifest, resource documents, and snapshot state use `apiVersion: modernedi.com/v1`.\n\nServer-managed secrets are excluded. Public partner certificates and mapping source are configuration and are included. Treat the result as sensitive workspace configuration, keep the API key on a trusted server, and review customer-authored map source before sharing it.\n"
        return await self._transport.request(
            "exportIntegrationConfiguration", "GET", "/v1/configuration/export",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id, "If-None-Match": if_none_match},
            body=None, response_type=models.ConfigurationExportResponse, raw=False, options=options)

    async def get_configuration_scenario_run_selection(self, *, x_request_id: str | None = None, operation_id: str, binding_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationScenarioRunSelectionResponse]:
        "Select a scenario run from an exact configuration apply\n\n**Required key scope:** `configuration:read`.\n\nAfter an aggregate apply reaches `SUCCEEDED`, resolve the authored binding ID from `ScenarioBinding` source `metadata.id` into the exact `selection` accepted by `POST /v1/scenario-runs`. The response contains frozen runtime hashes, not source-file hashes. No browser visit, configuration mutation, run creation, or EDI dispatch occurs. Unchanged bindings are selectable after a no-op apply too.\n\nThe complete current configuration snapshot must still equal this operation's `appliedSnapshotEtag`. A pending apply returns `409 configuration_apply_pending` with `Retry-After`; a different snapshot returns non-retryable `409 configuration_snapshot_changed`. A binding whose referenced runtime inputs are no longer current returns `409 scenario_binding_not_current`. Never silently substitute a later apply or recalculate hashes. Missing, retired, or reserved browser-managed bindings have no public selection.\n\nThis is a point-in-time selection, not a workspace lock, a run, or a guarantee of runtime readiness. Run admission rechecks the selected binding and its referenced inputs. Unrelated configuration changes after discovery do not automatically invalidate a run start. Supply any required definition parameters, and persist the final start body and a new run idempotency key before starting. Starting requires `scenario-runs:write`; run reads and actual sends have separate scopes.\n"
        return await self._transport.request(
            "getConfigurationScenarioRunSelection", "GET", "/v1/configuration/apply-operations/{operationId}/scenario-run-selections/{bindingId}",
            path_params={"operationId": operation_id, "bindingId": binding_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationScenarioRunSelectionResponse, raw=False, options=options)

    async def get_integration_configuration_applied_verification(self, *, x_request_id: str | None = None, operation_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationAppliedVerificationResponse]:
        "Read verification linked to an apply\n\n**Required key scope:** `configuration:read`.\n\nReturns the server run explicitly selected by verificationRunId during apply, or null when none is retained. Ordinary applies do not require verification."
        return await self._transport.request(
            "getIntegrationConfigurationAppliedVerification", "GET", "/v1/configuration/apply-operations/{operationId}/verification",
            path_params={"operationId": operation_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationAppliedVerificationResponse, raw=False, options=options)

    async def get_integration_configuration_apply_operation(self, *, x_request_id: str | None = None, operation_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationApplyOperationResponse]:
        "Get a configuration apply operation\n\n**Required key scope:** `configuration:read`.\n\nReturns the workspace-scoped immutable result of one aggregate apply. Operation ids use `apply-` followed by a canonical UUID. `PENDING` means the database change already committed and only runtime publication remains; `SUCCEEDED` is terminal. Poll only when a prior POST returned `202`, honoring its `Retry-After` value.\n"
        return await self._transport.request(
            "getIntegrationConfigurationApplyOperation", "GET", "/v1/configuration/apply-operations/{operationId}",
            path_params={"operationId": operation_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationApplyOperationResponse, raw=False, options=options)

    async def get_integration_configuration_context(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationContextResponse]:
        "Identify the calling workspace and API key\n\n**Required key scope:** `configuration:read`.\n\nConfirms the workspace ID, calling key ID, label, and currently granted scopes using the same authentication as every configuration operation. Automation can compare these IDs with its approved target before proceeding. The workspace is derived from the key, not a request parameter. This does not enumerate users, other workspaces, or other keys, and never returns the key value, prefix, hash, or credentials. It is not an authorization lease; every subsequent request is independently authorized.\n"
        return await self._transport.request(
            "getIntegrationConfigurationContext", "GET", "/v1/configuration/context",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationContextResponse, raw=False, options=options)

    async def get_integration_configuration_external_repository(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationExternalRepositoryResponse]:
        "Read external repository synchronization status\n\n**Required key scope:** `configuration:read`.\n\nReturns the connection already configured by a workspace owner, its automatic synchronization status, last synchronized commits, and optional import-test reference. `connected: false` is normal when Git is not configured. This is a database status read, not a remote Git fetch or synchronization trigger. The commit fields describe the last successful synchronization; they are not an attestation of the current remote branch HEAD. Connecting, disconnecting, changing import-test policy, retrying, and resolving conflicts remain owner actions in the browser. Provider tokens, usernames, secret-store references, and internal lease state are excluded.\n"
        return await self._transport.request(
            "getIntegrationConfigurationExternalRepository", "GET", "/v1/configuration/external-repository",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationExternalRepositoryResponse, raw=False, options=options)

    async def get_integration_configuration_import_verification(self, *, x_request_id: str | None = None, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationImportVerificationResponse]:
        "Read the current external import's saved-case evidence\n\n**Required key scope:** `configuration:read`.\n\nUse the `importVerification.runId` from the connection status. Returns the existing server-owned verification result for that connection's current import attempt. A `200` with `run: null` means the attempt was reserved but no retained result is available (for example, admission did not succeed or evidence expired); it never means a pass. A different attempt, disconnected repository, unknown ID, or another workspace's ID returns `404 verification_not_found`. Re-read connection status if the attempt changes. This endpoint does not run cases, retry an import, apply configuration, or send EDI. Previously retained results can still be read using the ordinary verification-run endpoint.\n"
        return await self._transport.request(
            "getIntegrationConfigurationImportVerification", "GET", "/v1/configuration/external-repository/verification/{runId}",
            path_params={"runId": run_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationImportVerificationResponse, raw=False, options=options)

    async def get_integration_configuration_verification(self, *, x_request_id: str | None = None, run_id: str, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationVerificationResponse]:
        "Read configuration verification\n\n**Required key scope:** `configuration:read`.\n\nReturns persisted outcomes and freshly checked configuration, evaluator and catalog identity. Any read-capable key in the same workspace can read a run."
        return await self._transport.request(
            "getIntegrationConfigurationVerification", "GET", "/v1/configuration/verification-runs/{runId}",
            path_params={"runId": run_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationVerificationResponse, raw=False, options=options)

    async def list_integration_configuration_apply_operations(self, *, x_request_id: str | None = None, limit: int | None = None, cursor: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationApplyOperationHistoryResponse]:
        "List workspace configuration changes\n\n**Required key scope:** `configuration:read`.\n\nLists the same workspace-wide change history shown in the browser, including browser, API, and automatic Git imports. Newest requests come first, with operation ID breaking timestamp ties. Entries are compact summaries; fetch the existing operation endpoint for its full change list. Pass `nextCursor` unchanged to retrieve the next page and stop when it is null. Cursors belong to one workspace. Pagination is not a frozen snapshot: new changes can arrive during a scan, so re-read the first page when checking for drift. This endpoint does not advance pending publications or mutate configuration.\n"
        return await self._transport.request(
            "listIntegrationConfigurationApplyOperations", "GET", "/v1/configuration/apply-operations",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.ConfigurationApplyOperationHistoryResponse, raw=False, options=options)

    async def plan_integration_configuration(self, *, body: models.ConfigurationPlanRequest, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationPlanResponse]:
        "Plan desired workspace configuration\n\n**Required key scope:** `configuration:read`.\n\nCompares a portable desired configuration bundle with the workspace's current AS2 connections, active partners, published mappings, and optional scenario definitions and bindings. Planning is read-only: it does not create, update, retire, publish, or reapply anything, and it does not require an idempotency key.\n\nSubmit exactly one `MANIFEST` at `modernedi.json` plus every `RESOURCE` and `SOURCE` file inventoried by that manifest. You may pass the `files` array from configuration export unchanged: its single `_state/snapshot.json` `STATE` file is accepted as advisory context, but current workspace configuration remains authoritative. A stale advisory snapshot adds the `BASE_SNAPSHOT_STALE` warning; it does not make old database ids or ETags desired state. ModernEDI verifies safe paths, closed JSON objects, canonical file hashes, manifest inventory, stable resource keys, cross-resource references, mapping source, aggregate runtime limits, and the active syntax-tree catalog before comparing desired and current state.\n\nA structurally valid bundle always receives `200`, even when the desired state cannot be applied. Inspect `applicable` and every entry in `diagnostics`; each diagnostic carries an RFC 6901 JSON Pointer into the submitted request. `operations` contains only `CREATE`, `UPDATE`, and `DELETE` entries. `summary.unchanged` reports resources omitted from that array because their complete portable configuration is already current.\n\nScenario bindings are compiled against the complete proposed configuration, so one apply can create their partners and maps too. Changing a referenced resource adds a binding `UPDATE` with unchanged authored content hashes: this creates a fresh runtime revision in the same transaction. `refreshScenarioBindings` explicitly requests that behavior for otherwise unchanged binding resource keys; include the same array in the apply request. Export followed by plan without refresh requests is a no-op.\n\n`scenarioImpactComplete` is false when ModernEDI could not safely determine every affected applied scenario. `affectedScenarios` distinguishes bindings refreshed by this apply (`REAPPLIED_BY_APPLY`), retired by it (`RETIRED_BY_APPLY`), or requiring a separate reapplication (`REAPPLY_REQUIRED`). `affectedRuns` identifies ACTIVE runs pinned to impacted binding revisions; those runs must be cancelled or completed before re-planning. `planSha256` is present only when the plan is applicable and binds the desired bundle, current snapshot, validation context, operations, and scenario impact. A later apply request must still prove that exact plan is current; this endpoint grants no mutation authority.\n\nCommon planning diagnostics have deliberate recovery paths:\n\n- `BASE_SNAPSHOT_STALE` is a warning that the optional exported snapshot no longer matches the workspace. The returned plan still uses live current state.\n- `STAGED_CHANGE_REQUIRED` is an error when a natural identity such as an AS2 identifier or X12 sender identity belongs to another stable resource key. Release it from the current owner in a separate apply, export again, and then plan the transfer.\n- `ACTIVE_SCENARIO_RUNS_AFFECTED` is an error when a change would alter authority used by an ACTIVE scenario run. Complete or cancel every listed `affectedRuns` entry and plan again.\n\nMalformed envelopes, unsafe or duplicate paths, unsupported file roles, a noncanonical advisory `STATE` file, hash mismatches, and inconsistent manifests return `400 configuration_plan_invalid` with the same diagnostic shape in `error.details.diagnostics`. Request bodies may be at most 16 MiB (16,777,216 bytes).\n"
        return await self._transport.request(
            "planIntegrationConfiguration", "POST", "/v1/configuration/plan",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.ConfigurationPlanResponse, raw=False, options=options)

    async def verify_integration_configuration(self, *, body: models.ConfigurationVerificationRequest, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.ConfigurationVerificationResponse]:
        "Verify saved cases in an exact configuration plan\n\n**Required key scope:** `configuration:read`.\n\nOptional and side-effect-free: re-plans the submitted bundle and verifies all saved mapping cases on the server. Supports up to 25 tested mappings and 100 cases in a 30-second suite. Uses the same incoming/JSLT/XSLT engines as Mapper reviews. Mappings without cases are counted explicitly. No raw input/output is retained. One active verification and 30 starts per workspace per hour are shared with browser reviews. Same requestId and identical content replay the persisted run. This endpoint never applies configuration or executes AS2/scenarios. A network interruption does not imply cancellation; GET the deterministic verify-{requestId} run before retrying."
        return await self._transport.request(
            "verifyIntegrationConfiguration", "POST", "/v1/configuration/verification-runs",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.ConfigurationVerificationResponse, raw=False, options=options)

class AsyncOutboundAS2Api:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def carbon_copy_generated_x12(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, original_message_id: str, original_transaction_key: str | None = None, copy_to_partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send already-generated X12 to a carbon-copy partner\n\n**Required key scope:** `messages:write`.\nSends supplied X12 to a second partner while preserving the original transaction context. ModernEDI validates the X12 but does not apply an outgoing map. Select the original partner with `partnerId` and the recipient with `copyToPartnerId`. Use `originalTransactionKey` when the original AS2 message contains more than one transaction set.\n"
        return await self._transport.request(
            "carbonCopyGeneratedX12", "POST", "/v1/as2/x12/carbonCopy",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key, "copyToPartnerId": copy_to_partner_id},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    async def preview_outbound_x12(self, *, body: RequestBody, x_request_id: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, options: RequestOptions | None = None) -> ApiResponse[models.OutboundPreviewResponse]:
        "Transform and validate an outbound document without sending it\n\n**Required key scope:** `messages:write`.\nUses the same partner, X12 metadata, content type, source body, params, and business-key contract as `/v1/as2/send`, but stops after mapping and X12 validation. It returns generated X12, validation details, mapping provenance, the resolved partner, and the optional business key. It does not contact the trading partner, create an outbound transaction, or require the partner's AS2 endpoint to be configured. Use it to validate a production-shaped request before the first live send.\n"
        return await self._transport.request(
            "previewOutboundX12", "POST", "/v1/as2/preview",
            path_params={},
            query={"partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.OutboundPreviewResponse, raw=False, options=options)

    async def reply_to_inbound_as2_message(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int | None = None, x12_version: str | None = None, functional_group_type: str | None = None, transaction_group_type: int | None = None, original_message_id: str, original_transaction_key: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send a follow-up document tied to an inbound message\n\n**Required key scope:** `messages:write`.\nSends a follow-up document such as an ASN or invoice in response to a previously received inbound message. Send the source XML, JSON, or text input as the HTTP request body. ModernEDI looks up the original message by `originalMessageId`, and uses unambiguous metadata from that inbound transaction to recover an omitted partner selector and `x12Version`. When the inbound AS2 message contains more than one transaction set, send `originalTransactionKey` to bind the reply to the exact `GS06#ST02` transaction. ModernEDI validates that composite reference before transforming or sending; an unknown or non-inbound reference returns `404`. When it is omitted, ModernEDI resolves and persists the key only if the message contains exactly one inbound transaction; an ambiguous multi-transaction message returns `400`. This lookup uses production transaction history by default; send `test=true` to infer from and link to isolated test history. ModernEDI uses the persisted `partnerId`, so the reply still selects the same partner after its configured name changes. Transactions without a persisted partner id do not supply inferred partner metadata. An explicit `partnerId` always overrides inferred partner metadata. After the partner id, X12 version, and request `Content-Type` are known, ModernEDI can also fill omitted `functionalGroupType` and `transactionGroupType` when those selectors match exactly one outgoing reply map. ModernEDI then selects the matching outgoing map by partner, X12 version, functional group, transaction set, and request `Content-Type`, generates and validates X12, then sends the reply through the configured AS2 connection. Send `x12Version` explicitly when a partner requires reply documents on a different X12 version than the one they send; explicit query parameters override inferred metadata. If multiple reply maps could match, send `functionalGroupType` and `transactionGroupType` explicitly. The original inbound document type is not reused as the reply type; these fields identify the generated reply document, such as `IN`/`810` for an invoice. JSON source maps can use XSLT with Saxon `json-to-xml($json)` or JSLT. For JSLT, ModernEDI sets the current input `.` to a wrapper object, so the source document is read through `.input` paths. If the outgoing map needs extra runtime parameters, send the JSON envelope shape with `input`, `contentType`, and `params`; XSLT maps receive those values as top-level stylesheet parameters, JSLT maps read them from `.params`, and mapper-editor params files are not used as live defaults. Use the envelope's optional `businessKey` field when the reply has a stable identifier, such as an invoice number, that should be stored on the outbound transaction record.\n"
        return await self._transport.request(
            "replyToInboundAs2Message", "POST", "/v1/as2/reply",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    async def reply_with_generated_x12(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int | None = None, x12_version: str | None = None, functional_group_type: str, transaction_group_type: int, original_message_id: str, original_transaction_key: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Reply to an inbound message with already-generated X12\n\n**Required key scope:** `messages:write`.\nSends X12 that your system generated as a reply tied to an inbound AS2 message. ModernEDI does not apply an outgoing map. When the partner or X12 version is omitted, `originalMessageId` can recover it from the selected transaction history. Use `originalTransactionKey` to bind a reply to one exact transaction in a multi-ST message; the composite reference is validated before delivery. Production history is the default; send `test=true` to infer from and link to isolated test history. The functional group and transaction-set identifiers describe the reply document and remain required because they are not copied from the original inbound document.\n"
        return await self._transport.request(
            "replyWithGeneratedX12", "POST", "/v1/as2/x12/reply",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    async def send_as2_carbon_copy(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, original_message_id: str, original_transaction_key: str | None = None, copy_to_partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send a carbon copy of an inbound message flow to another partner\n\n**Required key scope:** `messages:write`.\nSends a generated X12 document to a second partner while preserving context from a previously received inbound message. Send the source XML, JSON, or text input as the HTTP request body. The `partnerId` query parameter identifies the source/original partner whose outgoing map should generate the X12, and `copyToPartnerId` identifies the destination partner for the copied AS2 envelope. ModernEDI selects the matching outgoing map for that original/source partner, generates and validates X12, then forwards the carbon copy through the configured AS2 connection. Example: to generate an 856 ASN for Retailer One and copy it to Broker One, send `partnerId=1` and `copyToPartnerId=2`; ModernEDI uses partner 1's outgoing 856 map. `copyToPartnerId` does not select the outgoing map. JSON source maps can use XSLT with Saxon `json-to-xml($json)` or JSLT. For JSLT, ModernEDI sets the current input `.` to a wrapper object, so the source document is read through `.input` paths. If the outgoing map needs extra runtime parameters, send the JSON envelope shape with `input`, `contentType`, and `params`; the map is still selected by `partnerId`, not by `copyToPartnerId`. XSLT maps receive params as top-level stylesheet parameters, JSLT maps read them from `.params`, and mapper-editor params files are test fixtures only and are not read by live carbon-copy calls. The envelope's optional `businessKey` is recorded on the copied outbound transaction, but it does not affect map selection. Send `originalTransactionKey` when the source message contains multiple transaction sets and this copy belongs to one exact transaction.\n"
        return await self._transport.request(
            "sendAs2CarbonCopy", "POST", "/v1/as2/carbonCopy",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type, "originalMessageId": original_message_id, "originalTransactionKey": original_transaction_key, "copyToPartnerId": copy_to_partner_id},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    async def send_as2_message(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send a standalone outbound document\n\n**Required key scope:** `messages:write`.\nSends a standalone outbound document to the configured trading partner. Send the source XML, JSON, or text input as the HTTP request body. ModernEDI looks up the matching outgoing map by partner, X12 version, functional group, transaction set, and request `Content-Type`, applies that map to generate X12, syntax-checks the generated X12, then sends it through the configured AS2 connection. JSON source maps can use XSLT with Saxon `json-to-xml($json)` or JSLT. For JSLT, ModernEDI sets the current input `.` to a wrapper object, so the source document is read through `.input` paths. Send `partnerId` to select the partner; use `GET /v1/partners` when your integration client needs to discover stable partner ids. If the outgoing map needs extra runtime parameters such as a bill-of-lading number, pallet list, or generated control number, send the JSON envelope shape with `input`, `contentType`, and `params`. The envelope can also include `businessKey` when your system knows a stable purchase order, shipment, BOL, or other business identifier that should appear on the outbound transaction record. XSLT maps receive those params as top-level stylesheet parameters; JSLT maps receive them under `.params`. Mapper-editor params files are test fixtures only; live API calls must provide required params in this request envelope.\n"
        return await self._transport.request(
            "sendAs2Message", "POST", "/v1/as2/send",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

    async def send_generated_x12_message(self, *, body: RequestBody, x_request_id: str | None = None, test: bool | None = None, idempotency_key: str | None = None, partner_id: int, x12_version: str, functional_group_type: str, transaction_group_type: int, options: RequestOptions | None = None) -> ApiResponse[models.SendSuccessResponse]:
        "Send an already-generated X12 document\n\n**Required key scope:** `messages:write`.\nSends X12 that your system generated without applying a ModernEDI outgoing map. ModernEDI parses and validates the supplied X12, builds the AS2 message, and delivers it through the selected partner connection. Supply the X12 directly with `Content-Type: application/edi-x12` (or `text/plain`), or use the JSON envelope when you also want to record a business key. The partner selector and X12 metadata remain explicit so ModernEDI can choose and audit the correct destination. Use `/v1/as2/send` instead when ModernEDI should map your business document into X12 first.\n"
        return await self._transport.request(
            "sendGeneratedX12Message", "POST", "/v1/as2/x12/send",
            path_params={},
            query={"test": test, "partnerId": partner_id, "x12Version": x12_version, "functionalGroupType": functional_group_type, "transactionGroupType": transaction_group_type},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.SendSuccessResponse, raw=False, options=options)

class AsyncAS2ConnectionsApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get_integration_as2_connection(self, *, x_request_id: str | None = None, connection_id: int, options: RequestOptions | None = None) -> ApiResponse[models.As2ConnectionResponse]:
        "Get a partner AS2 connection\n\n**Required key scope:** `configuration:read`.\n\nReturns one public AS2 connection configuration and the ETag that identifies this observed resource version. To change or remove the connection, use the aggregate export–plan–apply workflow.\n"
        return await self._transport.request(
            "getIntegrationAs2Connection", "GET", "/v1/as2/connections/{connectionId}",
            path_params={"connectionId": connection_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.As2ConnectionResponse, raw=False, options=options)

    async def list_integration_as2_connections(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.As2ConnectionListResponse]:
        "List partner AS2 connections\n\n**Required key scope:** `configuration:read`.\n\nReturns every partner AS2 connection in this tenant. Certificates are partner public X.509 certificates formatted as PEM. Private keys and secret locations are never returned.\n"
        return await self._transport.request(
            "listIntegrationAs2Connections", "GET", "/v1/as2/connections",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.As2ConnectionListResponse, raw=False, options=options)

class AsyncPartnersApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get_integration_as2_profile(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.As2ProfileResponse]:
        "Get the tenant's public AS2 profile\n\n**Required key scope:** `configuration:read`.\nReturns the safe connection sheet your trading partners need: production and test AS2 URLs and identifiers, X12 sender identities, static network addresses included in the current plan, and active or next public certificates. Private keys, secret ARNs, billing contacts, and internal infrastructure identifiers are never returned. Network capability status is `ready`, `pending`, or `not_included`.\n"
        return await self._transport.request(
            "getIntegrationAs2Profile", "GET", "/v1/as2/profile",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.As2ProfileResponse, raw=False, options=options)

    async def get_integration_partner(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.PartnerResponse]:
        "Get a trading partner\n\n**Required key scope:** `configuration:read`.\n\nReturns the complete active public partner configuration. Retired partners return `404`; their retained rows are used only for historical transaction authorization. The response never exposes internal header overrides or infrastructure settings. The `ETag` header and `partner.etag` identify this observed resource version. To change or retire the partner, export the workspace configuration, edit its portable partner resource, plan the aggregate change, and apply that exact plan.\n"
        return await self._transport.request(
            "getIntegrationPartner", "GET", "/v1/partners/{partnerId}",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.PartnerResponse, raw=False, options=options)

    async def get_integration_partner_capabilities(self, *, x_request_id: str | None = None, partner_id: int, options: RequestOptions | None = None) -> ApiResponse[models.PartnerCapabilitiesResponse]:
        "Inspect a partner's published mapping capabilities\n\n**Required key scope:** `configuration:read`.\nReturns the selected partner plus its published incoming and outgoing mapping capabilities. Use this before sending to discover the exact X12 version, functional group, transaction set, source content type, and transform type that are currently configured. `productionReady` and `testReady` report whether the corresponding AS2 destination endpoint is configured; a published mapping can exist before either endpoint is ready.\n"
        return await self._transport.request(
            "getIntegrationPartnerCapabilities", "GET", "/v1/partners/{partnerId}/capabilities",
            path_params={"partnerId": partner_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.PartnerCapabilitiesResponse, raw=False, options=options)

    async def list_integration_partners(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.PartnerListResponse]:
        "List configured trading partners\n\n**Required key scope:** `configuration:read`.\nReturns the tenant's active configured trading partners in workspace order. Retired partners are excluded. Use `partnerId` from this response as the `partnerId` query parameter on `/v1/as2/send`, `/v1/as2/reply`, or `/v1/as2/carbonCopy` when your integration selects the outbound partner. The returned `name` is display metadata; use `copyToPartnerId` for the carbon-copy recipient. Partners can appear before their AS2 profile is complete so teams can publish and test maps during onboarding; `as2ConnectionConfigured` tells you whether live AS2 delivery can use that partner yet.\n"
        return await self._transport.request(
            "listIntegrationPartners", "GET", "/v1/partners",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.PartnerListResponse, raw=False, options=options)

class AsyncMappingsApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get_integration_mapping(self, *, x_request_id: str | None = None, mapping_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappingResponse]:
        "Get a published mapping\n\n**Required key scope:** `configuration:read`.\n\nReturns one published map, its complete source text, safe output configuration, delivery category, and observed resource ETag. To change or retire the map, use the aggregate export–plan–apply workflow or the browser editor's reviewed deployment flow.\n"
        return await self._transport.request(
            "getIntegrationMapping", "GET", "/v1/mappings/{mappingId}",
            path_params={"mappingId": mapping_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingResponse, raw=False, options=options)

    async def get_integration_mapping_configuration_revision(self, *, x_request_id: str | None = None, mapping_id: int, revision_id: int, options: RequestOptions | None = None) -> ApiResponse[models.MappingConfigurationRevisionResponse]:
        "Get a historical mapping configuration revision\n\n**Required key scope:** `configuration:read`.\n\nReturns the identity, syntax-tree provenance, and complete stored configuration for one immutable historical mapping-configuration revision. The revision must belong to the tenant-scoped mapping in the path.\n"
        return await self._transport.request(
            "getIntegrationMappingConfigurationRevision", "GET", "/v1/mappings/{mappingId}/revisions/{revisionId}",
            path_params={"mappingId": mapping_id, "revisionId": revision_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingConfigurationRevisionResponse, raw=False, options=options)

    async def list_integration_mapping_configuration_revisions(self, *, x_request_id: str | None = None, mapping_id: int, cursor: str | None = None, limit: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingConfigurationRevisionListResponse]:
        "List a mapping's configuration history\n\n**Required key scope:** `configuration:read`.\n\nReturns one page of immutable mapping-configuration revisions, newest first. A configuration-only change creates a distinct revision even when its transform source is unchanged. Page entries intentionally omit source text; fetch one revision by id to preview or diff its transform. Follow `nextCursor` while `hasMore` is true. Cursors are opaque and must be sent back unchanged.\n\n`currentRevision` always contains the complete currently published transform source and exact configuration identity, even when that configuration's chronological entry is outside this page. It and `currentEtag` are read from the same locked configuration snapshot, so clients can use them as an authoritative diff baseline. If `currentEtag` changes between page requests, restart from the first page before presenting a coherent history view.\n\n`sourceHash` identifies only transform text. `configurationSha256` identifies the complete immutable mapping configuration and may be `null` for a legacy revision recorded before exact configuration identities. `current` compares the complete configuration identity. The API exposes the retained transform and configuration for inspection, diffing, and reviewed desired-configuration workflows.\n"
        return await self._transport.request(
            "listIntegrationMappingConfigurationRevisions", "GET", "/v1/mappings/{mappingId}/revisions",
            path_params={"mappingId": mapping_id},
            query={"cursor": cursor, "limit": limit},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingConfigurationRevisionListResponse, raw=False, options=options)

    async def list_integration_mappings(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingListResponse]:
        "List published mappings\n\n**Required key scope:** `configuration:read`.\n\nReturns the tenant's published incoming and outgoing maps, including the full transform source, delivery category, and each resource ETag. Infrastructure details are never exposed.\n"
        return await self._transport.request(
            "listIntegrationMappings", "GET", "/v1/mappings",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingListResponse, raw=False, options=options)

class AsyncMappingRuntimeApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get_integration_mapping_runtime_failure(self, *, x_request_id: str | None = None, failure_id: str, options: RequestOptions | None = None) -> ApiResponse[models.MappingRuntimeFailureResponse]:
        "Get one mapping runtime failure\n\n**Required key scope:** `transactions:read`.\nReturns one safe diagnostic by its opaque `failureId`. The id is still checked against the authenticated tenant; knowing another tenant's id never grants access.\n"
        return await self._transport.request(
            "getIntegrationMappingRuntimeFailure", "GET", "/v1/integration/mapping-runtime/failures/{failureId}",
            path_params={"failureId": failure_id},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingRuntimeFailureResponse, raw=False, options=options)

    async def get_integration_mapping_runtime_health(self, *, x_request_id: str | None = None, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingRuntimeHealthResponse]:
        "Get mapping runtime health\n\n**Required key scope:** `transactions:read`.\nReturns aggregate unresolved and recovered mapping outcomes for the selected environment. This view includes failures that occurred before an X12 transaction could be created, so its totals can be non-zero even when no corresponding transaction appears in the transaction list. `truncated=true` means the bounded health scan could not summarize every retained attempt; use the paginated failures endpoint for investigation.\n"
        return await self._transport.request(
            "getIntegrationMappingRuntimeHealth", "GET", "/v1/integration/mapping-runtime/health",
            path_params={},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingRuntimeHealthResponse, raw=False, options=options)

    async def list_integration_mapping_runtime_failures(self, *, x_request_id: str | None = None, environment: str | None = None, mapping_id: int | None = None, direction: str | None = None, resolved: bool | None = None, cursor: str | None = None, limit: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.MappingRuntimeFailuresResponse]:
        "List mapping runtime failures\n\n**Required key scope:** `transactions:read`.\nReturns safe, tenant-scoped mapping failure diagnostics in reverse chronological order. The response deliberately omits raw source input, generated output, stack traces, and internal exception text. A failure whose `transactionReference` is null occurred before a transaction existed. For those pre-transaction outbound failures, `correlationId` is a ModernEDI request-correlation identifier rather than an AS2 Message-Id, and `transactionKey` is `outbound-request`.\nUse `failureId` as the stable investigation and deduplication key. `resolved=true` means a later equivalent mapping attempt succeeded; it does not mean an AS2 document was sent, delivered, or acknowledged.\n"
        return await self._transport.request(
            "listIntegrationMappingRuntimeFailures", "GET", "/v1/integration/mapping-runtime/failures",
            path_params={},
            query={"environment": environment, "mappingId": mapping_id, "direction": direction, "resolved": resolved, "cursor": cursor, "limit": limit},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.MappingRuntimeFailuresResponse, raw=False, options=options)

class AsyncTransactionViewerApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get_integration_transaction(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionDetailResponse]:
        "Get transaction detail\n\n**Required key scope:** `transactions:read`.\nReturns a metadata-first transaction aggregate: the summary, mapped output provenance and managed handoff state, normalized acknowledgment status, a document index, timeline events, compact linked-reply summaries, and the complete mapping-attempt history used to explain `needsAttention`. Document bodies are returned only by the individual document endpoint.\n"
        return await self._transport.request(
            "getIntegrationTransaction", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionDetailResponse, raw=False, options=options)

    async def get_integration_transaction_document(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, document_id: str, options: RequestOptions | None = None) -> ApiResponse[models.TransactionDocumentResponse]:
        "Get one transaction document\n\n**Required key scope:** `transactions:read`.\nReturns one complete retained artifact selected by the stable transaction-local `documentId` from the document list. A document id is not a mapped-output queue id and cannot be used to acknowledge delivery. The returned body is untrusted external content and must be rendered as untrusted external content: escape text, sanitize any supported markup, and sandbox richer previews instead of inserting it directly into a page.\n"
        return await self._transport.request(
            "getIntegrationTransactionDocument", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/documents/{documentId}",
            path_params={"messageId": message_id, "transactionKey": transaction_key, "documentId": document_id},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionDocumentResponse, raw=False, options=options)

    async def get_integration_transaction_documents(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionDocumentsResponse]:
        "Get transaction documents\n\n**Required key scope:** `transactions:read`.\nReturns a lightweight metadata index for raw X12, mapped inbound outputs, MDN reports, acknowledgements, and HTTP responses recorded for the transaction. It never returns document bodies. Fetch one selected body from the individual document endpoint when an operator opens it.\n"
        return await self._transport.request(
            "getIntegrationTransactionDocuments", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/documents",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionDocumentsResponse, raw=False, options=options)

    async def get_integration_transaction_events(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionEventsResponse]:
        "Get transaction events\n\n**Required key scope:** `transactions:read`.\nReturns a normalized timeline for the transaction, including receipt or send events, mapping events, MDNs, acknowledgements, mapped-output availability/delivery/redelivery/attention/acknowledgment, and linked replies. These entries are derived from current persisted evidence; an output acknowledgment means acknowledged by your integration, not accepted by a downstream business system.\n"
        return await self._transport.request(
            "getIntegrationTransactionEvents", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/events",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionEventsResponse, raw=False, options=options)

    async def get_related_integration_transactions(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.RelatedTransactionsResponse]:
        "Get linked reply transactions\n\n**Required key scope:** `transactions:read`.\nReturns compact summaries of outbound reply transactions linked to an inbound transaction. Follow a summary's `messageId` and `transactionKey` to fetch its metadata-first detail or document index. Replies are included only when `replyToTransactionKey` identifies that exact transaction inside `replyToMessageId`. Use the returned linkage fields rather than inferring relationships from document type.\n"
        return await self._transport.request(
            "getRelatedIntegrationTransactions", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/related",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.RelatedTransactionsResponse, raw=False, options=options)

    async def list_integration_transactions(self, *, x_request_id: str | None = None, environment: str | None = None, needs_attention: bool | None = None, attention_reason: list[models.TransactionAttentionReason] | None = None, mapping_status: list[models.FilterableTransactionMappingStatus] | None = None, functional_ack_status: list[models.FilterableFunctionalAcknowledgmentStatus] | None = None, implementation_ack_status: list[models.FilterableImplementationAcknowledgmentStatus] | None = None, mdn_status: list[models.FilterableTransactionMdnStatus] | None = None, start_date: str | None = None, end_date: str | None = None, cursor: str | None = None, limit: int | None = None, direction: str | None = None, partner_name: str | None = None, partner_id: int | None = None, transaction_set: str | None = None, business_key: str | None = None, message_id: str | None = None, reply_to_message_id: str | None = None, transaction_control_number: str | None = None, functional_group_control_number: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionListResponse]:
        "List transactions\n\n**Required key scope:** `transactions:read`.\nReturns a pageable transaction history for custom transaction viewers, dashboards, and reconciliation workflows. Outbound replies include `replyToMessageId` so they can be shown underneath the inbound document they answer. Each row includes the stable `needsAttention` operator signal, machine-readable `attentionReasons`, and a compact `mappingStatus` so unattended integrations can route failures without fetching every transaction detail. `functionalAckStatus`, `implementationAckStatus`, and `mdnStatus` expose the same compact status values used by their exact list filters. The root `attentionSummary` is an environment-wide count and reconciliation-freshness signal; it is not restricted to the requested page or date window. Exact mapping, functional-acknowledgment, implementation-acknowledgment, and MDN filters use that same asynchronous projection, so check `attentionSummary.freshness.complete` before treating an empty filtered page as proof that no matching transaction exists.\n"
        return await self._transport.request(
            "listIntegrationTransactions", "GET", "/v1/integration/transactions",
            path_params={},
            query={"environment": environment, "needsAttention": needs_attention, "attentionReason": attention_reason, "mappingStatus": mapping_status, "functionalAckStatus": functional_ack_status, "implementationAckStatus": implementation_ack_status, "mdnStatus": mdn_status, "startDate": start_date, "endDate": end_date, "cursor": cursor, "limit": limit, "direction": direction, "partnerName": partner_name, "partnerId": partner_id, "transactionSet": transaction_set, "businessKey": business_key, "messageId": message_id, "replyToMessageId": reply_to_message_id, "transactionControlNumber": transaction_control_number, "functionalGroupControlNumber": functional_group_control_number},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionListResponse, raw=False, options=options)

    async def replay_integration_transaction(self, *, body: models.TransactionReplayRequest, x_request_id: str | None = None, message_id: str, transaction_key: str, idempotency_key: str, options: RequestOptions | None = None) -> ApiResponse[models.TransactionReplayResponse]:
        "Replay an inbound transaction without redelivery\n\n**Required key scope:** `transactions:replay`.\n\nRe-runs mapping for one tenant-visible inbound transaction with the currently published maps and returns the regenerated mapped outputs directly. Historical map revision replay is not part of the public API.\n\nThe only supported delivery is `response_only`. ModernEDI does not put regenerated outputs on the mapped-output queue, invoke mapped-output webhooks, or generate outbound acknowledgements. This endpoint is therefore suitable for inspection and controlled recovery without repeating downstream delivery side effects.\n\nReplay re-applies the currently active inbound protection policy. The stored inbound row must contain successful `signatureVerified` and `encryptionDecrypted` evidence for every protection required in the selected environment. A missing or `false` evidence value fails closed with an `insufficient-message-security:` replay error; consequently, older transactions without that evidence are not replayable while the corresponding protection remains required.\n\n`Idempotency-Key` is required. Repeating the same key and request returns the stored successful replay with `Idempotency-Replayed: true` and does not invoke mapping again. Reusing the key for different replay input returns `409 idempotency_key_conflict`; retry while the same replay is still processing returns `409 idempotency_key_in_progress` with `retryable: true`.\n\nThe replay body is strict JSON: unknown fields are rejected, and `environment`, `mode`, `delivery`, and `reason` must be strings when present (`reason` may also be `null`). Type mismatches return `400 invalid_request` with the offending JSON pointer.\n"
        return await self._transport.request(
            "replayIntegrationTransaction", "POST", "/v1/integration/transactions/{messageId}/{transactionKey}/replays",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={},
            headers={"X-Request-Id": x_request_id, "Idempotency-Key": idempotency_key},
            body=body, response_type=models.TransactionReplayResponse, raw=False, options=options)

    async def unwatch_integration_transaction(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionWatchResponse]:
        "Stop watching a transaction\n\n**Required key scope:** `transactions:write`.\nIdempotently removes a tenant-visible transaction from the selected environment's operator watchlist. The response reports `onWatchlist: false` even when the transaction was already unwatched, so retrying after a network failure is safe. Workspace-wide attention counts and status-filter projections are asynchronous; use their `freshness` object when reconciling an immediately following list response.\n"
        return await self._transport.request(
            "unwatchIntegrationTransaction", "DELETE", "/v1/integration/transactions/{messageId}/{transactionKey}/watch",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionWatchResponse, raw=False, options=options)

    async def validate_integration_transaction_x12(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionX12ValidationResponse]:
        "Validate the X12 retained for a transaction\n\n**Required key scope:** `transactions:read`.\nParses and validates the X12 content ModernEDI retained for this transaction and returns the same structured validation model as `POST /v1/x12/validate`. Invalid X12 is a successful analysis response with `validation.valid=false`, not an HTTP error. The retained X12 can be a complete interchange containing more than one transaction set; use the returned group and transaction indexes when displaying errors. This read-only endpoint lets transaction-viewer keys inspect stored content without granting message-send or transaction-replay authority. It does not rerun mappings, create mapped outputs, replay the transaction, or resend a document.\n"
        return await self._transport.request(
            "validateIntegrationTransactionX12", "GET", "/v1/integration/transactions/{messageId}/{transactionKey}/x12/validation",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionX12ValidationResponse, raw=False, options=options)

    async def watch_integration_transaction(self, *, x_request_id: str | None = None, message_id: str, transaction_key: str, environment: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.TransactionWatchResponse]:
        "Watch a transaction\n\n**Required key scope:** `transactions:write`.\nIdempotently adds a tenant-visible transaction to the selected environment's operator watchlist. Public API watch entries do not expire and remain active until the DELETE operation removes them. The response reports the resulting state, so retrying the same request is safe. Workspace-wide attention counts and status-filter projections are asynchronous; use their `freshness` object when reconciling an immediately following list response.\n"
        return await self._transport.request(
            "watchIntegrationTransaction", "PUT", "/v1/integration/transactions/{messageId}/{transactionKey}/watch",
            path_params={"messageId": message_id, "transactionKey": transaction_key},
            query={"environment": environment},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.TransactionWatchResponse, raw=False, options=options)

class AsyncAccountApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get_integration_usage(self, *, x_request_id: str | None = None, days: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.UsageResponse]:
        "Get plan usage and enforcement status\n\n**Required key scope:** `transactions:read`.\nReturns the tenant's current AS2 message usage, plan thresholds, daily history, and operational signals. Use `rejectionActive`, `status`, and the threshold fields to warn operators before additional messages are rejected. The quota date and `timeZone` are reported in UTC and usage includes both inbound and outbound AS2 messages. Hour bucket labels use `HH:00` values such as `18:00`.\n"
        return await self._transport.request(
            "getIntegrationUsage", "GET", "/v1/usage",
            path_params={},
            query={"days": days},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.UsageResponse, raw=False, options=options)

class AsyncIntegrationEventsApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list_integration_change_events(self, *, x_request_id: str | None = None, environment: str | None = None, cursor: str | None = None, limit: int | None = None, options: RequestOptions | None = None) -> ApiResponse[models.IntegrationChangeEventsResponse]:
        "Poll transaction-state changes\n\n**Required key scope:** `transactions:read`.\n\nReturns a small invalidation feed for transaction state detected after an initial snapshot, including late mapping results, MDNs, 997 and 999 evaluations, mapped-output handoff changes, and attention changes. Events do not duplicate transaction detail. Refetch the referenced transaction to read authoritative current state.\n\nWhen `cursor` is omitted, ModernEDI returns no historical events, `bootstrap=true`, and a `nextCursor` positioned at the current high-water mark. A race-safe custom viewer should:\n\n1. Request this endpoint without a cursor and retain `nextCursor`.\n2. Load its current transaction snapshot from `/v1/integration/transactions`.\n3. Poll this endpoint again using the retained cursor.\n4. Refetch every transaction named by events that arrived while the snapshot loaded.\n\nThereafter, keep sending each `nextCursor` back unchanged. `observedAt` is when the reconciliation sweep detected the change, not necessarily the partner's event time; event order is detection order. The feed is eventually consistent, so inspect `freshness.complete` and `freshness.status` before treating an empty poll as proof that no changes are pending.\n\nChange events have a rolling 30-day retention independent of retained transaction documents. Polling successfully refreshes the cursor's age. A client that resumes with an expired cursor receives `410 cursor_expired`; request a new bootstrap cursor and repeat the snapshot sequence.\n"
        return await self._transport.request(
            "listIntegrationChangeEvents", "GET", "/v1/integration/events",
            path_params={},
            query={"environment": environment, "cursor": cursor, "limit": limit},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.IntegrationChangeEventsResponse, raw=False, options=options)

class AsyncX12ToolsApi:
    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list_x12_transaction_sets(self, *, x_request_id: str | None = None, x12_version: str, options: RequestOptions | None = None) -> ApiResponse[models.X12TransactionSetsResponse]:
        "List transaction sets for an X12 version\n\n**Required key scope:** `configuration:read`.\nReturns the transaction-set identifiers and descriptions available for the normalized X12 version. Both `4010` and `004010` style version values are accepted.\n"
        return await self._transport.request(
            "listX12TransactionSets", "GET", "/v1/x12/versions/{x12Version}/transaction-sets",
            path_params={"x12Version": x12_version},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.X12TransactionSetsResponse, raw=False, options=options)

    async def list_x12_versions(self, *, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.X12VersionsResponse]:
        "List available X12 versions\n\n**Required key scope:** `configuration:read`.\n\nReturns X12 versions for which the tenant has reference syntax trees.\n"
        return await self._transport.request(
            "listX12Versions", "GET", "/v1/x12/versions",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=None, response_type=models.X12VersionsResponse, raw=False, options=options)

    async def validate_x12(self, *, body: RequestBody, x_request_id: str | None = None, options: RequestOptions | None = None) -> ApiResponse[models.X12ValidationResponse]:
        "Parse and validate an X12 interchange\n\n**Required key scope:** `transactions:read`.\nParses an X12 interchange and returns structural, group, transaction, segment, and element validation results without sending anything. Send X12 directly as `application/edi-x12` or `text/plain`, or wrap it in an `x12` field when JSON is more convenient. A syntactically invalid X12 document still returns a 200 validation result; malformed request shapes return a standard 400 error. Request bodies are limited to 3 MiB. Validation is available to read-only viewers and does not grant authority to send X12.\n"
        return await self._transport.request(
            "validateX12", "POST", "/v1/x12/validate",
            path_params={},
            query={},
            headers={"X-Request-Id": x_request_id},
            body=body, response_type=models.X12ValidationResponse, raw=False, options=options)

class AsyncModernEdiClient(AsyncTransport):
    @property
    def mapped_outputs(self) -> AsyncMappedOutputQueueApi:
        return AsyncMappedOutputQueueApi(self)

    @property
    def scenario_runs(self) -> AsyncScenarioRunsApi:
        return AsyncScenarioRunsApi(self)

    @property
    def configuration_as_code(self) -> AsyncConfigurationAsCodeApi:
        return AsyncConfigurationAsCodeApi(self)

    @property
    def outbound_as2(self) -> AsyncOutboundAS2Api:
        return AsyncOutboundAS2Api(self)

    @property
    def as2_connections(self) -> AsyncAS2ConnectionsApi:
        return AsyncAS2ConnectionsApi(self)

    @property
    def partners(self) -> AsyncPartnersApi:
        return AsyncPartnersApi(self)

    @property
    def mappings(self) -> AsyncMappingsApi:
        return AsyncMappingsApi(self)

    @property
    def mapping_runtime(self) -> AsyncMappingRuntimeApi:
        return AsyncMappingRuntimeApi(self)

    @property
    def transactions(self) -> AsyncTransactionViewerApi:
        return AsyncTransactionViewerApi(self)

    @property
    def account(self) -> AsyncAccountApi:
        return AsyncAccountApi(self)

    @property
    def integration_events(self) -> AsyncIntegrationEventsApi:
        return AsyncIntegrationEventsApi(self)

    @property
    def x12(self) -> AsyncX12ToolsApi:
        return AsyncX12ToolsApi(self)
