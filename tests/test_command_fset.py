import pytest

from pyle38.commands.fset import Fset

from .helper.random_data import random_feature, random_integer, random_string


@pytest.mark.asyncio
async def test_command_fset_compile(tile38):
    key = random_string()
    id = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 10)
    fields = {fkey: fvalue}

    received = Fset(tile38.client, key, id, fields).compile()
    expected = ["FSET", [key, id, fkey, fvalue]]

    assert received == expected


@pytest.mark.asyncio
async def test_command_fset(tile38):
    key = random_string()
    id = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 10)
    fields = {fkey: fvalue}
    object = random_feature("Point")

    response = await tile38.set(key, id).object(object).exec()
    assert response.ok

    response = await tile38.fset(key, id, fields).xx().exec()
    assert response.ok

    response = await tile38.get(key, id).withfields().asObject()
    assert response.ok
    assert response.fields == fields
