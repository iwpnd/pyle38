import pytest

from pyle38.client import SubCommand
from pyle38.commands.get import Get


@pytest.mark.parametrize(
    "format, precision, expected",
    [
        (
            SubCommand.POINT.value,
            None,
            ["GET", ["fleet", "truck1", "WITHFIELDS", "POINT"]],
        ),
        (
            SubCommand.BOUNDS.value,
            None,
            ["GET", ["fleet", "truck1", "WITHFIELDS", "BOUNDS"]],
        ),
        (SubCommand.OBJECT.value, None, ["GET", ["fleet", "truck1", "WITHFIELDS"]]),
        (
            SubCommand.HASH.value,
            5,
            ["GET", ["fleet", "truck1", "WITHFIELDS", "HASH", 5]],
        ),
    ],
)
@pytest.mark.asyncio
async def test_get_compile(format, precision, expected, tile38):

    key = "fleet"
    id = "truck1"
    query = Get(tile38.client, key, id).with_fields()

    received = query.output(format, precision).compile()

    assert expected == received


@pytest.mark.asyncio
async def test_get_query(tile38):

    key = "fleet"
    id = "truck1"
    obj = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [1, 1]},
        "properties": {},
    }

    await tile38.set(key, id).object(obj).exec()

    expected_object = {"ok": True, "object": obj, "elapsed": "1 ms"}
    received = await tile38.get(key, id).asObject()

    assert expected_object["object"] == received.object

    expected_point = {"ok": True, "point": {"lat": 1, "lon": 1}, "elapsed": "1 ms"}
    received = await tile38.get(key, id).asPoint()

    assert expected_point["point"] == received.point

    expected_bounds = {
        "ok": True,
        "bounds": {"ne": {"lat": 1, "lon": 1}, "sw": {"lat": 1, "lon": 1}},
        "elapsed": "1 ms",
    }
    received = await tile38.get(key, id).asBounds()

    assert expected_bounds["bounds"] == received.bounds

    expected_hash = {"ok": True, "hash": "s00twy0", "elapsed": "1 ms"}
    received = await tile38.get(key, id).asHash(7)

    assert expected_hash["hash"] == received.hash
