import pytest

from .helper.random_data import random_string

key = random_string()
id = random_string()


@pytest.mark.asyncio
async def test_command_exists(tile38):
    key = random_string()
    id = random_string()

    await tile38.set(key, id).point(1, 1).exec()

    received = await tile38.exists(key, id)
    assert received.exists

    received = await tile38.exists(key, "does_not_exist")
    assert not received.exists
