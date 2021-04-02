import pytest

from pyle38.commands.scan import Scan

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
                "SCAN",
                [
                    key,
                    "MATCH",
                    "*",
                    "NOFIELDS",
                    "SPARSE",
                    1,
                    "ASC",
                    "CURSOR",
                    0,
                    "LIMIT",
                    10,
                ],
            ],
        )
    ],
    ids=["OBJECTS"],
)
@pytest.mark.asyncio
async def test_command_scan_compile(tile38, format, precision, expected):
    query = (
        Scan(tile38.client, key)
        .match("*")
        .nofields()
        .sparse(1)
        .asc()
        .cursor(0)
        .limit(10)
    )

    received = query.output(format, precision).compile()

    assert expected == received


@pytest.mark.asyncio
async def test_command_scan(tile38):
    response = await tile38.set(key, id).object(feature).exec()
    assert response.ok

    response = await tile38.scan(key).asObjects()
    assert response.ok
    assert response.objects[0].dict() == expected
