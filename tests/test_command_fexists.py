import pytest

from .helper.random_data import random_string

key = random_string()
id = random_string()


@pytest.mark.asyncio
async def test_command_fexists(tile38):
    key = random_string()
    id = random_string()
    field = random_string()
    value = random_string()

    await tile38.set(key, id).fields({field: value}).point(1, 1).exec()

    received = await tile38.fexists(key, id, field)
    assert received.exists

    received = await tile38.fexists(key, id, "does_not_exist")
    assert not received.exists
