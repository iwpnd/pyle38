import pytest

key = "fleet"
id = "truck"
expire = 5


@pytest.mark.asyncio
async def test_command_ttl(tile38):
    response = await tile38.set(key, id).ex(5).point(1, 1).exec()
    assert response.ok

    response = await tile38.ttl(key, id)
    assert response.ok
    assert response.ttl < expire
