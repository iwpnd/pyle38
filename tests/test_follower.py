import pytest

from pyle38.errors import Tile38Error
from pyle38.tile38 import Follower


@pytest.mark.asyncio
async def test_missing_follower_raises():
    with pytest.raises(Tile38Error):
        Follower(None)
