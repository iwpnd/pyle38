import pytest

from pyle38 import Tile38
from pyle38.commands.fget import Fget

from .helper.random_data import random_integer, random_point_feature, random_string


@pytest.mark.asyncio
async def test_command_fget_compile(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    field = random_string()

    received = Fget(tile38.client, key, oid, field).compile()
    expected = ["FGET", [key, oid, field]]

    assert received == expected


@pytest.mark.asyncio
async def test_command_fget(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 100)
    fields = {fkey: fvalue}
    obj = random_point_feature()

    # Set an object with fields
    response = await tile38.set(key, oid).fields(fields).object(obj).exec()
    assert response.ok

    # Get the field value using FGET
    response = await tile38.fget(key, oid, fkey).exec()
    assert response.ok
    assert response.value == fvalue


@pytest.mark.asyncio
async def test_command_fget_string_value(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = random_string()
    fields = {fkey: fvalue}
    obj = random_point_feature()

    # Set an object with string field
    response = await tile38.set(key, oid).fields(fields).object(obj).exec()
    assert response.ok

    # Get the field value using FGET
    response = await tile38.fget(key, oid, fkey).exec()
    assert response.ok
    assert response.value == fvalue


@pytest.mark.asyncio
async def test_command_fget_nonexistent_field(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    obj = random_point_feature()

    # Set an object without fields
    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    # Try to get a field that doesn't exist
    response = await tile38.fget(key, oid, fkey).exec()
    assert response.ok
    # According to Tile38 docs, it should return 0 for non-existent fields
    assert response.value == 0


@pytest.mark.asyncio
async def test_command_fget_after_fset(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    fkey = random_string()
    fvalue = random_integer(1, 100)
    fields = {fkey: fvalue}
    obj = random_point_feature()

    # Set an object first
    response = await tile38.set(key, oid).object(obj).exec()
    assert response.ok

    # Use FSET to set a field
    response = await tile38.fset(key, oid, fields).exec()
    assert response.ok

    # Use FGET to retrieve the field
    response = await tile38.fget(key, oid, fkey).exec()
    assert response.ok
    assert response.value == fvalue

