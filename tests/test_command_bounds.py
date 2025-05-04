import pytest

from pyle38 import Tile38

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_bounds(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()

    response = await tile38.set(key, oid).point(1, 1).exec()
    assert response.ok

    expected = {
        "bounds": {
            "type": "Polygon",
            "coordinates": [
                [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
            ],
        },
    }
    received = await tile38.bounds(key)

    assert received.ok is True
    assert received.bounds.dict() == expected["bounds"]
