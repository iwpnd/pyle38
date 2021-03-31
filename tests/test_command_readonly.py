import pytest

from pyle38.errors import Tile38Error

key = "fleet"
id = "truck"


@pytest.mark.asyncio
async def test_command_readonly(tile38):
    response = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok

    response = await tile38.readonly()
    assert response.ok

    with pytest.raises(Tile38Error):
        await tile38.set(key, id).point(1, 1).exec()

    response = await tile38.readonly(value=False)
    assert response.ok

    response.ok = await tile38.set(key, id).point(1, 1).exec()
    assert response.ok
