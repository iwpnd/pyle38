import pytest

from pyle38.commands.search import Search

key = "fleet"
id = "truck:driver"
string = "JC Denton"

expected = {"id": id, "object": string}


@pytest.mark.parametrize(
    "format, expected",
    [("OBJECTS", ["SEARCH", [key, "MATCH", "J*", "ASC", "CURSOR", 0, "LIMIT", 10]])],
    ids=["OBJECTS"],
)
@pytest.mark.asyncio
async def test_command_search_compile(tile38, format, expected):
    query = Search(tile38.client, key).match("J*").asc().cursor(0).limit(10)

    received = query.output(format).compile()

    assert expected == received


@pytest.mark.asyncio
async def test_command_search(tile38):
    response = await tile38.set(key, id).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match("J*").asStringObjects()
    assert response.ok
    assert response.objects[0].dict() == expected
