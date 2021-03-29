import pytest


@pytest.mark.asyncio
async def test_command_server(tile38_with_follower):
    tile38 = tile38_with_follower

    response = await tile38.server()
    assert response.ok
    assert response.stats.num_points == 0

    with pytest.raises(AttributeError):
        assert response.stats.caught_up

    response = await tile38.follower().server()
    assert response.ok
    assert response.stats.num_points == 0
    assert response.stats.caught_up is True
    assert response.stats.caught_up_once is True
