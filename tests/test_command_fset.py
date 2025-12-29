import pytest

from pyle38 import Tile38
from pyle38.commands.fset import FSet

from .helper.random_data import random_integer, random_point_feature, random_string


@pytest.mark.asyncio
async def test_command_fset_compile(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 10)
    fields = {fkey: fvalue}

    received = FSet(tile38.client, key, oid, fields).compile()
    expected = ["FSET", [key, oid, fkey, fvalue]]

    assert received == expected


@pytest.mark.asyncio
async def test_command_fset(tile38: Tile38) -> None:
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


@pytest.mark.asyncio
async def test_command_fset_expr(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = {random_string(): random_integer(1, 10)}
    fields = {fkey: fvalue}
    obj = random_point_feature()

    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    response = await tile38.fset(key, oid, fields).xx().exec()
    assert response.ok

    response = await tile38.get(key, oid).withfields().asObject()
    assert response.ok
    assert response.fields == fields


@pytest.mark.asyncio
async def test_command_fset_zero_deletes_field(tile38: Tile38) -> None:
    """
    ZeroValue fields are treated as non-existent in the tile38 field value context.
    """
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = {random_string(): random_integer(1, 10)}
    fields = {fkey: fvalue}
    obj = random_point_feature()

    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    response = await tile38.fset(key, oid, fields).xx().exec()
    assert response.ok

    response = await tile38.get(key, oid).withfields().asObject()
    assert response.ok
    assert response.fields == fields

    response = await tile38.fset(key, oid, {fkey: 0}).xx().exec()
    assert response.ok

    response = await tile38.fexists(key, oid, fkey)
    response.exists = False
