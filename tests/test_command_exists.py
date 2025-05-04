import pytest

from pyle38 import Tile38

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_exists(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()

    await tile38.set(key, oid).point(1, 1).exec()

    received = await tile38.exists(key, oid)
    assert received.exists

    received = await tile38.exists(key, "does_not_exist")
    assert not received.exists
