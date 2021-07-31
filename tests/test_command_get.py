import pytest

from pyle38.commands.get import Get

key = "fleet"
id = "truck1"
obj = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [1, 1]},
    "properties": {},
}


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

    received = await tile38.get(key, id).asBounds()
    assert expected_bounds["bounds"] == received.bounds

    expected_hash = {"ok": True, "hash": "s00twy0", "elapsed": "1 ms"}
    received = await tile38.get(key, id).asHash(7)
    assert expected_hash["hash"] == received.hash
