import pytest


@pytest.mark.asyncio
async def test_command_info(tile38_with_follower):
    tile38 = tile38_with_follower

    response = await tile38.info()
    assert response.ok

    response = await tile38.follower().info()
    assert response.ok
