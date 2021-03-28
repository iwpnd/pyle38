import os

import pytest

from pyle38.tile38 import Tile38

default_tile38_leader_uri = os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851"
default_tile38_follower_uri = (
    os.getenv("TILE38_FOLLOWER_URI") or "redis://localhost:9852"
)


@pytest.fixture()
def create_tile38(request, event_loop):
    async def f(uri: str = default_tile38_leader_uri):

        tile38 = Tile38(uri)

        def teardown():
            async def ateardown():
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
def create_tile38_with_follower(request, event_loop):
    async def f(
        uri: str = default_tile38_leader_uri,
        follower_uri: str = default_tile38_follower_uri,
    ):

        tile38 = Tile38(uri, follower_uri)

        def teardown():
            async def ateardown():
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
async def tile38(create_tile38):
    yield await create_tile38()


@pytest.fixture()
async def tile38_with_follower(create_tile38_with_follower):
    yield await create_tile38_with_follower()
