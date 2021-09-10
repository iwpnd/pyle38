import pytest

from pyle38.commands.search import Search

key = "fleet"
id = "truck:driver"
string = "JC Denton"

expected = {"id": id, "object": string}


@pytest.mark.asyncio
async def test_command_search_compile(tile38):
    query = Search(tile38.client, key).match("*").asc().cursor(0).limit(10)

    received = query.output("OBJECTS").compile()

    assert received == ["SEARCH", [key, "MATCH", "*", "ASC", "CURSOR", 0, "LIMIT", 10]]

    query = Search(tile38.client, key).match("*").desc().cursor(0).limit(10)

    received = query.output("OBJECTS").compile()

    assert received == ["SEARCH", [key, "MATCH", "*", "DESC", "CURSOR", 0, "LIMIT", 10]]

    query = (
        Search(tile38.client, key)
        .match("*")
        .where("foo", 1, 1)
        .desc()
        .cursor(0)
        .limit(10)
    )

    received = query.output("OBJECTS").compile()

    assert received == [
        "SEARCH",
        [key, "MATCH", "*", "DESC", "CURSOR", 0, "LIMIT", 10, "WHERE", "foo", 1, 1],
    ]


@pytest.mark.asyncio
async def test_command_search_returns_stringobjects(tile38):
    response = await tile38.set(key, id).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match("J*").asStringObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_search_returns_where_stringobjects(tile38):
    await tile38.set(key, id).fields({"maxspeed": 120, "maxweight": 1000}).string(
        string
    ).exec()
    await tile38.set(key, "truck2").fields({"maxspeed": 100, "maxweight": 1000}).string(
        "Max Payne"
    ).exec()

    response = (
        await tile38.search(key)
        .where("maxspeed", 120, 120)
        .match("J*")
        .asStringObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120, 1000]})

    response = (
        await tile38.search(key)
        .where("maxspeed", 100, 120)
        .where("maxweight", 1000, 1000)
        .match("J*")
        .asStringObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(expected, **{"fields": [120, 1000]})


@pytest.mark.asyncio
async def test_command_search_returns_ids(tile38):
    response = await tile38.set(key, id).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match("J*").asIds()
    assert response.ok
    assert response.ids == [id]


@pytest.mark.asyncio
async def test_command_search_returns_count(tile38):
    response = await tile38.set(key, id).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match("J*").asCount()
    assert response.ok
    assert response.count == 1
