from typing import Any

import pytest

from pyle38 import Tile38
from pyle38.commands.intersects import Intersects
from pyle38.errors import Pyle38BadObjectInputError
from pyle38.models import Feature, Polygon

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_intersects_compile(tile38: Tile38) -> None:
    key = random_string()

    expected = [
        "INTERSECTS",
        [
            key,
            "MATCH",
            "*",
            "BUFFER",
            10,
            "NOFIELDS",
            "SPARSE",
            1,
            "CLIP",
            "CURSOR",
            0,
            "LIMIT",
            10,
            "WHERE",
            "foo",
            1,
            1,
            "WHERE",
            "bar == 1",
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
    ]

    query = (
        Intersects(tile38.client, key)
        .match("*")
        .buffer(10)
        .nofields()
        .sparse(1)
        .clip()
        .cursor(0)
        .limit(10)
        .where("foo", 1, 1)
        .where_expr("bar == 1")
        .wherein("foo", [1])
        .wherein("bar", [1])
        .fence()
        .detect(["enter", "exit"])
        .commands(["del", "set"])
        .circle(1, 1, 100)
    )

    received = query.output("OBJECTS", None).compile()

    assert expected == received


key = random_string()
oid = random_string()
feature = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [13.37, 52.25]},
    "properties": {"id": oid},
}
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

expected = {"id": oid, "object": feature}


@pytest.mark.asyncio
async def test_command_intersects_with_fields(tile38: Tile38) -> None:
    # field type str
    name = "Tom"
    # field type float
    weight = 111.1
    # field type int
    height = 190
    # field type dict
    info = {"height": height, "weight": weight, "name": name}

    response = (
        await tile38.set(key, oid)
        .fields({"info": info, "height": height, "weight": weight, "name": name})
        .object(feature)
        .exec()
    )
    assert response.ok

    response = (
        await tile38.intersects(key).bounds(52.24, 13.36, 52.256, 13.379).asObjects()
    )
    assert response.ok
    assert response.objects[0].dict() == {
        **expected,
        # in lexical order
        "fields": [height, info, name, weight],
    }


@pytest.mark.asyncio
async def test_command_intersects_circle(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).circle(52.25, 13.37, 100).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_intersects_where_circle(tile38: Tile38) -> None:
    await (
        tile38.set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .object(feature)
        .exec()
    )
    await (
        tile38.set(key, "truck1")
        .fields({"maxspeed": 100, "maxweight": 1000})
        .object(feature)
        .exec()
    )

    response = (
        await tile38.intersects(key)
        .where("maxspeed", 120, 120)
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120, 1000]})

    response = (
        await tile38.intersects(key)
        .where("maxspeed", 100, 120)
        .where("maxweight", 1000, 1000)
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_intersects_wherein_circle(tile38: Tile38) -> None:
    await (
        tile38.set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .object(feature)
        .exec()
    )
    await (
        tile38.set(key, "truck1")
        .fields({"maxspeed": 100, "maxweight": 1000})
        .object(feature)
        .exec()
    )

    response = (
        await tile38.intersects(key)
        .wherein("maxspeed", [120])
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120, 1000]})

    response = (
        await tile38.intersects(key)
        .wherein("maxspeed", [100, 120])
        .wherein("maxweight", [1000])
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_intersects_where_expr_circle(tile38: Tile38) -> None:
    await (
        tile38.set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .object(feature)
        .exec()
    )
    await (
        tile38.set(key, "truck1")
        .fields({"maxspeed": 100, "maxweight": 1000})
        .object(feature)
        .exec()
    )

    response = (
        await tile38.intersects(key)
        .where_expr("maxspeed >= 100 && maxspeed <= 120 && maxweight == 1000")
        .circle(52.25, 13.37, 100)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_intersects_object(tile38: Tile38) -> None:
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
    featurePolygon: dict[str, Any] = {
        "type": "Feature",
        "properties": {},
        "geometry": polygon,
    }

    response = await tile38.intersects(key).object(polygon).asObjects()

    assert response.ok
    assert response.objects[0].dict() == expected

    response = await tile38.intersects(key).object(Polygon(**polygon)).asObjects()

    assert response.ok
    assert response.objects[0].dict() == expected

    response = (
        await tile38.intersects(key).object(Feature(**featurePolygon)).asObjects()
    )

    assert response.ok
    assert response.objects[0].dict() == expected

    response = await tile38.intersects(key).object(featurePolygon).asObjects()

    assert response.ok
    assert response.objects[0].dict() == expected

    with pytest.raises(Pyle38BadObjectInputError):
        response = (
            await tile38.intersects(key)
            .object({
                "type": "Point",
                "coordinates": [1, 1],
            })
            .asObjects()
        )


@pytest.mark.asyncio
async def test_command_intersects_hash(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).hash("u3390").asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_intersects_quadkey(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).quadkey("120").asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_intersects_tile(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).tile(2200, 1348, 12).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_intersects_sector(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = (
        await tile38.intersects(key)
        .sector(52.25191, 13.37230, 1000, 180, 270)
        .asObjects()
    )
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_intersects_bounds(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = (
        await tile38.intersects(key).bounds(52.24, 13.36, 52.256, 13.379).asObjects()
    )
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_intersects_object_with_intersection(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()

    response = await tile38.set(key, oid).object(polygon).exec()
    assert response.ok

    intersecting_feature = {
        "type": "Polygon",
        "coordinates": [
            [
                [13.374652862548828, 52.24398904962714],
                [13.38357925415039, 52.24398904962714],
                [13.38357925415039, 52.24987472405909],
                [13.374652862548828, 52.24987472405909],
                [13.374652862548828, 52.24398904962714],
            ]
        ],
    }

    response = await tile38.intersects(key).object(intersecting_feature).asObjects()

    assert response.ok
    assert response.objects[0].dict() == {"id": oid, "object": polygon}


@pytest.mark.asyncio
async def test_command_intersects_get(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    oid2 = random_string()

    response = await tile38.set(key, oid).object(polygon).exec()
    assert response.ok

    intersecting_feature = {
        "type": "Polygon",
        "coordinates": [
            [
                [13.374652862548828, 52.24398904962714],
                [13.38357925415039, 52.24398904962714],
                [13.38357925415039, 52.24987472405909],
                [13.374652862548828, 52.24987472405909],
                [13.374652862548828, 52.24398904962714],
            ]
        ],
    }

    response = await tile38.set(key, oid2).object(intersecting_feature).exec()
    assert response.ok

    response = await tile38.intersects(key).get(key, oid2).asObjects()

    assert response.ok
    assert response.objects[0].dict() == {"id": oid, "object": polygon}


@pytest.mark.asyncio
async def test_command_intersects_return_points(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).circle(52.25, 13.37, 100).asPoints()
    assert response.ok
    assert response.points[0].dict() == {
        "id": oid,
        "point": {"lat": 52.25, "lon": 13.37},
    }


@pytest.mark.asyncio
async def test_command_intersects_return_ids(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).circle(52.25, 13.37, 100).asIds()
    assert response.ok
    assert response.ids == [oid]


@pytest.mark.asyncio
async def test_command_intersects_return_count(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).circle(52.25, 13.37, 100).asCount()
    assert response.ok
    assert response.count == 1


@pytest.mark.asyncio
async def test_command_intersects_return_hashes(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).circle(52.25, 13.37, 100).asHashes(5)
    assert response.ok
    assert response.hashes[0].dict() == {"id": oid, "hash": "u3390"}


@pytest.mark.asyncio
async def test_command_intersects_return_bounds(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.intersects(key).circle(52.25, 13.37, 100).asBounds()
    assert response.ok
    assert response.bounds[0].dict() == {
        "id": oid,
        "bounds": {
            "ne": {"lat": 52.25, "lon": 13.37},
            "sw": {"lat": 52.25, "lon": 13.37},
        },
    }


@pytest.mark.asyncio
async def test_command_intersects_buffer_return_count(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    search_area = {
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

    response = await tile38.intersects(key).object(search_area).asCount()
    assert response.ok
    assert response.count == 0

    response = await tile38.intersects(key).buffer(10).object(search_area).asCount()
    assert response.ok
    assert response.count == 1
