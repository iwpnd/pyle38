import pytest

from pyle38.commands.nearby import Nearby

key = "fleet"
id = "truck"
feature = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [13.37, 52.25]},
    "properties": {"id": id},
}

expected = {"id": id, "object": feature}


@pytest.mark.parametrize(
    "format, precision, expected",
    [
        (
            "OBJECTS",
            None,
            [
                "NEARBY",
                [
                    key,
                    "MATCH",
                    "*",
                    "NOFIELDS",
                    "DISTANCE",
                    "CURSOR",
                    0,
                    "LIMIT",
                    10,
                    "FENCE",
                    "DETECT",
                    "enter,exit",
                    "COMMANDS",
                    "del,set",
                    "POINT",
                    1.0,
                    1.0,
                    100,
                ],
            ],
        )
    ],
    ids=["OBJECTS"],
)
@pytest.mark.asyncio
async def test_command_nearby_compile(tile38, format, precision, expected):
    query = (
        Nearby(tile38.client, key)
        .match("*")
        .nofields()
        .distance()
        .cursor(0)
        .limit(10)
        .fence()
        .detect(["enter", "exit"])
        .commands(["del", "set"])
        .point(1, 1, 100)
    )

    received = query.output(format, precision).compile()

    assert expected == received


@pytest.mark.asyncio
async def test_command_nearby_point(tile38):
    response = await tile38.set(key, id).object(feature).exec()
    assert response.ok

    response = await tile38.nearby(key).point(52.250212, 13.370871).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected


@pytest.mark.asyncio
async def test_command_nearby_point_with_radius(tile38):
    response = await tile38.set(key, id).object(feature).exec()
    assert response.ok

    response = await tile38.nearby(key).point(52.250212, 13.370871, 10).asObjects()
    assert response.ok
    assert len(response.objects) == 0
