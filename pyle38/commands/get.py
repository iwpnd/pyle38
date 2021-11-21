from __future__ import annotations

from typing import Literal, Optional, Sequence, Union

from ..client import Client, Command, SubCommand
from ..responses import BoundsNeSwResponse, HashResponse, ObjectResponse, PointResponse
from .executable import Compiled, Executable

Output = Union[Sequence[Union[Literal["HASH", "OBJECT", "POINT", "BOUNDS"], int]]]

Formats = Literal["BOUNDS", "HASH", "OBJECT", "POINT"]


class Get(Executable):
    _key: str
    _id: str
    _withfields: Optional[Literal["WITHFIELDS"]] = None
    _output: Optional[Output] = None

    def __init__(self, client: Client, key: str, id: str) -> None:
        super().__init__(client)

        self.key(key).id(id)

    def key(self, key: str) -> Get:
        self._key = key

        return self

    def id(self, id: str) -> Get:
        self._id = id

        return self

    def withfields(self, flag: bool = True) -> Get:
        if flag:
            self._withfields = "WITHFIELDS"

        return self

    def output(self, format: Formats, precision: Optional[int] = None) -> Get:
        if format == "OBJECT":
            self._output = None
        elif format == "HASH" and precision:
            self._output = [format, precision]
        elif format == "BOUNDS":
            self._output = [format]
        elif format == "POINT":
            self._output = [format]

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
        ]
