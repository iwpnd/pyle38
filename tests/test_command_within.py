from typing import Any

import pytest

from pyle38 import Tile38
from pyle38.commands.executable import Compiled
from pyle38.commands.within import Format, Within
from pyle38.models import Feature, Polygon

from .helper.random_data import random_string

key = random_string()
oid = random_string()
feature = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [13.37, 52.25]},
    "properties": {"id": oid},
}
polygon = {
    "type": "Polygon",
    "coordinates": [
        [
            [13.361263275146484, 52.24630137198303],
            [13.379974365234373, 52.24630137198303],
            [13.379974365234373, 52.256705331409506],
            [13.361263275146484, 52.256705331409506],
            [13.361263275146484, 52.24630137198303],
        ]
    ],
}

expected = {"id": oid, "object": feature}


@pytest.mark.parametrize(
    "fmt, expected",
    [
        (
            "OBJECTS",
            [
                "WITHIN",
                [
                    key,
                    "MATCH",
                    "*",
                    "BUFFER",
                    10,
                    "NOFIELDS",
                    "SPARSE",
                    1,
                    "CURSOR",
                    0,
                    "LIMIT",
                    10,
                    "WHERE",
                    "foo",
                    1,
                    1,
                    "WHERE",
                    "bar",
                    1,
                    1,
                    "WHEREIN",
                    "foo",
                    1,
                    1,
                    "WHEREIN",
                    "bar",
                    1,
                    1,
                    "FENCE",
                    "DETECT",
                    "enter,exit",
                    "COMMANDS",
                    "del,set",
                    "CIRCLE",
                    1.0,
                    1.0,
                    100,
                ],
            ],
        )
    ],
    ids=["OBJECTS"],
)
@pytest.mark.asyncio
async def test_command_within_compile(
    tile38: Tile38, fmt: Format, expected: Compiled
) -> None:
    query = (
        Within(tile38.client, key)
        .match("*")
        .buffer(10)
        .nofields()
        .sparse(1)
        .cursor(0)
        .limit(10)
        .where("foo", 1, 1)
        .where("bar", 1, 1)
        .wherein("foo", [1])
        .wherein("bar", [1])
        .fence()
        .detect(["enter", "exit"])
        .commands(["del", "set"])
        .circle(1, 1, 100)
    )

    received = query.output(fmt).compile()

    assert expected == received


@pytest.mark.asyncio
async def test_command_within_circle(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_where_circle(tile38: Tile38) -> None:
    await tile38.set(key, oid).fields({"maxspeed": 120}).object(feature).exec()
    await tile38.set(key, "truck2").fields({"maxspeed": 100}).object(feature).exec()

    response = (
        await tile38
        .within(key)
        .where("maxspeed", 120, 120)
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120]})

    response = (
        await tile38
        .within(key)
        .where("maxspeed", 100, 120)
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_within_wherein_circle(tile38: Tile38) -> None:
    await tile38.set(key, oid).fields({"maxspeed": 120}).object(feature).exec()
    await tile38.set(key, "truck2").fields({"maxspeed": 100}).object(feature).exec()

    response = (
        await tile38
        .within(key)
        .wherein("maxspeed", [120])
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120]})

    response = (
        await tile38
        .within(key)
        .wherein("maxspeed", [100, 120])
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_within_object(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    polygon: dict[str, Any] = {
        "type": "Polygon",
        "coordinates": [
            [
                [13.361263275146484, 52.24630137198303],
                [13.379974365234373, 52.24630137198303],
                [13.379974365234373, 52.256705331409506],
                [13.361263275146484, 52.256705331409506],
                [13.361263275146484, 52.24630137198303],
            ]
        ],
    }

    response = await tile38.within(key).object(polygon).asObjects()

    assert response.ok
    assert response.objects[0].dict() == expected

    response = await tile38.within(key).object(Polygon(**polygon)).asObjects()

    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_hash(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).hash("u3390").asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_quadkey(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).quadkey("120").asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_tile(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).tile(2200, 1348, 12).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_bounds(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).bounds(52.24, 13.36, 52.256, 13.379).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_sector(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = (
        await tile38.within(key).sector(52.25191, 13.37230, 1000, 180, 270).asObjects()
    )
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_get(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.set("zones", "zone").object(polygon).exec()
    assert response.ok

    response = await tile38.within(key).get("zones", "zone").asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_within_return_points(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asPoints()
    assert response.ok
    assert response.points[0].dict() == {
        "id": oid,
        "point": {"lat": 52.25, "lon": 13.37},
    }


@pytest.mark.asyncio
async def test_command_within_return_ids(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asIds()
    assert response.ok
    assert response.ids == [oid]


@pytest.mark.asyncio
async def test_command_within_return_count(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asCount()
    assert response.ok
    assert response.count == 1


@pytest.mark.asyncio
async def test_command_within_return_hashes(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asHashes(5)
    assert response.ok
    assert response.hashes[0].dict() == {"id": oid, "hash": "u3390"}


@pytest.mark.asyncio
async def test_command_within_return_bounds(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asBounds()
    assert response.ok
    assert response.bounds[0].dict() == {
        "id": oid,
        "bounds": {
            "ne": {"lat": 52.25, "lon": 13.37},
            "sw": {"lat": 52.25, "lon": 13.37},
        },
    }


@pytest.mark.asyncio
async def test_command_within_buffer_return_count(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    search_area: dict[str, Any] = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [13.37009847164154, 52.2498254610514],
                    [13.370516896247862, 52.2498254610514],
                    [13.370516896247862, 52.25017851139772],
                    [13.37009847164154, 52.25017851139772],
                    [13.37009847164154, 52.2498254610514],
                ]
            ],
        },
    }

    response = await tile38.within(key).object(search_area).asCount()
    assert response.ok
    assert response.count == 0

    response = await tile38.within(key).buffer(10).object(search_area).asCount()
    assert response.ok
    assert response.count == 1

    response = (
        await tile38.within(key).buffer(10).object(Feature(**search_area)).asCount()
    )
    assert response.ok
    assert response.count == 1
