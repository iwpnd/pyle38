import pytest

from pyle38 import Tile38


@pytest.mark.asyncio
async def test_command_gc(tile38: Tile38) -> None:
    response = await tile38.gc()
    assert response.ok
