import pytest

from pyle38 import Tile38
from pyle38.commands.scan import Scan

from .helper.random_data import random_string

key = random_string()
oid = random_string()
feature = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [13.37, 52.25]},
    "properties": {"id": oid},
}

expected = {"id": oid, "object": feature}


@pytest.mark.asyncio
async def test_command_scan_compile(tile38: Tile38) -> None:
    query = (
        Scan(tile38.client, key)
        .match("*")
        .nofields()
        .sparse(1)
        .asc()
        .cursor(0)
        .limit(10)
    )

    received = query.output("OBJECTS").compile()

    assert received == [
        "SCAN",
        [key, "MATCH", "*", "NOFIELDS", "SPARSE", 1, "ASC", "CURSOR", 0, "LIMIT", 10],
    ]

    query = (
        Scan(tile38.client, key)
        .match("*")
        .nofields()
        .sparse(1)
        .desc()
        .cursor(0)
        .limit(10)
    )

    received = query.output("OBJECTS").compile()

    assert received == [
        "SCAN",
        [key, "MATCH", "*", "NOFIELDS", "SPARSE", 1, "DESC", "CURSOR", 0, "LIMIT", 10],
    ]

    query = (
        Scan(tile38.client, key)
        .match("*")
        .nofields()
        .sparse(1)
        .desc()
        .cursor(0)
        .limit(10)
        .where("foo", 1, 1)
        .where("bar", 1, 1)
        .wherein("foo", [1])
        .wherein("bar", [1])
    )

    received = query.output("OBJECTS").compile()

    assert received == [
        "SCAN",
        [
            key,
            "MATCH",
            "*",
            "NOFIELDS",
            "SPARSE",
            1,
            "DESC",
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
        ],
    ]


@pytest.mark.asyncio
async def test_command_scan(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_scan_wherein(tile38: Tile38) -> None:
    await (
        tile38
        .set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .object(feature)
        .exec()
    )
    await (
        tile38
        .set(key, "truck1")
        .fields({"maxspeed": 100, "maxweight": 1000})
        .object(feature)
        .exec()
    )

    response = await tile38.scan(key).wherein("maxspeed", [120]).asObjects()
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120, 1000]})

    response = (
        await tile38
        .scan(key)
        .wherein("maxspeed", [100, 120])
        .wherein("maxweight", [1000])
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_scan_where(tile38: Tile38) -> None:
    await (
        tile38
        .set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .object(feature)
        .exec()
    )
    await (
        tile38
        .set(key, "truck1")
        .fields({"maxspeed": 100, "maxweight": 1000})
        .object(feature)
        .exec()
    )

    response = await tile38.scan(key).where("maxspeed", 120, 120).asObjects()
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120, 1000]})

    response = (
        await tile38
        .scan(key)
        .where("maxspeed", 100, 120)
        .where("maxweight", 1000, 1000)
        .asObjects()
    )
    assert response.ok
    assert len(response.objects) == 2


@pytest.mark.asyncio
async def test_command_scan_return_points(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asPoints()
    assert response.ok
    assert response.points[0].dict() == {
        "id": oid,
        "point": {"lat": 52.25, "lon": 13.37},
    }


@pytest.mark.asyncio
async def test_command_scan_return_ids(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asIds()
    assert response.ok
    assert response.ids == [oid]


@pytest.mark.asyncio
async def test_command_scan_return_count(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asCount()
    assert response.ok
    assert response.count == 1


@pytest.mark.asyncio
async def test_command_scan_return_hashes(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asHashes(5)
    assert response.ok
    assert response.hashes[0].dict() == {"id": oid, "hash": "u3390"}


@pytest.mark.asyncio
async def test_command_scan_return_bounds(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asBounds()
    assert response.ok
    assert response.bounds[0].dict() == {
        "id": oid,
        "bounds": {
            "ne": {"lat": 52.25, "lon": 13.37},
            "sw": {"lat": 52.25, "lon": 13.37},
        },
    }
