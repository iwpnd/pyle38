import pytest

from pyle38.errors import Tile38KeyNotFoundError

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_del(tile38):
    key = random_string()
    id = random_string()

    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.delete(key, id)
    assert response.ok

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.get(key, id).asObject()
