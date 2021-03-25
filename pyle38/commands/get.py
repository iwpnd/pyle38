from __future__ import annotations

from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from ..client import Client
from ..client import Command
from ..client import SubCommand
from .executable import Executable

Output = Union[
    List[Union[Literal["HASH"], int]],
    List[Literal["OBJECT"]],
    List[Literal["POINT"]],
    List[Literal["BOUNDS"]],
]

Formats = Union[Literal["BOUNDS"], Literal["HASH"], Literal["OBJECT"], Literal["POINT"]]


class Get(Executable):
    _key: str
    _id: str
    _with_fields: Optional[Literal["WITHFIELDS"]] = None
    _output: Optional[Output]

    def __init__(self, client: Client, key: str, id: str) -> None:
        super().__init__(client)

        self.key(key).id(id)

    def key(self, key: str) -> Get:
        self._key = key

        return self

    def id(self, id: str) -> Get:
        self._id = id

        return self

    def with_fields(self, flag: bool = True) -> Get:
        if flag:
            self._with_fields = SubCommand.WITHFIELDS.value

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

    # TODO: add Response
    async def asObjects(self):
        self.output(SubCommand.OBJECT.value)

        return await self.exec()

    async def asBounds(self):
        self.output(SubCommand.BOUNDS.value)

        return await self.exec()

    async def asPoint(self):
        self.output(SubCommand.POINT.value)

        return await self.exec()

    async def asHash(self, precision: int):
        self.output(SubCommand.HASH.value, precision)

        return await self.exec()

    def compile(self) -> List[Union[str, List[Union[str, float, int]]]]:
        return [
            Command.GET.value,
            [
                self._key,
                self._id,
                *([SubCommand.WITHFIELDS.value] if self._with_fields else []),
                *(self._output if self._output else []),
            ],
        ]
