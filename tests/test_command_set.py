import json

import pytest

from pyle38.client import Client
from pyle38.commands.set import Set

from .helper.random_data import (
    random_float,
    random_integer,
    random_polygon_feature,
    random_position,
    random_string,
)

client = Client("test")

key = random_string()
id = random_string()
obj: dict = random_polygon_feature()
fields = {"speed": 100, "state": 1}


@pytest.mark.parametrize(
    "expected, received",
    [
        (
            ["SET", [key, id, "NX", "POINT", 1, 1]],
            Set(client, key, id).nx().point(1, 1).compile(),
        ),
        (
            ["SET", [key, id, "NX", "POINT", 1, 1, 1]],
            Set(client, key, id).nx().point(1, 1, 1).compile(),
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
    ids=["point", "point_z", "bounds", "object", "hash", "string", "with fields"],
)
@pytest.mark.asyncio
async def test_command_set_compile(expected, received):
    assert expected == received


@pytest.mark.asyncio
async def test_command_set_get(tile38):
    key = random_string()
    id = random_string()
    obj = random_polygon_feature()

    response = await tile38.set(key, id).object(obj).exec()
    assert response.ok

    expected = obj
    received = await tile38.get(key, id).asObject()

    assert received.ok
    assert expected == received.object


@pytest.mark.asyncio
async def test_command_set_get_point_z(tile38):
    key = random_string()
    id = random_string()

    response = await tile38.set(key, id).point(1, 1, 1).exec()
    assert response.ok

    received = await tile38.get(key, id).asPoint()

    assert received.ok
    assert received.point.lat == 1.0
    assert received.point.lon == 1.0
    assert received.point.z == 1.0

    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    received = await tile38.get(key, id).asPoint()

    assert received.ok
    assert received.point.lat == 1.0
    assert received.point.lon == 1.0
    assert not received.point.z


@pytest.mark.parametrize(
    "key, value",
    [
        (
            "integer",
            random_integer(),
        ),
        (
            "float",
            random_float(),
        ),
        (
            "string",
            random_string(),
        ),
        (
            "dictionary",
            {
                "foo": random_string(),
                "bar": random_float(),
            },
        ),
    ],
    ids=["integer", "float", "string", "dictionary"],
)
@pytest.mark.asyncio
async def test_command_set_get_with_fields(tile38, key, value):
    key = random_string()
    id = random_string()
    [lng, lat] = random_position()

    fields = {key: value}

    response = await tile38.set(key, id).fields(fields).point(lat, lng).exec()
    assert response.ok

    response = await tile38.get(key, id).withfields().asObject()
    assert response.ok
    assert response.fields == fields
