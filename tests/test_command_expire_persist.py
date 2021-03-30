import pytest

key = "fleet"
id = "truck"
expire = 10


@pytest.mark.asyncio
async def test_command_expire_persist(tile38):
    response = await tile38.set(key, id).point(1, 1).exec()
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
