import pytest


@pytest.mark.asyncio
async def test_command_config(tile38_with_follower):

    tile38 = tile38_with_follower

    response = await tile38.config_set("keepalive", 500)
    assert response.ok

    response = await tile38.follower().config_set("keepalive", 500)
    assert response.ok

    response = await tile38.config_rewrite()
    assert response.ok
    response = await tile38.follower().config_rewrite()
    assert response.ok

    config_keepalive = await tile38.config_get("keepalive")
    assert config_keepalive.properties["keepalive"] == 500
    config_keepalive = await tile38.follower().config_get("keepalive")
    assert config_keepalive.properties["keepalive"] == 500
