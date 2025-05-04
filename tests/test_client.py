import os

import pytest

from pyle38 import Tile38
from pyle38.client import (
    Client,
)
from pyle38.client_options import WithRetryExponentialBackoff, WithRetryOnError
from pyle38.errors import (
    Pyle38ConnectionError,
    Pyle38NoFollowerSetError,
    Pyle38NoLeaderSetError,
    Pyle38TimeoutError,
    Tile38Error,
    Tile38IdNotFoundError,
    Tile38KeyNotFoundError,
)


@pytest.mark.asyncio
async def test_client_options() -> None:
    url = os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851"
    client_options = [
        WithRetryExponentialBackoff(10),
        WithRetryOnError(Pyle38TimeoutError, Pyle38ConnectionError),
    ]
    client = Client(url, client_options)

    assert client.url == url

    opts = client.client_options()
    assert opts["retry"]  # pyright: ignore[reportTypedDictNotRequiredAccess]
    assert type(opts["retry_on_error"]) is list  # pyright: ignore[reportTypedDictNotRequiredAccess]
    assert opts["retry_on_error"] == [Pyle38TimeoutError, Pyle38ConnectionError]  # pyright: ignore[reportTypedDictNotRequiredAccess]

    response = await client.command("SET", ["fleet", "truck", "POINT", 1, 1])  # type: ignore[arg-type]
    assert response["ok"]

    response = await client.command("GET", ["fleet", "truck"])
    assert response["ok"]

    await client.quit()


@pytest.mark.asyncio
async def test_client() -> None:
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
    response = await client.command("SET", ["fleet", "truck", "POINT", 1, 1])  # type: ignore[arg-type]
    assert response["ok"]

    response = await client.command("GET", ["fleet", "truck"])
    assert response["ok"]

    await client.quit()


@pytest.mark.asyncio
async def test_client_exceptions() -> None:
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
    with pytest.raises(Tile38Error):
        await client.command("BLA")
    with pytest.raises(Tile38IdNotFoundError):
        await client.command("GET", ["fleet", "Scooter"])

    with pytest.raises(Tile38KeyNotFoundError):
        await client.command("GET", ["vehicles", "Scooter"])

    await client.quit()


@pytest.mark.asyncio
async def test_client_empty_uri() -> None:
    with pytest.raises(Pyle38NoLeaderSetError):
        client = Tile38("")
        await client.get("BLA", "BLA").asObject()


@pytest.mark.asyncio
async def test_no_follower_set() -> None:
    with pytest.raises(Pyle38NoFollowerSetError):
        client = Tile38(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
        await client.follower().get("BLA", "BLA").asObject()


@pytest.mark.asyncio
async def test_client_quit() -> None:
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")
    response = await client.quit()

    assert response == "OK"


@pytest.mark.asyncio
async def test_client_handles_disconnection() -> None:
    client = Client(os.getenv("TILE38_LEADER_URI") or "redis://localhost:9851")

    response = await client.command("SET", ["fleet", "truck", "POINT", 1, 1])  # type: ignore[arg-type]
    assert response["ok"]

    quit_response = await client.quit()
    assert quit_response == "OK"

    response = await client.command("SET", ["fleet", "truck", "POINT", 1, 1])  # type: ignore[arg-type]
    assert response["ok"]

    quit_response = await client.quit()
    assert quit_response == "OK"
