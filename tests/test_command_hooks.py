import pytest


@pytest.mark.asyncio
async def test_command_hooks(tile38):

    # TODO: test after tile38.set_hook
    response = await tile38.hooks()

    assert response.ok

    response = await tile38.follower().hooks()

    assert response.ok
