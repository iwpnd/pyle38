import json
from typing import List
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import TypedDict
from typing import Union

from pydantic import BaseModel
from pydantic import Field


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


class CircleQuery(BaseModel):
    command: Literal["CIRCLE"] = "CIRCLE"
    lat: float
    lng: float
    radius: float

    def get(self) -> Sequence[Union[str, int, float]]:
        return [self.command, self.lat, self.lng, self.radius]


class PointQuery(BaseModel):
    command: Literal["POINT"] = "POINT"
    lat: float
    lng: float
    radius: Optional[Union[float, int]] = None

    def get(self) -> Sequence[Union[str, int, float]]:
        if self.radius:
            return [self.command, self.lat, self.lng, self.radius]

        return [self.command, self.lat, self.lng]


class BoundsQuery(BaseModel):
    command: Literal["BOUNDS"] = "BOUNDS"
    minlat: float
    minlng: float
    maxlat: float
    maxlng: float

    def get(self) -> Sequence[Union[str, int, float]]:
        return [self.command, self.minlat, self.minlng, self.maxlat, self.maxlng]


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
