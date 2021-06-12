from time import sleep

import pytest


@pytest.mark.asyncio
async def test_command_bounds(tile38_with_follower):
    tile38 = tile38_with_follower
    key = "fleet"
    id = "truck"

    await tile38.set(key, id).point(1, 1).exec()

    expected = {
        "ok": True,
        "elapsed": "1 ms",
        "bounds": {
            "type": "Polygon",
            "coordinates": [
                [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
            ],
        },
    }

    sleep(0.5)

    received = await tile38.bounds(key)
    assert expected["bounds"] == received.bounds

    received = await tile38.follower().bounds(key)
    assert expected["bounds"] == received.bounds
