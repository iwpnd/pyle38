import pytest

from pyle38 import Tile38
from pyle38.commands.fget import FGet
from pyle38.errors import Tile38FieldNotFoundError

from .helper.random_data import random_integer, random_point_feature, random_string


@pytest.mark.asyncio
async def test_command_fget_compile(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()

    received = FGet(tile38.client, key, oid, fkey).compile()
    expected = ["FGET", [key, oid, fkey]]

    assert received == expected


@pytest.mark.asyncio
async def test_command_fget(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 10)
    fields = {fkey: fvalue}
    obj = random_point_feature()

    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    response = await tile38.fset(key, oid, fields).xx().exec()
    assert response.ok

    response = await tile38.get(key, oid).withfields().asObject()
    assert response.ok
    assert response.fields == fields

    response = await tile38.fget(key, oid, fkey).exec()
    assert response.ok
    assert response.value == fvalue


@pytest.mark.asyncio
async def test_command_fget_raises(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 10)
    fields = {fkey: fvalue}
    obj = random_point_feature()

    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    response = await tile38.fset(key, oid, fields).xx().exec()
    assert response.ok

    response = await tile38.get(key, oid).withfields().asObject()
    assert response.ok
    assert response.fields == fields

    with pytest.raises(Tile38FieldNotFoundError):
        response = await tile38.fget(key, oid, "unknown").exec()
