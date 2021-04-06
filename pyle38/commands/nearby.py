from __future__ import annotations

from typing import List, Literal, Optional, Sequence, Union

from ..client import Client, Command, CommandArgs, SubCommand
from ..errors import Tile38Error
from ..models import Options, PointQuery
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


class Nearby(Executable):
    _key: str
    _command: Literal["NEARBY"]
    _hook = None
    _options: Options = {}
    _query: PointQuery
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

    def key(self, key: str) -> Nearby:
        self._key = key

        return self

    def cursor(self, value: int) -> Nearby:
        self._options["cursor"] = value

        return self

    def fence(self, flag: bool = True) -> Nearby:
        self._fence = flag

        return self

    def detect(self, what: List[FenceDetect]) -> Nearby:
        self._detect = what if len(what) > 0 else []

        return self

    def commands(self, which: Optional[List[FenceCommand]] = []) -> Nearby:
        if which and len(which) > 0:
            self._commands = which

        return self

    def limit(self, value: int) -> Nearby:
        self._options["limit"] = value

        return self

    def nofields(self, flag: bool = True) -> Nearby:
        self._options["nofields"] = flag

        return self

    def match(self, value: str) -> Nearby:
        self._options["match"] = value

        return self

    def sparse(self, value: int) -> Nearby:
        self._options["sparse"] = value

        return self

    def distance(self, flag: bool = True) -> Nearby:
        self._options["distance"] = flag

        return self

    def point(self, lat: float, lon: float, radius: Optional[float] = None) -> Nearby:
        self._query = PointQuery(lat=lat, lon=lon, radius=radius)

        return self

    def output(self, format: Format, precision: Optional[int] = None) -> Nearby:
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
            Command.NEARBY.value,
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
            return [command, [*(args), *(flatten(compiled))]]

        return compiled

    async def activate(self) -> JSONResponse:  # type: ignore
        if self._hook:
            return JSONResponse(**(await self.client.command(*self.compile())))
        else:
            raise Tile38Error("No hook to activate")
