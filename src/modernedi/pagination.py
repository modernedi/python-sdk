"""Opaque-cursor iteration without hidden endpoint assumptions."""
from typing import AsyncIterator, Awaitable, Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")
P = TypeVar("P")


def _limit(max_pages: int) -> None:
    if type(max_pages) is not int or max_pages < 1:
        raise ValueError("max_pages must be a positive integer")


def paginate_cursor(load: Callable[[str | None], P], items: Callable[[P], Iterable[T]],
                    next_cursor: Callable[[P], str | None], *, cursor: str | None = None,
                    max_pages: int = 1000) -> Iterator[T]:
    """Fetch at most max_pages, preserving cursors exactly and rejecting cycles."""
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
