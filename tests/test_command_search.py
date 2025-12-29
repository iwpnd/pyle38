import pytest

from pyle38 import Tile38
from pyle38.commands.search import Search

from .helper.random_data import random_string


@pytest.mark.asyncio
async def test_command_search_compile(tile38: Tile38) -> None:
    key = random_string()

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
        .wherein("foo", [1])
        .desc()
        .cursor(0)
        .limit(10)
    )

    received = query.output("OBJECTS").compile()

    assert received == [
        "SEARCH",
        [
            key,
            "MATCH",
            "*",
            "DESC",
            "CURSOR",
            0,
            "LIMIT",
            10,
            "WHERE",
            "foo",
            1,
            1,
            "WHEREIN",
            "foo",
            1,
            1,
        ],
    ]


@pytest.mark.asyncio
async def test_command_search_returns_stringobjects(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    string = random_string()

    pattern = string[:1] + "*"

    response = await tile38.set(key, oid).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match(pattern).asStringObjects()
    assert response.ok
    assert response.objects[0].dict()["object"] == string


@pytest.mark.asyncio
async def test_command_search_returns_where_stringobjects(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    string = random_string()
    pattern = string[:1] + "*"

    await (
        tile38
        .set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .string(string)
        .exec()
    )
    await (
        tile38
        .set(key, random_string())
        .fields({"maxspeed": 100, "maxweight": 1000})
        .string(random_string())
        .exec()
    )

    response = (
        await tile38
        .search(key)
        .where("maxspeed", 120, 120)
        .match(pattern)
        .asStringObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(
        {"id": oid, "object": string}, **{"fields": [120, 1000]}
    )

    response = (
        await tile38
        .search(key)
        .where("maxspeed", 100, 120)
        .where("maxweight", 1000, 1000)
        .match(pattern)
        .asStringObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(
        {"id": oid, "object": string}, **{"fields": [120, 1000]}
    )


@pytest.mark.asyncio
async def test_command_search_returns_wherein_stringobjects(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    string = random_string()
    pattern = string[:1] + "*"

    await (
        tile38
        .set(key, oid)
        .fields({"maxspeed": 120, "maxweight": 1000})
        .string(string)
        .exec()
    )
    await (
        tile38
        .set(key, random_string())
        .fields({"maxspeed": 100, "maxweight": 1000})
        .string(random_string())
        .exec()
    )

    response = (
        await tile38
        .search(key)
        .wherein("maxspeed", [120])
        .match(pattern)
        .asStringObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(
        {"id": oid, "object": string}, **{"fields": [120, 1000]}
    )

    response = (
        await tile38
        .search(key)
        .wherein("maxspeed", [100, 120])
        .wherein("maxweight", [1000])
        .match(pattern)
        .asStringObjects()
    )
    assert response.ok
    assert len(response.objects) == 1
    assert response.objects[0].dict() == dict(
        {"id": oid, "object": string}, **{"fields": [120, 1000]}
    )


@pytest.mark.asyncio
async def test_command_search_returns_ids(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    string = random_string()
    pattern = string[:1] + "*"

    response = await tile38.set(key, oid).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match(pattern).asIds()
    assert response.ok
    assert response.ids == [oid]


@pytest.mark.asyncio
async def test_command_search_returns_count(tile38: Tile38) -> None:
    key = random_string()
    oid = random_string()
    string = random_string()
    pattern = string[:1] + "*"

    response = await tile38.set(key, oid).string(string).exec()
    assert response.ok

    response = await tile38.search(key).match(pattern).asCount()
    assert response.ok
    assert response.count == 1
