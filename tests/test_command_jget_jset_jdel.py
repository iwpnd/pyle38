import pytest


@pytest.mark.asyncio
async def test_command_jset_jget_jdel(tile38_with_follower):
    tile38 = tile38_with_follower

    response = await tile38.jset(key="user", id="901", path="name", value="Tom")
    assert response.ok

    response = await tile38.jget("user", "901")
    assert response.ok
    assert response.value == '{"name":"Tom"}'

    response = await tile38.follower().jget("user", "901")
    assert response.ok
    assert response.value == '{"name":"Tom"}'

    response = await tile38.jdel("user", "901", "name")
    assert response.ok

    response = await tile38.jget("user", "901", "name")
    assert response.ok
    assert response.value == "{}"


@pytest.mark.asyncio
async def test_command_j_options(tile38):
    obj = {"type": "LineString", "coordinates": [[0, 0], [1, 1]]}

    response = await tile38.set("linestring", "1").object(obj).exec()
    assert response.ok

    response = await tile38.get("linestring", "1").asObject()
    assert response.ok
    assert response.object == obj

    response = await tile38.jset("linestring", "1", "coordinates.-1", "[2,2]", "RAW")
    assert response.ok

    response = await tile38.jget("linestring", "1")
    response.ok
    response.value == '{"type":"LineString","coordinates":[[0,0],[1,1],[2,2]]}'

    # TODO: test for raise Tile38Error on deleted key
