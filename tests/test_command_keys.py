import pytest

from .helper.random_data import random_latitude, random_longitude, random_string


@pytest.mark.asyncio
async def test_command_keys(tile38_with_follower):
    tile38 = tile38_with_follower

    key = random_string()
    id = random_string()

    response = (
        await tile38.set(key, id).point(random_latitude(), random_longitude()).exec()
    )
    assert response.ok

    response = await tile38.keys()
    assert response.ok
    assert response.keys == [key]
