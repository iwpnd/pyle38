import pytest

from pyle38 import Tile38
from pyle38.errors import Tile38NotCaughtUpError
from pyle38.parse_response import parse_response


@pytest.mark.asyncio
async def test_command_healthz(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    response = await tile38.healthz()
    assert response.ok

    response = await tile38.follower().healthz()
    assert response.ok


@pytest.mark.asyncio
async def test_parse_command_raises() -> None:
    with pytest.raises(Tile38NotCaughtUpError):
        parse_response('{"ok":false,"err":"not caught up","elapsed":"1ms"}')
