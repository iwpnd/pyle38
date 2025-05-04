import pytest

from pyle38 import Tile38


@pytest.mark.asyncio
async def test_command_ping(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    response = await tile38.ping()
    assert response.ok
    assert response.ping == "pong"

    response = await tile38.follower().ping()
    assert response.ok
    assert response.ping == "pong"
