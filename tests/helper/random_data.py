import random
import uuid
from typing import Dict, List, Literal, Optional, Union

Position = List[float]
Polygon = List[List[Position]]
BoundingBox = List[float]


def random_string() -> str:
    return str(uuid.uuid4())


def random_integer(minimum: int = 0, maximum: int = 1000) -> int:
    return random.randint(minimum, maximum)


def random_float(minimum: float = 0, maximum: float = 1000) -> float:
    return random.uniform(minimum, maximum)


def random_longitude(minimum=-179.0, maximum=179.0) -> float:
    return random.uniform(minimum, maximum)


def random_latitude(minimum=-89.0, maximum=89.0) -> float:
    return random.uniform(minimum, maximum)


def random_position() -> Position:
    return [random_longitude(), random_latitude()]


def random_point_geometry(
    position: Optional[Position] = None,
) -> Dict[str, Union[str, List[float]]]:
    return {"type": "Point", "coordinates": position if position else random_position()}


def random_polygon_geometry(
    bbox: BoundingBox = [13.1632, 52.4099, 13.6402, 52.6353],
) -> Dict[str, Union[str, Polygon]]:
    [min_lng, min_lat, max_lng, max_lat] = bbox

    positions = [
        [random_longitude(min_lng, max_lng), random_latitude(min_lat, max_lat)]
        for _ in range(5)
    ]

    sw: List[float] = []
    ne: List[float] = []

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


def random_feature(feature_type: Literal["Point", "Polygon"]) -> dict:
    if feature_type == "Point":
        return {"type": "Feature", "geometry": random_point_geometry()}

    if feature_type == "Polygon":
        return random_polygon_geometry()
