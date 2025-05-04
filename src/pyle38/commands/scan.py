from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from ..client import Client, Command, CommandArg, CommandArgs
from ..models import Options
from ..responses import (
    BoundsNeSwResponses,
    CountResponse,
    HashesResponse,
    IdsResponse,
    ObjectsResponse,
    PointsResponse,
)
from .executable import Compiled, Executable
from .whereable import Whereable

Format = Literal["BOUNDS", "COUNT", "HASHES", "IDS", "OBJECTS", "POINTS"]
Output = Sequence[Format | int]


class Scan(Executable, Whereable):
    _key: str
    _command: Literal["SCAN"]
    _options: Options
    _output: Output | None = None
    _all: bool = False

    def __init__(self, client: Client, key: str) -> None:
        super().__init__(client)

        self.key(key)
        self._options = {}
        self._where = []
        self._wherein = []

    def key(self, key: str) -> Scan:
        self._key = key

        return self

    def cursor(self, value: int) -> Scan:
        self._options["cursor"] = value

        return self

    def limit(self, value: int) -> Scan:
        self._options["limit"] = value

        return self

    def nofields(self, flag: bool = True) -> Scan:
        self._options["nofields"] = flag

        return self

    def match(self, value: str) -> Scan:
        self._options["match"] = value

        return self

    def sparse(self, value: int) -> Scan:
        self._options["sparse"] = value

        return self

    def asc(self, flag: bool = True) -> Scan:
        self._options["asc"] = flag

        if flag:
            self._options["desc"] = False

        return self

    def desc(self, flag: bool = True) -> Scan:
        self._options["desc"] = flag

        if flag:
            self._options["asc"] = False

        return self

    def output(self, fmt: Format, precision: int | None = None) -> Scan:
        if fmt == "OBJECTS":
            self._output = None
        elif fmt == "HASHES" and precision:
            self._output = [fmt, precision]
        elif fmt == "BOUNDS" or fmt == "COUNT" or fmt == "IDS" or fmt == "POINTS":
            self._output = [fmt]

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
        commands: list[CommandArg] = []

        # raises mypy: TypedDict key must be string literal
        # open PR: https://github.com/python/mypy/issues/7867
        for k in self._options:
            if isinstance(self._options[k], bool):  # type: ignore
                if self._options[k]:  # type: ignore
                    commands.append(k.upper())
            elif self._options[k] or self._options[k] == 0:  # type: ignore
                commands.extend([k.upper(), self._options[k]])  # type: ignore

        return commands

    def compile(self) -> Compiled:
        return [
            Command.SCAN.value,
            [
                self._key,
                *(self.__compile_options()),
                *(self.compile_where()),
                *(self.compile_wherein()),
                *(self._output if self._output else []),
            ],
        ]  # type: ignore
