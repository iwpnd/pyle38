import pytest

from pyle38.commands.setchan import SetChan
from pyle38.errors import Tile38Error

key = "fleet"
name = "warehouse"
meta = {"city": "Berlin"}


@pytest.mark.asyncio
async def test_command_setchan_compile_within(tile38):
    received = (
        SetChan(tile38.client, name)
        .meta(meta)
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
            "city",
            "Berlin",
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
async def test_command_Sethook_compile_nearby(tile38):

    received = (
        SetChan(tile38.client, name).intersects(key).circle(52.25, 13.37, 100).compile()
    )

    assert received == [
        "SETCHAN",
        [name, "INTERSECTS", key, "FENCE", "CIRCLE", 52.25, 13.37, 100.0],
    ]


@pytest.mark.asyncio
async def test_command_setchan_compile_nearby(tile38):

    received = (
        SetChan(tile38.client, name).nearby(key).point(52.25, 13.37, 100).compile()
    )

    assert received == [
        "SETCHAN",
        [name, "NEARBY", key, "FENCE", "POINT", 52.25, 13.37, 100.0],
    ]


@pytest.mark.asyncio
async def test_command_setchan(tile38):
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
async def test_command_setchan_raises(tile38):

    with pytest.raises(Tile38Error):
        await tile38.within(key).circle(52.25, 13.37, 100).activate()

    with pytest.raises(Tile38Error):
        await tile38.intersects(key).circle(52.25, 13.37, 100).activate()

    with pytest.raises(Tile38Error):
        await tile38.nearby(key).point(52.25, 13.37, 100).activate()


@pytest.mark.asyncio
async def test_command_pdelhook(tile38):
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
async def test_command_delhook(tile38):
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
