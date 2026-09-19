"""Read-only list pagination and bounded, lease-aware mapped-output polling."""
from typing import AsyncIterator, Awaitable, Callable, Iterable, Iterator, TypeVar
from ._transport import ApiResponse
from .generated.models import MappedOutputMessage, MappedOutputQueueResponse

T = TypeVar("T")
P = TypeVar("P")


def _limit(value: int, name: str = "max_pages") -> None:
    if type(value) is not int or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def paginate_cursor(load: Callable[[str | None], P], items: Callable[[P], Iterable[T]],
                    next_cursor: Callable[[P], str | None], *, cursor: str | None = None,
                    max_pages: int = 1000) -> Iterator[T]:
    """Read-only lists: fetch at most max_pages, preserving cursors and rejecting cycles."""
    _limit(max_pages)
    seen = set()
    for _ in range(max_pages):
        if cursor is not None:
            if cursor in seen:
                raise ValueError("Repeated pagination cursor")
            seen.add(cursor)
        page = load(cursor)
        yield from items(page)
        cursor = next_cursor(page)
        if cursor is None:
            return


def iterate_mapped_outputs(load: Callable[[str | None], ApiResponse[MappedOutputQueueResponse]], *,
                           cursor: str | None = None, max_polls: int = 1000) -> Iterator[MappedOutputMessage]:
    """Bounded queue scan; repeated cursors are valid. Persist and acknowledge outputs yourself.

    Does not retry failed polls, acknowledge, deduplicate redeliveries, or continuously watch.
    """
    _limit(max_polls, "max_polls")
    for _ in range(max_polls):
        page = load(cursor).data
        if page is None:
            raise ValueError("Mapped-output poll returned no body")
        yield from page.messages
        cursor = page.next_cursor
        if cursor is None:
            return


async def iterate_mapped_outputs_async(load: Callable[[str | None], Awaitable[ApiResponse[MappedOutputQueueResponse]]], *,
                                       cursor: str | None = None, max_polls: int = 1000) -> AsyncIterator[MappedOutputMessage]:
    """Async bounded queue scan with the same lease semantics as iterate_mapped_outputs."""
    _limit(max_polls, "max_polls")
    for _ in range(max_polls):
        page = (await load(cursor)).data
        if page is None:
            raise ValueError("Mapped-output poll returned no body")
        for item in page.messages:
            yield item
        cursor = page.next_cursor
        if cursor is None:
            return


async def paginate_cursor_async(load: Callable[[str | None], Awaitable[P]], items: Callable[[P], Iterable[T]],
                                next_cursor: Callable[[P], str | None], *, cursor: str | None = None,
                                max_pages: int = 1000) -> AsyncIterator[T]:
    _limit(max_pages)
    seen = set()
    for _ in range(max_pages):
        if cursor is not None:
            if cursor in seen:
                raise ValueError("Repeated pagination cursor")
            seen.add(cursor)
        page = await load(cursor)
        for item in items(page):
            yield item
        cursor = next_cursor(page)
        if cursor is None:
            return
