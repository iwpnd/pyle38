from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from ..client import Client, Command, SubCommand
from ..responses import BoundsNeSwResponse, HashResponse, ObjectResponse, PointResponse
from .executable import Compiled, Executable

Output = Sequence[Literal["HASH", "OBJECT", "POINT", "BOUNDS"] | int]

Formats = Literal["BOUNDS", "HASH", "OBJECT", "POINT"]


class Get(Executable):
    _key: str
    _id: str
    _withfields: Literal["WITHFIELDS"] | None = None
    _output: Output | None = None

    def __init__(self, client: Client, key: str, oid: str) -> None:
        super().__init__(client)

        self.key(key).id(oid)

    def key(self, key: str) -> Get:
        self._key = key

        return self

    def id(self, oid: str) -> Get:
        self._id = oid

        return self

    def withfields(self, flag: bool = True) -> Get:
        if flag:
            self._withfields = "WITHFIELDS"

        return self

    def output(self, fmt: Formats, precision: int | None = None) -> Get:
        if fmt == "OBJECT":
            self._output = None
        elif fmt == "HASH" and precision:
            self._output = [fmt, precision]
        elif fmt == "BOUNDS" or fmt == "POINT":
            self._output = [fmt]

        return self

    async def asObject(self) -> ObjectResponse:
        self.output("OBJECT")

        return ObjectResponse(**(await self.exec()))

    async def asStringObject(self) -> ObjectResponse[str]:
        self.output("OBJECT")

        return ObjectResponse[str](**(await self.exec()))

    async def asBounds(self) -> BoundsNeSwResponse:
        self.output("BOUNDS")

        return BoundsNeSwResponse(**(await self.exec()))

    async def asPoint(self) -> PointResponse:
        self.output("POINT")

        return PointResponse(**(await self.exec()))

    async def asHash(self, precision: int) -> HashResponse:
        self.output("HASH", precision)

        return HashResponse(**(await self.exec()))

    def compile(self) -> Compiled:
        return [
            Command.GET.value,
            [
                self._key,
                self._id,
                *([SubCommand.WITHFIELDS.value] if self._withfields else []),
                *(self._output if self._output else []),
            ],
        ]  # type: ignore
