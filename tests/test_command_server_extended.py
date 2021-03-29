import pytest


@pytest.mark.asyncio
async def test_command_server_extended(tile38_with_follower):
    tile38 = tile38_with_follower

    response = await tile38.server_extended()
    assert response.ok
    assert response.stats.tile38_connected_slaves == 1

    response = await tile38.follower().server_extended()
    assert response.ok
    assert response.stats.tile38_connected_slaves == 0
