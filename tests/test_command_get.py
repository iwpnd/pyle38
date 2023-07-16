import pytest

from pyle38.commands.get import Get

from .helper.random_data import random_point_feature, random_string

key = random_string()
id = random_string()
object = random_point_feature("Point")


@pytest.mark.parametrize(
    "format, precision, expected",
    [
        ("POINT", None, ["GET", [key, id, "WITHFIELDS", "POINT"]]),
        ("BOUNDS", None, ["GET", [key, id, "WITHFIELDS", "BOUNDS"]]),
        ("OBJECT", None, ["GET", [key, id, "WITHFIELDS"]]),
        ("HASH", 5, ["GET", [key, id, "WITHFIELDS", "HASH", 5]]),
    ],
    ids=["point", "bounds", "object", "hash"],
)
@pytest.mark.asyncio
async def test_command_get_compile(format, precision, expected, tile38):
    query = Get(tile38.client, key, id).withfields()
    received = query.output(format, precision).compile()
    assert expected == received


@pytest.mark.asyncio
async def test_command_get_query(tile38):
    key = random_string()
    id = random_string()
    object = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [1, 1]},
        "properties": {},
    }

    await tile38.set(key, id).object(object).exec()
    await tile38.set(key, f"{id}:driver").string("John").exec()

    received = await tile38.get(key, id).asObject()
    assert object == received.object

    expected_point = {"lat": 1, "lon": 1}
    received = await tile38.get(key, id).asPoint()
    assert received.point.dict() == expected_point

    expected_bounds = {"ne": {"lat": 1, "lon": 1}, "sw": {"lat": 1, "lon": 1}}
    received = await tile38.get(key, id).asBounds()
    assert received.bounds.dict() == expected_bounds

    expected_hash = "s00twy0"
    received = await tile38.get(key, id).asHash(7)
    assert expected_hash == received.hash
    assert received.hash == expected_hash

    expected_string = "John"
    received = await tile38.get(key, f"{id}:driver").asStringObject()
    assert received.object == expected_string
