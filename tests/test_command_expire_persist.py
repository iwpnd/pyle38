import pytest

from .helper.random_data import random_integer, random_polygon_geometry, random_string


@pytest.mark.asyncio
async def test_command_expire_persist(tile38):
    key = random_string()
    id = random_string()
    object = random_polygon_geometry()
    expire = random_integer(10, 100)

    response = await tile38.set(key, id).object(object).exec()
    assert response.ok

    response = await tile38.ttl(key, id)
    assert response.ok
    assert response.ttl == -1

    response = await tile38.expire(key, id, expire)
    assert response.ok

    response = await tile38.ttl(key, id)
    assert response.ok
    assert response.ttl < expire

    response = await tile38.persist(key, id)
    assert response.ok

    response = await tile38.ttl(key, id)
    assert response.ok
    assert response.ttl == -1
