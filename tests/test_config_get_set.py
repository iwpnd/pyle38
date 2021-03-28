import pytest


@pytest.mark.asyncio
async def test_config_get_set(tile38):

    response = await tile38.config_set("keepalive", 500)
    assert response.ok

    response = await tile38.config_rewrite()
    assert response.ok

    config_keepalive = await tile38.config_get("keepalive")
    assert config_keepalive.properties["keepalive"] == 500
