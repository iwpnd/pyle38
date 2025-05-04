import pytest

from pyle38 import Tile38

from .helper.random_data import random_polygon_feature, random_string


@pytest.mark.asyncio
async def test_command_hooks(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    key = random_string()
    oid = random_string()
    obj = random_polygon_feature()
    endpoint = "kafka://10.0.20.78:9092/warehouse"

    response = await tile38.sethook(oid, endpoint).within(key).object(obj).activate()

    assert response.ok

    response = await tile38.hooks()
    assert response.ok
    assert len(response.hooks) == 1
