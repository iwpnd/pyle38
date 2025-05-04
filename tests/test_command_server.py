import time

import pytest

from pyle38 import Tile38


@pytest.mark.asyncio
async def test_command_server(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    leaderResponse = await tile38.server()
    assert leaderResponse.ok
    assert leaderResponse.stats.num_points == 0

    with pytest.raises(AttributeError):
        # NOTE: we know that type is wrong here, we just wanna test it not being here
        assert leaderResponse.stats.caught_up  # type: ignore[attr-defined,unused-ignore]

    time.sleep(0.2)

    followerResponse = await tile38.follower().server()
    assert followerResponse.ok
    assert followerResponse.stats.num_points == 0
    assert followerResponse.stats.caught_up is True
    assert followerResponse.stats.caught_up_once is True
