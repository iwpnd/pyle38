import os
from asyncio import AbstractEventLoop
from collections.abc import AsyncGenerator, Awaitable, Callable
from typing import Any

import pytest
from _pytest.fixtures import SubRequest

from pyle38 import Tile38

default_tile38_leader_url = os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851"
default_tile38_follower_url = (
    os.getenv("TILE38_FOLLOWER_URI") or "redis://localhost:9852"
)


@pytest.fixture()
def create_tile38(
    request: SubRequest, event_loop: AbstractEventLoop
) -> Callable[..., Awaitable[Tile38]]:
    async def f(url: str = default_tile38_leader_url) -> Tile38:
        tile38 = Tile38(url)
        # make sure to reset readonly
        await tile38.readonly(False)

        def teardown() -> None:
            async def ateardown() -> None:
                try:
                    await tile38.flushdb()
                    await tile38.readonly(False)
                # TODO: find explicit exception
                except Exception:
                    await tile38.flushdb()

                await tile38.quit()

            if event_loop.is_running():
                event_loop.create_task(ateardown())
            else:
                event_loop.run_until_complete(ateardown())

        request.addfinalizer(teardown)
        return tile38

    return f


@pytest.fixture()
def create_tile38_with_follower(
    request: SubRequest, event_loop: AbstractEventLoop
) -> Callable[..., Awaitable[Tile38]]:
    async def f(
        url: str = default_tile38_leader_url,
        follower_url: str = default_tile38_follower_url,
    ) -> Tile38:
        tile38 = Tile38(url, follower_url)
        # make sure to reset readonly
        await tile38.readonly(False)

        def teardown() -> None:
            async def ateardown() -> None:
                try:
                    await tile38.flushdb()
                # TODO: find explicit exception
                except Exception:
                    await tile38.flushdb()

                await tile38.quit()

            if event_loop.is_running():
                event_loop.create_task(ateardown())
            else:
                event_loop.run_until_complete(ateardown())

        request.addfinalizer(teardown)
        return tile38

    return f


@pytest.fixture()
async def tile38(
    create_tile38: Callable[..., Awaitable[Tile38]],
) -> AsyncGenerator[Any, Any]:
    yield await create_tile38()


@pytest.fixture()
async def tile38_with_follower(
    create_tile38_with_follower: Callable[..., Awaitable[Tile38]],
) -> AsyncGenerator[Any, Any]:
    yield await create_tile38_with_follower()
