import pytest

from pyle38 import Tile38

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_fexists(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    field = random_string()
    value = random_string()

    await tile38.set(key, oid).fields({field: value}).point(1, 1).exec()

    received = await tile38.fexists(key, oid, field)
    assert received.exists

    received = await tile38.fexists(key, oid, "does_not_exist")
    assert not received.exists
