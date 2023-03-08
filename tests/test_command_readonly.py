import pytest

from pyle38.errors import Tile38Error

from .helper.random_data import random_latitude, random_longitude, random_string


@pytest.mark.asyncio
# @pytest.mark.skip(reason="causes issues with consecutive tests")
async def test_command_readonly(tile38):
    key = random_string()
    id = random_string()
    lat = random_latitude()
    lon = random_longitude()

    response = await tile38.set(key, id).point(lat, lon).exec()
    assert response.ok

    response = await tile38.readonly()
    assert response.ok

    with pytest.raises(Tile38Error):
        await tile38.set(key, id).point(lat, lon).exec()

    response = await tile38.readonly(value=False)
    assert response.ok

    response = await tile38.server_extended()
    assert response.ok
    assert response.stats.tile38_read_only is False

    response.ok = await tile38.set(key, id).point(lat, lon).exec()
    assert response.ok
