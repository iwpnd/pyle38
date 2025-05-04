import random
import uuid
from typing import Any

Position = list[float]
Polygon = list[list[Position]]
BoundingBox = list[float]


def random_string() -> str:
    return str(uuid.uuid4())


def random_integer(minimum: int = 0, maximum: int = 1000) -> int:
    return random.randint(minimum, maximum)  # noqa: S311


def random_float(minimum: float = 0, maximum: float = 1000) -> float:
    return random.uniform(minimum, maximum)  # noqa: S311


def random_longitude(minimum: float = -179.0, maximum: float = 179.0) -> float:
    return random.uniform(minimum, maximum)  # noqa: S311


def random_latitude(minimum: float = -89.0, maximum: float = 89.0) -> float:
    return random.uniform(minimum, maximum)  # noqa: S311


def random_position() -> Position:
    return [random_longitude(), random_latitude()]


def random_point_geometry(
    position: Position | None = None,
) -> dict[str, str | list[float]]:
    return {"type": "Point", "coordinates": position if position else random_position()}


def random_polygon_geometry(
    bbox: BoundingBox = [13.1632, 52.4099, 13.6402, 52.6353],
) -> dict[str, str | Polygon]:
    [min_lng, min_lat, max_lng, max_lat] = bbox

    positions = [
        [random_longitude(min_lng, max_lng), random_latitude(min_lat, max_lat)]
        for _ in range(5)
    ]

    sw: list[float] = []
    ne: list[float] = []

    for [lng, lat] in positions:
        if len(sw) == 0:
            sw = [lng, lat]

        if len(ne) == 0:
            ne = [lng, lat]

        if sw[0] > lng:
            sw[0] = lng

        if sw[1] > lat:
            sw[1] = lat

        if ne[0] < lng:
            ne[0] = lng

        if ne[1] < lat:
            ne[1] = lat

    return {
        "type": "Polygon",
        "coordinates": [[sw, [ne[0], sw[1]], ne, [sw[0], ne[1]], sw]],
    }


def random_point_feature(
    geometry: dict[str, Any] = {}, properties: dict[str, Any] = {}
) -> dict:
    return {
        "type": "Feature",
        "geometry": geometry if geometry else random_point_geometry(),
        "properties": properties,
    }


def random_polygon_feature(
    geometry: dict[str, Any] = {}, properties: dict[str, Any] = {}
) -> dict:
    return {
        "type": "Feature",
        "geometry": geometry if geometry else random_polygon_geometry(),
        "properties": properties,
    }
