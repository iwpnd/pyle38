from __future__ import annotations

from typing import List
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Union

from ..client import Client
from ..client import Command
from ..client import CommandArgs
from ..client import SubCommand
from ..models import BoundsQuery
from ..models import CircleQuery
from ..models import Feature
from ..models import GetQuery
from ..models import HashQuery
from ..models import ObjectQuery
from ..models import Options
from ..models import Polygon
from ..models import QuadkeyQuery
from ..models import TileQuery
from ..responses import BoundsNeSwResponses
from ..responses import CountResponse
from ..responses import FenceCommand
from ..responses import FenceDetect
from ..responses import HashesResponse
from ..responses import IdsResponse
from ..responses import ObjectsResponse
from ..responses import PointsResponse
from .executable import Compiled
from .executable import Executable
from .setchan import SetChan
from .sethook import SetHook


Format = Literal["BOUNDS", "COUNT", "HASHES", "IDS", "OBJECTS", "POINTS"]
Output = Union[Sequence[Union[Format, int]]]


class Intersects(Executable):
    _key: str
    _command: Literal["INTERSECTS"]
    _hook: Optional[Union[SetHook, SetChan]] = None
    _options: Options = {}
    _query: Union[
        CircleQuery,
        BoundsQuery,
        HashQuery,
        QuadkeyQuery,
        TileQuery,
        ObjectQuery,
        GetQuery,
    ]
    _output: Optional[Output] = None
    _all: bool = False
    _fence: bool = False
    _detect: Optional[List[FenceDetect]] = []
    _commands: Optional[List[FenceCommand]] = []

    def __init__(
        self, client: Client, key: str, hook: Optional[Union[SetChan, SetHook]] = None
    ) -> None:
        super().__init__(client)

        self.key(key)
        self._options = {}
        self._hook = hook

    def key(self, key: str) -> Intersects:
        self._key = key

        return self

    def circle(self, lat: float, lng: float, radius: float) -> Intersects:
        self._query = CircleQuery(lat=lat, lng=lng, radius=radius)

        return self

    def cursor(self, value: int) -> Intersects:
        self._options["cursor"] = value

        return self

    def fence(self, flag: bool = True) -> Intersects:
        self._fence = flag

        return self

    def detect(self, what: List[FenceDetect]) -> Intersects:
        self._detect = what if len(what) > 0 else []

        return self

    def commands(self, which: Optional[List[FenceCommand]] = []) -> Intersects:
        if which and len(which) > 0:
            self._commands = which

        return self

    def limit(self, value: int) -> Intersects:
        self._options["limit"] = value

        return self

    def nofields(self, flag: bool = True) -> Intersects:
        self._options["nofields"] = flag

        return self

    def match(self, value: str) -> Intersects:
        self._options["match"] = value

        return self

    def sparse(self, value: int) -> Intersects:
        self._options["sparse"] = value

        return self

    def clip(self, flag: bool = True) -> Intersects:
        self._options["clip"] = flag

        return self

    def bounds(
        self, minlat: float, minlng: float, maxlat: float, maxlng: float
    ) -> Intersects:
        self._query = BoundsQuery(
            minlat=minlat, minlng=minlng, maxlat=maxlat, maxlng=maxlng
        )

        return self

    def hash(self, geohash: str) -> Intersects:
        self._query = HashQuery(geohash=geohash)

        return self

    def quadkey(self, quadkey: str) -> Intersects:
        self._query = QuadkeyQuery(quadkey=quadkey)

        return self

    def tile(self, x: int, y: int, z: int) -> Intersects:
        self._query = TileQuery(x=x, y=y, z=z)

        return self

    def object(self, object: Union[Polygon, Feature]) -> Intersects:
        self._query = ObjectQuery(object=object)

        return self

    def get(self, key: str, id: str) -> Intersects:
        self._query = GetQuery(key=key, id=id)

        return self

    def output(self, format: Format, precision: Optional[int] = None) -> Intersects:
        if format == "OBJECTS":
            self._output = None
        elif format == "HASHES" and precision:
            self._output = [format, precision]
        elif format == "BOUNDS":
            self._output = [format]
        elif format == "COUNT":
            self._output = [format]
        elif format == "IDS":
            self._output = [format]
        elif format == "POINTS":
            self._format = [format]

        return self

    async def asObjects(self) -> ObjectsResponse:
        self.output("OBJECTS")

        return ObjectsResponse(**(await self.exec()))

    async def asBounds(self) -> BoundsNeSwResponses:
        self.output("BOUNDS")

        return BoundsNeSwResponses(**(await self.exec()))

    async def asHashes(self, precision: int) -> HashesResponse:
        self.output("HASHES", precision)

        return HashesResponse(**(await self.exec()))

    async def asCount(self) -> CountResponse:
        self.output("COUNT")

        return CountResponse(**(await self.exec()))

    async def asIds(self) -> IdsResponse:
        self.output("IDS")

        return IdsResponse(**(await self.exec()))

    async def asPoints(self) -> PointsResponse:
        self.output("POINTS")

        return PointsResponse(**(await self.exec()))

    def __compile_options(self) -> CommandArgs:
        commands = []

        # raises mypy: TypedDict key must be string literal
        # open PR: https://github.com/python/mypy/issues/7867
        for k in self._options.keys():
            if isinstance(self._options[k], bool):  # type: ignore
                commands.append(k.upper())
            elif self._options[k]:  # type: ignore
                commands.extend([k.upper(), self._options[k]])  # type: ignore
            elif self._options[k] == 0:  # type: ignore
                commands.extend([k.upper(), self._options[k]])  # type: ignore

        return commands

    def __compile_fence(self) -> CommandArgs:
        return (
            [
                SubCommand.FENCE.value,
                *(
                    [SubCommand.DETECT.value, ",".join(self._detect)]
                    if self._detect
                    else []
                ),
                *(
                    [SubCommand.COMMANDS.value, ",".join(self._commands)]
                    if self._commands
                    else []
                ),
            ]
            if self._fence
            else []
        )

    def compile(self) -> Compiled:
        return [
            Command.INTERSECTS.value,
            [
                self._key,
                *(self.__compile_options()),
                *(self.__compile_fence()),
                *(self._query.get()),
                *(self._output if self._output else []),
            ],
        ]
