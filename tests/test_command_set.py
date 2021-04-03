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

fields = {"speed": 100, "state": 1}


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
        (
            [
                "SET",
                [key, id, "FIELD", "speed", 100, "FIELD", "state", 1, "POINT", 1, 1],
            ],
            Set(client, key, id).fields(fields).point(1, 1).compile(),
        ),
    ],
    ids=["point", "bounds", "object", "hash", "string", "with fields"],
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


@pytest.mark.asyncio
async def test_command_set_with_fields(tile38):
    response = await tile38.set(key, id).fields(fields).point(1, 1).exec()
    assert response.ok

    response = await tile38.get(key, id).with_fields().asObject()
    assert response.ok
    assert response.fields == fields
