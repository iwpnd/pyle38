import pytest


@pytest.mark.asyncio
async def test_command_stats(tile38):
    response = await tile38.stats(["fleet"])
    assert response.ok
    assert response.stats == []

    await tile38.set("fleet", "truck1").point(1, 1).exec()
    await tile38.set("zones", "parking1").bounds(1, 1, 1, 1).exec()

    response = await tile38.stats(["fleet", "zones"])
    assert response.ok
    assert len(response.stats) == 2
