import pytest

from pyle38 import Tile38
from pyle38.errors import Tile38KeyNotFoundError, Tile38PathNotFoundError

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_jset_jget_jdel(tile38_with_follower: Tile38) -> None:
    tile38 = tile38_with_follower

    response = await tile38.jset(key="user", oid="901", path="name", value="Tom")
    assert response.ok

    response = await tile38.jget("user", "901")
    assert response.ok
    assert response.value == '{"name":"Tom"}'

    response = await tile38.jdel("user", "901", "name")
    assert response.ok

    response = await tile38.jget("user", "901", "name")
    assert response.ok
    assert response.value == "{}"


@pytest.mark.asyncio
async def test_command_j_options(tile38: Tile38) -> None:
    obj = {"type": "LineString", "coordinates": [[0, 0], [1, 1]]}

    response = await tile38.set("linestring", "1").object(obj).exec()
    assert response.ok

    response = await tile38.get("linestring", "1").asObject()
    assert response.ok
    assert response.object == obj

    response = await tile38.jset("linestring", "1", "coordinates.-1", "[2,2]", "RAW")
    assert response.ok

    response = await tile38.jget("linestring", "1")
    assert response.ok
    assert response.value == '{"type":"LineString","coordinates":[[0,0],[1,1],[2,2]]}'

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.jdel(random_string(), random_string(), random_string())

    with pytest.raises(Tile38PathNotFoundError):
        await tile38.jdel("linestring", random_string(), random_string())
