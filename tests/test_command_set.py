import json

import pytest

from pyle38.client import Client
from pyle38.commands.set import Set

client = Client("test")

key = "fleet"
id = "truck1"
obj = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [1, 1]},
    "properties": {},
}


@pytest.mark.parametrize(
    "expected, received",
    [
        (
            ["SET", [key, id, "NX", "POINT", 1, 1]],
            Set(client, key, id).nx().point(1, 1).compile(),
        ),
        (
            ["SET", [key, id, "EX", 5, "BOUNDS", 1, 1, 1, 1]],
            Set(client, key, id).ex(5).bounds(1, 1, 1, 1).compile(),
        ),
        (
            ["SET", [key, id, "XX", "OBJECT", json.dumps(obj)]],
            Set(client, key, id).xx().object(obj).compile(),
        ),
        (
            ["SET", [key, id, "HASH", "u33d"]],
            Set(client, key, id).hash("u33d").compile(),
        ),
        (["SET", [key, id, "STRING", id]], Set(client, key, id).string(id).compile()),
    ],
    ids=["point", "bounds", "object", "hash", "string"],
)
@pytest.mark.asyncio
async def test_command_set_compile(expected, received):

    assert expected == received


@pytest.mark.asyncio
async def test_command_set_query(tile38):
    response = await tile38.set(key, id).object(obj).exec()
    assert response.ok

    expected = {"ok": True, "object": obj, "elapsed": "1ms"}

    received = await tile38.get(key, id).asObject()

    assert expected["object"] == received.object
