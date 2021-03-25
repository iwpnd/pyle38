import pytest

from pyle38 import Client
from pyle38.errors import Tile38IdNotFoundError
from pyle38.errors import Tile38KeyNotFoundError

# from pyle38.errors import Tile38Error

TILE38_URI = "redis://localhost:9851"

# try fixture that yields redis


@pytest.mark.asyncio
async def test_client():
    client = Client(TILE38_URI)
    await client.command("SET", ["fleet", "truck", "POINT", 1, 1])

    response = await client.command("GET", ["fleet", "truck"])

    assert response["ok"]


@pytest.mark.asyncio
async def test_client_exceptions():
    client = Client(TILE38_URI)
    with pytest.raises(Tile38IdNotFoundError):
        await client.command("GET", ["fleet", "Scooter"])

    with pytest.raises(Tile38KeyNotFoundError):
        await client.command("GET", ["vehicles", "Scooter"])


@pytest.mark.asyncio
async def test_client_quit():
    client = Client(TILE38_URI)
    response = await client.quit()

    assert response == "OK"
