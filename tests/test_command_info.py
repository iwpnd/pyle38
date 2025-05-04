import pytest

from pyle38 import Tile38


@pytest.mark.asyncio
async def test_command_info(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    leaderResponse = await tile38.info()
    assert leaderResponse.ok

    followerResponse = await tile38.follower().info()
    assert followerResponse.ok
