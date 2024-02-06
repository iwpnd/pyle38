import os

import pytest

from pyle38 import Tile38
from pyle38.client import Client
from pyle38.errors import Tile38Error, Tile38IdNotFoundError, Tile38KeyNotFoundError


@pytest.mark.asyncio
async def test_client():
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
    response = await client.command("SET", ["fleet", "truck", "POINT", 1, 1])
    assert response["ok"]

    response = await client.command("GET", ["fleet", "truck"])
    assert response["ok"]

    await client.quit()


@pytest.mark.asyncio
async def test_client_exceptions():
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
    with pytest.raises(Tile38Error):
        await client.command("BLA")
    with pytest.raises(Tile38IdNotFoundError):
        await client.command("GET", ["fleet", "Scooter"])

    with pytest.raises(Tile38KeyNotFoundError):
        await client.command("GET", ["vehicles", "Scooter"])

    await client.quit()


@pytest.mark.asyncio
async def test_client_empty_uri():
    with pytest.raises(Tile38Error):
        client = Tile38("")
        await client.get("BLA", "BLA").asObject()


@pytest.mark.asyncio
async def test_no_follower_set():
    with pytest.raises(Tile38Error):
        client = Tile38(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
        await client.follower().get("BLA", "BLA").asObject()


@pytest.mark.asyncio
async def test_client_quit():
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
    response = await client.quit()

    assert response == "OK"
