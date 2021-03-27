import pytest

from pyle38.client import SubCommand
from pyle38.commands.get import Get
from pyle38.tile38 import Tile38

tile38 = Tile38()


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
async def test_get_compile(format, precision, expected):

    key = "fleet"
    id = "truck1"
    query = Get(tile38, key, id).with_fields()

    received = query.output(format, precision).compile()

    assert expected == received


@pytest.mark.asyncio
async def test_get_query():
    await tile38.flush_db()

    key = "fleet"
    id = "truck1"
    obj = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [1, 1]},
        "properties": {},
    }

    await tile38.set(key, id).object(obj).exec()

    expected = {"ok": True, "object": obj, "elapsed": "1ms"}

    received = await tile38.get(key, id).asObject()

    assert expected["object"] == received.object
