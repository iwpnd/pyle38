import pytest

from pyle38 import Tile38
from pyle38.errors import Tile38KeyNotFoundError

from .helper.random_data import random_latitude, random_longitude, random_string


@pytest.mark.asyncio
async def test_command_rename(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    newkey = random_string()
    lat = random_latitude()
    lon = random_longitude()

    response = await tile38.set(key, oid).point(lat, lon).exec()
    assert response.ok

    response = await tile38.rename(key, newkey)
    assert response.ok

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.get(key, oid).asObject()


@pytest.mark.asyncio
async def test_command_renamex(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    newkey = random_string()
    lat = random_latitude()
    lon = random_longitude()

    response = await tile38.set(key, oid).point(lat, lon).exec()
    assert response.ok

    response = await tile38.set(newkey, oid).point(lat, lon).exec()
    assert response.ok

    response = await tile38.rename(key, newkey, nx=True)
    assert response.ok

    response = await tile38.get(key, oid).asObject()
    assert response.ok

    response = await tile38.get(newkey, oid).asObject()
    assert response.ok
