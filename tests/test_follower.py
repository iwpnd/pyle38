import pytest

from pyle38.errors import Pyle38NoFollowerSetError
from pyle38.follower import Follower


@pytest.mark.asyncio
async def test_missing_follower_raises() -> None:
    with pytest.raises(Pyle38NoFollowerSetError):
        Follower("")
