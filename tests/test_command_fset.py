import pytest

from pyle38.commands.fset import Fset

key = "fleet"
id = "truck1"
obj = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [1, 1]},
    "properties": {},
}

fields = {"speed": 100, "state": 1}


@pytest.mark.asyncio
async def test_command_fset_compile(tile38):
    received = Fset(tile38.client, key, id, fields).compile()
    expected = ["FSET", [key, id, "speed", 100, "state", 1]]

    assert received == expected


@pytest.mark.asyncio
async def test_command_fset(tile38):
    response = await tile38.set(key, id).object(obj).exec()
    assert response.ok

    response = await tile38.fset(key, id, fields).exec()
    assert response.ok

    response = await tile38.get(key, id).withfields().asObject()
    assert response.ok
    assert response.fields == fields
