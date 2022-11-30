import pytest

from pyle38.errors import Tile38KeyNotFoundError

from .helper.random_data import random_latitude, random_longitude, random_string


@pytest.mark.asyncio
async def test_command_rename(tile38):
    key = random_string()
    id = random_string()
    newkey = random_string()
    lat = random_latitude()
    lon = random_longitude()

    response = await tile38.set(key, id).point(lat, lon).exec()
    assert response.ok

    response = await tile38.rename(key, newkey)
    assert response.ok

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.get(key, id).asObject()


@pytest.mark.asyncio
async def test_command_renamex(tile38):
    key = random_string()
    id = random_string()
    newkey = random_string()
    lat = random_latitude()
    lon = random_longitude()

    response = await tile38.set(key, id).point(lat, lon).exec()
    assert response.ok

    response = await tile38.set(newkey, id).point(lat, lon).exec()
    assert response.ok

    response = await tile38.rename(key, newkey, nx=True)
    assert response.ok

    response = await tile38.get(key, id).asObject()
    assert response.ok

    response = await tile38.get(newkey, id).asObject()
    assert response.ok
