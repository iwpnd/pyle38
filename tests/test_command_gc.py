import pytest


@pytest.mark.asyncio
async def test_command_gc(tile38_with_follower):
    tile38 = tile38_with_follower

    response = await tile38.gc()
    assert response.ok

    response = await tile38.follower().gc()
    assert response.ok
