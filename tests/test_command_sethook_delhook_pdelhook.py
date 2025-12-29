import pytest

from pyle38 import Tile38
from pyle38.commands.sethook import SetHook
from pyle38.errors import Pyle38NoHookToActivateError

from .helper.random_data import random_string

endpoint = "kafka://10.0.20.78:9092/warehouse"


@pytest.mark.asyncio
async def test_command_sethook_compile_within(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()
    meta_key = random_string()
    meta_value = random_string()

    received = (
        SetHook(tile38.client, name, endpoint)
        .meta({meta_key: meta_value})
        .ex(10)
        .within(key)
        .circle(52.25, 13.37, 100)
        .compile()
    )

    assert received == [
        "SETHOOK",
        [
            name,
            endpoint,
            "META",
            meta_key,
            meta_value,
            "EX",
            10,
            "WITHIN",
            key,
            "FENCE",
            "CIRCLE",
            52.25,
            13.37,
            100.0,
        ],
    ]


@pytest.mark.asyncio
async def test_command_Sethook_compile_nearby(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    received = (
        SetHook(tile38.client, name, endpoint)
        .intersects(key)
        .circle(52.25, 13.37, 100)
        .compile()
    )

    assert received == [
        "SETHOOK",
        [name, endpoint, "INTERSECTS", key, "FENCE", "CIRCLE", 52.25, 13.37, 100.0],
    ]


@pytest.mark.asyncio
async def test_command_sethook_compile_nearby(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    received = (
        SetHook(tile38.client, name, endpoint)
        .nearby(key)
        .point(52.25, 13.37, 100)
        .compile()
    )

    assert received == [
        "SETHOOK",
        [name, endpoint, "NEARBY", key, "FENCE", "POINT", 52.25, 13.37, 100.0],
    ]


@pytest.mark.asyncio
async def test_command_sethook(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    response = (
        await tile38
        .sethook(name, endpoint)
        .within(key)
        .circle(52.25, 13.37, 100)
        .activate()
    )
    assert response.ok

    response = (
        await tile38
        .sethook(name, endpoint)
        .intersects(key)
        .circle(52.25, 13.37, 100)
        .activate()
    )
    assert response.ok

    response = (
        await tile38
        .sethook(name, endpoint)
        .nearby(key)
        .point(52.25, 13.37, 100)
        .activate()
    )
    assert response.ok


@pytest.mark.asyncio
async def test_command_sethook_raises(tile38: Tile38) -> None:
    key = random_string()

    with pytest.raises(Pyle38NoHookToActivateError):
        await tile38.within(key).circle(52.25, 13.37, 100).activate()

    with pytest.raises(Pyle38NoHookToActivateError):
        await tile38.intersects(key).circle(52.25, 13.37, 100).activate()

    with pytest.raises(Pyle38NoHookToActivateError):
        await tile38.nearby(key).point(52.25, 13.37, 100).activate()


@pytest.mark.asyncio
async def test_command_pdelhook(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    response = (
        await tile38
        .sethook(name, endpoint)
        .within(key)
        .circle(52.25, 13.37, 100)
        .activate()
    )
    assert response.ok

    response = await tile38.hooks()
    assert response.ok
    assert len(response.hooks) == 1

    response = await tile38.pdelhook("*")
    assert response.ok

    response = await tile38.hooks()
    assert response.ok
    assert len(response.hooks) == 0


@pytest.mark.asyncio
async def test_command_delhook(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    response = (
        await tile38
        .sethook(name, endpoint)
        .within(key)
        .circle(52.25, 13.37, 100)
        .activate()
    )
    assert response.ok

    response = await tile38.hooks()
    assert response.ok
    assert len(response.hooks) == 1

    response = await tile38.delhook(name)
    assert response.ok

    response = await tile38.hooks()
    assert response.ok
    assert len(response.hooks) == 0
