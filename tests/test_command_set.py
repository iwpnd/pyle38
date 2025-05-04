import json

import pytest

from pyle38 import Tile38
from pyle38.client import Client
from pyle38.commands.executable import Compiled
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
oid = random_string()
obj: dict = random_polygon_feature()
fields = {"speed": 100, "state": 1}


@pytest.mark.parametrize(
    "expected, received",
    [
        (
            ["SET", [key, oid, "NX", "POINT", 1, 1]],
            Set(client, key, oid).nx().point(1, 1).compile(),
        ),
        (
            ["SET", [key, oid, "NX", "POINT", 1, 1, 1]],
            Set(client, key, oid).nx().point(1, 1, 1).compile(),
        ),
        (
            ["SET", [key, oid, "EX", 5, "BOUNDS", 1, 1, 1, 1]],
            Set(client, key, oid).ex(5).bounds(1, 1, 1, 1).compile(),
        ),
        (
            ["SET", [key, oid, "XX", "OBJECT", json.dumps(obj)]],
            Set(client, key, oid).xx().object(obj).compile(),
        ),
        (
            ["SET", [key, oid, "HASH", "u33d"]],
            Set(client, key, oid).hash("u33d").compile(),
        ),
        (
            ["SET", [key, oid, "STRING", oid]],
            Set(client, key, oid).string(oid).compile(),
        ),
        (
            [
                "SET",
                [key, oid, "FIELD", "speed", 100, "FIELD", "state", 1, "POINT", 1, 1],
            ],
            Set(client, key, oid).fields(fields).point(1, 1).compile(),
        ),
    ],
    ids=["point", "point_z", "bounds", "object", "hash", "string", "with fields"],
)
@pytest.mark.asyncio
async def test_command_set_compile(expected: Compiled, received: Compiled) -> None:
    assert expected == received


@pytest.mark.asyncio
async def test_command_set_get(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    obj = random_polygon_feature()

    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    expected = obj
    received = await tile38.get(key, oid).asObject()

    assert received.ok
    assert expected == received.object


@pytest.mark.asyncio
async def test_command_set_get_point_z(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()

    response = await tile38.set(key, oid).point(1, 1, 1).exec()
    assert response.ok

    received = await tile38.get(key, oid).asPoint()

    assert received.ok
    assert received.point.lat == 1.0
    assert received.point.lon == 1.0
    assert received.point.z == 1.0

    response = await tile38.set(key, oid).point(1, 1).exec()
    assert response.ok

    received = await tile38.get(key, oid).asPoint()

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
async def test_command_set_get_with_fields(
    tile38: Tile38, key: str, value: str | float | int | dict
) -> None:
    key = random_string()
    oid = random_string()
    [lng, lat] = random_position()

    fields = {key: value}

    response = await tile38.set(key, oid).fields(fields).point(lat, lng).exec()
    assert response.ok

    response = await tile38.get(key, oid).withfields().asObject()
    assert response.ok
    assert response.fields == fields
