import pytest


@pytest.mark.asyncio
async def test_command_gc(tile38):
    response = await tile38.gc()
    assert response.ok
