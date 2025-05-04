import json
from collections.abc import Sequence
from typing import Any, Literal, TypedDict

from pydantic import BaseModel


class Options(TypedDict, total=False):
    cursor: int | None
    limit: int | None
    nofields: int | None
    match: str | None
    sparse: int | None
    clip: bool | None
    distance: bool | None
    asc: bool | None
    desc: bool | None
    buffer: int | None


class CircleQuery(BaseModel):
    command: Literal["CIRCLE"] = "CIRCLE"
    lat: float
    lon: float
    radius: float

    def get(self) -> Sequence[str | int | float]:
        return [self.command, self.lat, self.lon, self.radius]


class PointQuery(BaseModel):
    command: Literal["POINT"] = "POINT"
    lat: float
    lon: float
    radius: float | int | None = None

    def get(self) -> Sequence[str | int | float]:
        if self.radius:
            return [self.command, self.lat, self.lon, self.radius]

        return [self.command, self.lat, self.lon]


class BoundsQuery(BaseModel):
    command: Literal["BOUNDS"] = "BOUNDS"
    minlat: float
    minlon: float
    maxlat: float
    maxlon: float

    def get(self) -> Sequence[str | int | float]:
        return [self.command, self.minlat, self.minlon, self.maxlat, self.maxlon]


class HashQuery(BaseModel):
    command: Literal["HASH"] = "HASH"
    geohash: str

    def get(self) -> Sequence[str]:
        return [self.command, self.geohash]


class QuadkeyQuery(BaseModel):
    command: Literal["QUADKEY"] = "QUADKEY"
    quadkey: str

    def get(self) -> Sequence[str]:
        return [self.command, self.quadkey]


class TileQuery(BaseModel):
    command: Literal["TILE"] = "TILE"
    x: int
    y: int
    z: int

    def get(self) -> Sequence[str | int]:
        return [self.command, self.x, self.y, self.z]


class SectorQuery(BaseModel):
    command: Literal["SECTOR"] = "SECTOR"
    lat: float
    lon: float
    radius: float
    bearing1: float
    bearing2: float

    def get(self) -> Sequence[str | float]:
        return [
            self.command,
            self.lat,
            self.lon,
            self.radius,
            self.bearing1,
            self.bearing2,
        ]


Coordinate = tuple[float, float]


class Polygon(BaseModel):
    type: Literal["Polygon"] = "Polygon"
    coordinates: list[list[Coordinate]]


class Feature(BaseModel):
    type: Literal["Feature"] = "Feature"
    geometry: Polygon
    properties: dict[Any, Any]


class ObjectQuery(BaseModel):
    command: Literal["OBJECT"] = "OBJECT"
    object: Polygon | Feature

    def get(self) -> Sequence[str]:
        return [self.command, json.dumps(self.object.model_dump())]


class GetQuery(BaseModel):
    command: Literal["GET"] = "GET"
    key: str
    id: str

    def get(self) -> Sequence[str]:
        return [self.command, self.key, self.id]
