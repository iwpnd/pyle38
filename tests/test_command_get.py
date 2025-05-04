import pytest

from pyle38 import Tile38
from pyle38.commands.executable import Compiled
from pyle38.commands.get import Formats, Get

from .helper.random_data import random_point_feature, random_string

key = random_string()
oid = random_string()
obj = random_point_feature()


@pytest.mark.parametrize(
    "fmt, precision, expected",
    [
        ("POINT", None, ["GET", [key, oid, "WITHFIELDS", "POINT"]]),
        ("BOUNDS", None, ["GET", [key, oid, "WITHFIELDS", "BOUNDS"]]),
        ("OBJECT", None, ["GET", [key, oid, "WITHFIELDS"]]),
        ("HASH", 5, ["GET", [key, oid, "WITHFIELDS", "HASH", 5]]),
    ],
    ids=["point", "bounds", "object", "hash"],
)
@pytest.mark.asyncio
async def test_command_get_compile(
    fmt: Formats, precision: int | None, expected: Compiled, tile38: Tile38
) -> None:
    query = Get(tile38.client, key, oid).withfields()
    received = query.output(fmt, precision).compile()
    assert expected == received


@pytest.mark.asyncio
async def test_command_get_query(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    obj = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [1, 1]},
        "properties": {},
    }

    await tile38.set(key, oid).object(obj).exec()
    await tile38.set(key, f"{oid}:driver").string("John").exec()

    obj_response = await tile38.get(key, oid).asObject()
    assert obj == obj_response.object

    expected_point = {"lat": 1, "lon": 1}
    point_response = await tile38.get(key, oid).asPoint()
    assert point_response.point.dict() == expected_point

    expected_bounds = {"ne": {"lat": 1, "lon": 1}, "sw": {"lat": 1, "lon": 1}}
    bounds_response = await tile38.get(key, oid).asBounds()
    assert bounds_response.bounds.dict() == expected_bounds

    expected_hash = "s00twy0"
    hash_response = await tile38.get(key, oid).asHash(7)
    assert expected_hash == hash_response.hash

    expected_string = "John"
    str_obj_response = await tile38.get(key, f"{oid}:driver").asStringObject()
    assert str_obj_response.object == expected_string
