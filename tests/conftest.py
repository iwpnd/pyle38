import pytest

from pyle38.tile38 import Tile38

default_tile38_url = "redis://localhost:9851"


@pytest.fixture()
def create_tile38(request, event_loop):
    async def f(url: str = default_tile38_url):

        tile38 = Tile38(url)

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
