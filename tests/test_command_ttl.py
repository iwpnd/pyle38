import pytest

from pyle38 import Tile38

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_ttl(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    expire_in = 5

    response = await tile38.set(key, oid).ex(expire_in).point(1, 1).exec()
    assert response.ok

    response = await tile38.ttl(key, oid)
    assert response.ok
    assert response.ttl < expire_in
