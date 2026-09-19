"""Shared queue traces through both public clients; no network or implicit acknowledgments."""
import asyncio
import json
from pathlib import Path
import unittest

import httpx
from modernedi import ModernEdiClient, AsyncModernEdiClient, iterate_mapped_outputs, iterate_mapped_outputs_async

CORPUS = json.loads((Path(__file__).parent / "fixtures/queue-iteration.json").read_text(encoding="utf-8"))


class QueueIterationTests(unittest.TestCase):
    def test_shared_queue_iteration(self):
        for row in CORPUS["cases"]:
            for asynchronous in (False, True):
                with self.subTest(case=row["id"], asynchronous=asynchronous):
                    polls = 0
                    expected_cursor = row.get("cursor")

                    def respond(request):
                        nonlocal polls, expected_cursor
                        self.assertEqual(request.url.params.get("cursor"), expected_cursor)
                        page = row["pages"][min(polls, len(row["pages"]) - 1)]
                        polls += 1
                        expected_cursor = page["nextCursor"]
                        return httpx.Response(200, json={"success": True, "environment": "test", "limit": 1,
                            "visibilityTimeoutSeconds": 120, "nextCursor": expected_cursor, "hasMore": expected_cursor is not None,
                            "messages": [dict(CORPUS["message"], id=id) for id in page["items"]]})

                    options = dict(cursor=row.get("cursor"), max_polls=row["maxPolls"])
                    if asynchronous:
                        async def run():
                            async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http:
                                async with AsyncModernEdiClient(api_key="synthetic", http_client=http) as client:
                                    return [item.id async for item in iterate_mapped_outputs_async(
                                        lambda cursor: client.mapped_outputs.poll_mapped_outputs(cursor=cursor, environment="test"), **options)]
                        actual = asyncio.run(run())
                    else:
                        with httpx.Client(transport=httpx.MockTransport(respond)) as http:
                            with ModernEdiClient(api_key="synthetic", http_client=http) as client:
                                actual = [item.id for item in iterate_mapped_outputs(
                                    lambda cursor: client.mapped_outputs.poll_mapped_outputs(cursor=cursor, environment="test"), **options)]
                    self.assertEqual(actual, row["expected"])
                    self.assertEqual(polls, row["polls"])

    def test_bounds_and_poll_errors(self):
        for limit in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                list(iterate_mapped_outputs(lambda _: self.fail("unexpected poll"), max_polls=limit))
        def fail(_):
            raise RuntimeError("lost poll response")
        with self.assertRaisesRegex(RuntimeError, "lost poll response"):
            list(iterate_mapped_outputs(fail))

    def test_async_bounds_and_poll_errors(self):
        async def run():
            for limit in (0, -1, 1.5, True):
                with self.assertRaisesRegex(ValueError, "max_polls"):
                    async for _ in iterate_mapped_outputs_async(lambda _: self.fail("unexpected poll"), max_polls=limit):
                        pass
            async def fail(_):
                raise RuntimeError("lost poll response")
            with self.assertRaisesRegex(RuntimeError, "lost poll response"):
                async for _ in iterate_mapped_outputs_async(fail):
                    pass
        asyncio.run(run())
