import pytest

from pyle38.errors import Tile38IdNotFoundError, Tile38KeyNotFoundError

key = "fleet"
id = "truck1"


@pytest.mark.asyncio
async def test_command_pdel(tile38):
    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.get(key, id).asObject()
    assert response.ok
    assert response.object["type"] == "Point"

    response = await tile38.pdel(key, "tr*")
    assert response.ok

    with pytest.raises(Tile38KeyNotFoundError):
        await tile38.get(key, id).asObject()

    await tile38.set(key, "truck1").point(1, 1).exec()
    await tile38.set(key, "bus1").point(1, 2).exec()

    await tile38.pdel(key, "t*")

    with pytest.raises(Tile38IdNotFoundError):
        await tile38.get(key, "truck1").asObject()
