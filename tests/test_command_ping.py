import pytest


@pytest.mark.asyncio
async def test_command_ping(tile38_with_follower):
    tile38 = tile38_with_follower

    response = await tile38.ping()
    assert response.ok
    assert response.ping == "pong"

    response = await tile38.follower().ping()
    assert response.ok
    assert response.ping == "pong"
