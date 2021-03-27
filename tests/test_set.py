import pytest

from pyle38.commands.set import Set


@pytest.mark.asyncio
async def test_set_compile(tile38):

    key = "fleet"
    id = "truck1"
    query = Set(tile38.client, key, id).nx().point(1, 1)

    expected = ["SET", [key, id, "NX", "POINT", 1, 1]]
    received = query.compile()

    assert expected == received


@pytest.mark.asyncio
async def test_set_query(tile38):

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
