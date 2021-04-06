from __future__ import annotations

from typing import List, Literal, Optional, Sequence, Union

from ..client import Client, Command, CommandArgs, SubCommand
from ..errors import Tile38Error
from ..models import (
    BoundsQuery,
    CircleQuery,
    Feature,
    GetQuery,
    HashQuery,
    ObjectQuery,
    Options,
    Polygon,
    QuadkeyQuery,
    TileQuery,
)
from ..responses import (
    BoundsNeSwResponses,
    CountResponse,
    FenceCommand,
    FenceDetect,
    HashesResponse,
    IdsResponse,
    JSONResponse,
    ObjectsResponse,
    PointsResponse,
)
from ..utils import flatten
from .executable import Compiled, Executable

Format = Literal["BOUNDS", "COUNT", "HASHES", "IDS", "OBJECTS", "POINTS"]
Output = Union[Sequence[Union[Format, int]]]


class Within(Executable):
    _key: str
    _command: Literal["WITHIN"]
    _hook = None
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

    def __init__(self, client: Client, key: str, hook=None) -> None:
        super().__init__(client)

        self.key(key)
        self._options = {}
        self._hook = hook

    def key(self, key: str) -> Within:
        self._key = key

        return self

    def circle(self, lat: float, lon: float, radius: float) -> Within:
        self._query = CircleQuery(lat=lat, lon=lon, radius=radius)

        return self

    def cursor(self, value: int) -> Within:
        self._options["cursor"] = value

        return self

    def fence(self, flag: bool = True) -> Within:
        self._fence = flag

        return self

    def detect(self, what: List[FenceDetect]) -> Within:
        self._detect = what if len(what) > 0 else []

        return self

    def commands(self, which: Optional[List[FenceCommand]] = []) -> Within:
        if which and len(which) > 0:
            self._commands = which

        return self

    def limit(self, value: int) -> Within:
        self._options["limit"] = value

        return self

    def nofields(self, flag: bool = True) -> Within:
        self._options["nofields"] = flag

        return self

    def match(self, value: str) -> Within:
        self._options["match"] = value

        return self

    def sparse(self, value: int) -> Within:
        self._options["sparse"] = value

        return self

    def bounds(
        self, minlat: float, minlon: float, maxlat: float, maxlon: float
    ) -> Within:
        self._query = BoundsQuery(
            minlat=minlat, minlon=minlon, maxlat=maxlat, maxlon=maxlon
        )

        return self

    def hash(self, geohash: str) -> Within:
        self._query = HashQuery(geohash=geohash)

        return self

    def quadkey(self, quadkey: str) -> Within:
        self._query = QuadkeyQuery(quadkey=quadkey)

        return self

    def tile(self, x: int, y: int, z: int) -> Within:
        self._query = TileQuery(x=x, y=y, z=z)

        return self

    def object(self, object: Union[Polygon, Feature]) -> Within:
        self._query = ObjectQuery(object=object)

        return self

    def get(self, key: str, id: str) -> Within:
        self._query = GetQuery(key=key, id=id)

        return self

    def output(self, format: Format, precision: Optional[int] = None) -> Within:
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
            self._output = [format]

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
        compiled = [
            Command.WITHIN.value,
            [
                self._key,
                *(self.__compile_options()),
                *(self.__compile_fence()),
                *(self._output if self._output else []),
                *(self._query.get()),
            ],
        ]

        if self._hook:
            command, args = self._hook.compile()
            response = [command, [*(args), *(flatten(compiled))]]
            return response

        return compiled

    async def activate(self) -> JSONResponse:  # type: ignore
        if self._hook:
            return JSONResponse(**(await self.client.command(*self.compile())))
        else:
            raise Tile38Error("No hook to activate")
