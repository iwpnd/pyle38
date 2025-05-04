import pytest

from pyle38 import Tile38

from .helper.random_data import random_latitude, random_longitude, random_string


@pytest.mark.asyncio
async def test_command_keys(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    key = random_string()
    oid = random_string()

    response = (
        await tile38.set(key, oid).point(random_latitude(), random_longitude()).exec()
    )
    assert response.ok

    response = await tile38.keys()
    assert response.ok
    assert response.keys == [key]
