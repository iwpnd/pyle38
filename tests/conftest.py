import os
from collections.abc import AsyncGenerator, Awaitable, Callable
from typing import Any

import pytest

from pyle38 import Tile38

default_tile38_leader_url = os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851"
default_tile38_follower_url = (
    os.getenv("TILE38_FOLLOWER_URI") or "redis://localhost:9852"
)


@pytest.fixture()
async def create_tile38():  # type: ignore[no-untyped-def]
    teardown_clients = []

    async def client_factory(url: str = default_tile38_leader_url) -> Tile38:
        tile38 = Tile38(url)
        # make sure to reset readonly
        await tile38.readonly(False)

        async def teardown() -> None:
            try:
                await tile38.flushdb()
                await tile38.readonly(False)
            # TODO: find explicit exception
            except Exception as e:
                print(e)
                await tile38.flushdb()

            await tile38.quit()

        teardown_clients.append(teardown)
        return tile38

    yield client_factory

    for teardown in teardown_clients:
        await teardown()


@pytest.fixture()
async def create_tile38_with_follower():  # type: ignore[no-untyped-def]
    teardown_clients = []

    async def client_factory(
        url: str = default_tile38_leader_url,
        follower_url: str = default_tile38_follower_url,
    ) -> Tile38:
        tile38 = Tile38(url, follower_url)
        # make sure to reset readonly
        await tile38.readonly(False)

        async def teardown() -> None:
            try:
                await tile38.flushdb()
            # TODO: find explicit exception
            except Exception as e:
                print(e)
                await tile38.flushdb()

            await tile38.quit()

        teardown_clients.append(teardown)
        return tile38

    yield client_factory

    for teardown in teardown_clients:
        await teardown()


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
