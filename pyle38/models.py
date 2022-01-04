import json
from typing import List, Literal, Optional, Sequence, Tuple, TypedDict, Union

from pydantic import BaseModel, Field


class Options(TypedDict, total=False):
    cursor: Optional[int]
    limit: Optional[int]
    nofields: Optional[int]
    match: Optional[str]
    sparse: Optional[int]
    clip: Optional[bool]
    distance: Optional[bool]
    asc: Optional[bool]
    desc: Optional[bool]
    buffer: Optional[int]


class CircleQuery(BaseModel):
    command: Literal["CIRCLE"] = "CIRCLE"
    lat: float
    lon: float
    radius: float

    def get(self) -> Sequence[Union[str, int, float]]:
        return [self.command, self.lat, self.lon, self.radius]


class PointQuery(BaseModel):
    command: Literal["POINT"] = "POINT"
    lat: float
    lon: float
    radius: Optional[Union[float, int]] = None

    def get(self) -> Sequence[Union[str, int, float]]:
        if self.radius:
            return [self.command, self.lat, self.lon, self.radius]

        return [self.command, self.lat, self.lon]


class BoundsQuery(BaseModel):
    command: Literal["BOUNDS"] = "BOUNDS"
    minlat: float
    minlon: float
    maxlat: float
    maxlon: float

    def get(self) -> Sequence[Union[str, int, float]]:
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

    def get(self) -> Sequence[Union[str, int]]:
        return [self.command, self.x, self.y, self.z]


class SectorQuery(BaseModel):
    command: Literal["SECTOR"] = "SECTOR"
    lat: float
    lon: float
    radius: float
    bearing1: float
    bearing2: float

    def get(self) -> Sequence[Union[str, float]]:
        return [
            self.command,
            self.lat,
            self.lon,
            self.radius,
            self.bearing1,
            self.bearing2,
        ]


Coordinate = Tuple[float, float]


class Polygon(BaseModel):
    type: str = Field("Polygon", const=True)
    coordinates: List[List[Coordinate]]


class Feature(BaseModel):
    type: str = Field("Feature", const=True)
    geometry: Polygon


class ObjectQuery(BaseModel):
    command: Literal["OBJECT"] = "OBJECT"
    object: Union[Polygon, Feature]

    def get(self) -> Sequence[str]:
        return [self.command, json.dumps(self.object.dict())]


class GetQuery(BaseModel):
    command: Literal["GET"] = "GET"
    key: str
    id: str

    def get(self) -> Sequence[str]:
        return [self.command, self.key, self.id]
