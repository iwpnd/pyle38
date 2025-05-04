import pytest

from pyle38 import Tile38

from .helper.random_data import random_point_feature, random_string

key = random_string()
oid = random_string()
fields = {"speed": 100, "state": 1}
feature = random_point_feature(
    {"type": "Point", "coordinates": [13.37, 52.25]}, {"id": oid}
)


@pytest.mark.asyncio
async def test_option_fields_in_objects(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asObjects()
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.objects[0].dict() == {
        "id": oid,
        "object": feature,
        "fields": [100, 1],
    }


@pytest.mark.asyncio
async def test_option_fields_in_hashes(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asHashes(5)
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.hashes[0].dict() == {"id": oid, "hash": "u3390", "fields": [100, 1]}


@pytest.mark.asyncio
async def test_option_fields_in_bounds(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asBounds()
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.bounds[0].dict() == {
        "id": oid,
        "bounds": {
            "ne": {"lat": 52.25, "lon": 13.37},
            "sw": {"lat": 52.25, "lon": 13.37},
        },
        "fields": [100, 1],
    }


@pytest.mark.asyncio
async def test_option_fields_in_points(tile38: Tile38) -> None:
    response = await tile38.set(key, oid).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asPoints()
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.points[0].dict() == {
        "id": oid,
        "point": {"lat": 52.25, "lon": 13.37},
        "fields": [100, 1],
    }
