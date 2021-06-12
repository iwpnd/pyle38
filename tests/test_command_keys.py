import asyncio

import pytest


@pytest.mark.asyncio
async def test_command_keys(tile38_with_follower):
    tile38 = tile38_with_follower

    key = "fleet"
    id = "truck"

    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.keys()
    assert response.ok
    assert response.keys == [key]

    await asyncio.sleep(0.1)

    response = await tile38.follower().keys("fl*")
    assert response.ok
    assert response.keys == [key]
