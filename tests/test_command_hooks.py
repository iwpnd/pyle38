import pytest

from .helper.random_data import random_feature, random_string


@pytest.mark.asyncio
async def test_command_hooks(tile38_with_follower):
    tile38 = tile38_with_follower

    key = random_string()
    id = random_string()
    object = random_feature("Polygon")
    endpoint = "kafka://10.0.20.78:9092/warehouse"

    response = await tile38.sethook(id, endpoint).within(key).object(object).activate()

    assert response.ok

    response = await tile38.hooks()
    assert response.ok
    assert len(response.hooks) == 1
