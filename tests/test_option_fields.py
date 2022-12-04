import pytest

from .helper.random_data import random_point_feature, random_string

key = random_string()
id = random_string()
fields = {"speed": 100, "state": 1}
feature = random_point_feature(
    {"type": "Point", "coordinates": [13.37, 52.25]}, {"id": id}
)


@pytest.mark.asyncio
async def test_option_fields_in_objects(tile38):
    response = await tile38.set(key, id).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asObjects()
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.objects[0] == {"id": id, "object": feature, "fields": [100, 1]}


@pytest.mark.asyncio
async def test_option_fields_in_hashes(tile38):
    response = await tile38.set(key, id).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asHashes(5)
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.hashes[0].dict() == {"id": id, "hash": "u3390", "fields": [100, 1]}


@pytest.mark.asyncio
async def test_option_fields_in_bounds(tile38):
    response = await tile38.set(key, id).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asBounds()
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.bounds[0].dict() == {
        "id": id,
        "bounds": {
            "ne": {"lat": 52.25, "lon": 13.37},
            "sw": {"lat": 52.25, "lon": 13.37},
        },
        "fields": [100, 1],
    }


@pytest.mark.asyncio
async def test_option_fields_in_points(tile38):
    response = await tile38.set(key, id).fields(fields).object(feature).exec()
    assert response.ok

    response = await tile38.within(key).circle(52.25, 13.37, 100).asPoints()
    assert response.ok
    assert response.fields == ["speed", "state"]
    assert response.points[0].dict() == {
        "id": id,
        "point": {"lat": 52.25, "lon": 13.37},
        "fields": [100, 1],
    }
