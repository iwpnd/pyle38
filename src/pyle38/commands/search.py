from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from ..client import Client, Command, CommandArg, CommandArgs
from ..models import Options
from ..responses import CountResponse, IdsResponse, ObjectsResponse
from .executable import Compiled, Executable
from .whereable import Whereable

Format = Literal["OBJECTS", "COUNT", "IDS"]
Output = Sequence[Format | int]


class Search(Executable, Whereable):
    _key: str
    _command: Literal["SEARCH"]
    _options: Options
    _output: Output | None = None
    _all: bool = False

    def __init__(self, client: Client, key: str) -> None:
        super().__init__(client)

        self.key(key)
        self._options = {}
        self._where = []
        self._wherein = []

    def key(self, key: str) -> Search:
        self._key = key

        return self

    def cursor(self, value: int) -> Search:
        self._options["cursor"] = value

        return self

    def limit(self, value: int) -> Search:
        self._options["limit"] = value

        return self

    def match(self, value: str) -> Search:
        self._options["match"] = value

        return self

    def asc(self, flag: bool = True) -> Search:
        self._options["asc"] = flag

        if flag:
            self._options["desc"] = False

        return self

    def desc(self, flag: bool = True) -> Search:
        self._options["desc"] = flag

        if flag:
            self._options["asc"] = False

        return self

    def output(self, fmt: Format) -> Search:
        if fmt == "OBJECTS":
            self._output = None
        elif fmt == "COUNT" or fmt == "IDS":
            self._output = [fmt]
        return self

    async def asCount(self) -> CountResponse:
        self.output("COUNT")

        return CountResponse(**(await self.exec()))

    async def asIds(self) -> IdsResponse:
        self.output("IDS")

        return IdsResponse(**(await self.exec()))

    async def asStringObjects(self) -> ObjectsResponse[str]:
        self.output("OBJECTS")

        return ObjectsResponse[str](**(await self.exec()))

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
            Command.SEARCH.value,
            [
                self._key,
                *(self.__compile_options()),
                *(self.compile_where()),
                *(self.compile_wherein()),
                *(self._output if self._output else []),
            ],
        ]  # type: ignore
