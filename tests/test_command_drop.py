import pytest

from pyle38 import Tile38
from pyle38.errors import Tile38KeyNotFoundError

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_drop(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()

    response = await tile38.set(key, oid).point(1, 1).exec()
    assert response.ok

    response = await tile38.drop(key)
    assert response.ok

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.get(key, oid).asObject()
