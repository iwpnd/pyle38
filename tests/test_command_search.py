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


@pytest.mark.asyncio
async def test_command_search_returns_stringobjects(tile38):
    response = await tile38.set(key, id).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match("J*").asStringObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


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
