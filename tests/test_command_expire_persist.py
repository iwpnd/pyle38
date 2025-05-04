import pytest

from pyle38 import Tile38

from .helper.random_data import random_integer, random_polygon_geometry, random_string


@pytest.mark.asyncio
async def test_command_expire_persist(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    obj = random_polygon_geometry()
    expire = random_integer(10, 100)

    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    response = await tile38.ttl(key, oid)
    assert response.ok
    assert response.ttl == -1

    response = await tile38.expire(key, oid, expire)
    assert response.ok

    response = await tile38.ttl(key, oid)
    assert response.ok
    assert response.ttl < expire

    response = await tile38.persist(key, oid)
    assert response.ok

    response = await tile38.ttl(key, oid)
    assert response.ok
    assert response.ttl == -1
