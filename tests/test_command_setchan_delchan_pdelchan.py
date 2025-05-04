import pytest

from pyle38 import Tile38
from pyle38.commands.setchan import SetChan
from pyle38.errors import Pyle38NoHookToActivateError

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_setchan_compile_within(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()
    meta_key = random_string()
    meta_value = random_string()

    received = (
        SetChan(tile38.client, name)
        .meta({meta_key: meta_value})
        .ex(10)
        .within(key)
        .circle(52.25, 13.37, 100)
        .compile()
    )

    assert received == [
        "SETCHAN",
        [
            name,
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
        SetChan(tile38.client, name).intersects(key).circle(52.25, 13.37, 100).compile()
    )

    assert received == [
        "SETCHAN",
        [name, "INTERSECTS", key, "FENCE", "CIRCLE", 52.25, 13.37, 100.0],
    ]


@pytest.mark.asyncio
async def test_command_setchan_compile_nearby(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    received = (
        SetChan(tile38.client, name).nearby(key).point(52.25, 13.37, 100).compile()
    )

    assert received == [
        "SETCHAN",
        [name, "NEARBY", key, "FENCE", "POINT", 52.25, 13.37, 100.0],
    ]


@pytest.mark.asyncio
async def test_command_setchan(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    response = (
        await tile38.setchan(name).within(key).circle(52.25, 13.37, 100).activate()
    )
    assert response.ok

    response = (
        await tile38.setchan(name).intersects(key).circle(52.25, 13.37, 100).activate()
    )
    assert response.ok

    response = (
        await tile38.setchan(name).nearby(key).point(52.25, 13.37, 100).activate()
    )
    assert response.ok


@pytest.mark.asyncio
async def test_command_setchan_raises(tile38: Tile38) -> None:
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
        await tile38.setchan(name).within(key).circle(52.25, 13.37, 100).activate()
    )
    assert response.ok

    response = await tile38.chans()
    assert response.ok
    assert len(response.chans) == 1

    response = await tile38.pdelchan("*")
    assert response.ok

    response = await tile38.chans()
    assert response.ok
    assert len(response.chans) == 0


@pytest.mark.asyncio
async def test_command_delhook(tile38: Tile38) -> None:
    key = random_string()
    name = random_string()

    response = (
        await tile38.setchan(name).within(key).circle(52.25, 13.37, 100).activate()
    )
    assert response.ok

    response = await tile38.chans()
    assert response.ok
    assert len(response.chans) == 1

    response = await tile38.delchan(name)
    assert response.ok

    response = await tile38.chans()
    assert response.ok
    assert len(response.chans) == 0
