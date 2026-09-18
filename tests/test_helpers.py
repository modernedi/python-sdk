import asyncio
import hashlib
import hmac
import json
import unittest

from modernedi import paginate_cursor, paginate_cursor_async, verify_mapped_output_webhook, WebhookVerificationError

NOW = 1800000000
SECRET = "synthetic-webhook-secret"
EVENT = {"event": "mapped_output.test", "deliveryId": "delivery-1", "createdAt": "2027-01-15T08:00:00.123456789Z",
         "tenantId": 1, "partnerId": 2, "test": True, "requestId": "req-1", "description": "Synthetic é event"}


def signed(event=EVENT, timestamp=str(NOW), raw=None):
    raw = raw if raw is not None else json.dumps(event, ensure_ascii=False, indent=2).encode()
    signature = hmac.new(SECRET.encode(), timestamp.encode() + b"." + raw, hashlib.sha256).hexdigest()
    return raw, {"X-ModernEDI-Timestamp": timestamp, "X-ModernEDI-Signature": "sha256=" + signature,
                 "X-ModernEDI-Event": event.get("event", "mapped_output.test"), "X-ModernEDI-Delivery-Id": event.get("deliveryId", "delivery-1")}


class HelperTests(unittest.TestCase):
    def test_webhook_verifies_raw_unicode_and_timestamp(self):
        raw, headers = signed()
        actual = verify_mapped_output_webhook(raw, headers, SECRET, now=NOW)
        self.assertEqual(actual, EVENT)
        self.assertEqual(actual["createdAt"], "2027-01-15T08:00:00.123456789Z")

    def test_webhook_accepts_mapped_output(self):
        event = {key: value for key, value in EVENT.items() if key not in {"test", "requestId", "description"}}
        event["event"] = "mapped_output.available"
        event["message"] = {"id": "output-1", "receiptHandle": "handle", "messageId": "msg-1", "transactionKey": "1#2",
            "environment": "test", "mappedOutputKey": "map-output", "purpose": "PROCESSING", "deliveryCount": 1, "sequenceNumber": 0}
        raw, headers = signed(event)
        self.assertEqual(verify_mapped_output_webhook(raw, headers, SECRET, now=NOW), event)

    def test_webhook_rejections(self):
        raw, good = signed()
        cases = [
            (raw + b" ", good, "signature_mismatch"),
            (raw, {**good, "X-ModernEDI-Timestamp": str(NOW - 301)}, "timestamp_outside_tolerance"),
            (raw, {**good, "X-ModernEDI-Timestamp": str(NOW + 301)}, "timestamp_outside_tolerance"),
            (raw, {**good, "X-ModernEDI-Timestamp": "01"}, "invalid_timestamp"),
            (raw, {**good, "X-ModernEDI-Signature": good["X-ModernEDI-Signature"] + "\n"}, "invalid_signature_format"),
            (raw, {**good, "x-modernedi-signature": "extra"}, "duplicate_header"),
            (raw, {**good, "X-ModernEDI-Signature": [good["X-ModernEDI-Signature"], "extra"]}, "duplicate_header"),
            (raw, {**good, "X-ModernEDI-Delivery-Id": "mismatch"}, "invalid_event"),
            (raw, {key: value for key, value in good.items() if key != "X-ModernEDI-Event"}, "missing_header"),
        ]
        bad, headers = signed(raw=b"not json")
        cases.append((bad, headers, "invalid_json"))
        bad, headers = signed({**EVENT, "extension": float("nan")})
        cases.append((bad, headers, "invalid_json"))
        for event in [{**EVENT, "test": False}, {**EVENT, "tenantId": True}, {**EVENT, "message": {}}, {**EVENT, "event": "unknown"}]:
            bad, headers = signed(event)
            cases.append((bad, headers, "invalid_event"))
        for body, headers, code in cases:
            with self.subTest(code=code):
                with self.assertRaises(WebhookVerificationError) as error:
                    verify_mapped_output_webhook(body, headers, SECRET, now=NOW)
                self.assertEqual(error.exception.code, code)

    def test_pagination_preserves_cursor_and_stops(self):
        calls = []
        def load(cursor):
            calls.append(cursor)
            return {"items": [len(calls)], "next": "opaque/+==?#" if cursor is None else None}
        self.assertEqual(list(paginate_cursor(load, lambda p: p["items"], lambda p: p["next"])), [1, 2])
        self.assertEqual(calls, [None, "opaque/+==?#"])

    def test_pagination_rejects_cycles_and_bounds_work(self):
        loader = lambda cursor: {"items": [1], "next": "repeat"}
        with self.assertRaisesRegex(ValueError, "Repeated"):
            list(paginate_cursor(loader, lambda p: p["items"], lambda p: p["next"]))
        self.assertEqual(list(paginate_cursor(loader, lambda p: p["items"], lambda p: p["next"], max_pages=1)), [1])
        with self.assertRaises(ValueError):
            list(paginate_cursor(loader, lambda p: [], lambda p: None, max_pages=0))


class AsyncHelperTests(unittest.IsolatedAsyncioTestCase):
    async def test_async_pagination(self):
        async def load(cursor):
            return {"items": [cursor or "first"], "next": "last" if cursor is None else None}
        self.assertEqual([item async for item in paginate_cursor_async(load, lambda p: p["items"], lambda p: p["next"])], ["first", "last"])
