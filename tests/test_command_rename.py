import pytest

from pyle38.errors import Tile38KeyNotFoundError

key = "fleet"
newkey = "fl33t"
id = "truck"


@pytest.mark.asyncio
async def test_command_rename(tile38):
    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.rename(key, newkey)
    assert response.ok

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.get(key, id).asObject()


@pytest.mark.asyncio
async def test_command_renamex(tile38):
    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.set(newkey, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.rename(key, newkey, nx=True)
    assert response.ok

    response = await tile38.get(key, id).asObject()
    assert response.ok

    response = await tile38.get(newkey, id).asObject()
    assert response.ok
