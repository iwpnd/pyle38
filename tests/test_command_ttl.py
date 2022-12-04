import pytest

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_ttl(tile38):
    key = random_string()
    id = random_string()
    expire_in = 5

    response = await tile38.set(key, id).ex(expire_in).point(1, 1).exec()
    assert response.ok

    response = await tile38.ttl(key, id)
    assert response.ok
    assert response.ttl < expire_in
