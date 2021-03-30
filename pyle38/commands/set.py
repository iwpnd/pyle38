from __future__ import annotations

import json
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from ..client import Client
from ..client import Command
from ..client import SubCommand
from ..responses import JSONResponse
from .executable import Executable


class Set(Executable):
    _key: str
    _id: str
    _ex: Optional[int] = None
    _nx_or_xx: Optional[Literal["NX", "XX"]] = None
    _input: Optional[
        Union[
            List[Union[Literal["POINT"], float]],
            List[Union[Literal["OBJECT"], str]],
            List[Union[Literal["BOUNDS"], float]],
            List[Union[Literal["HASH"], str]],
            List[Union[Literal["STRING"], str]],
        ]
    ] = None

    def __init__(self, client: Client, key: str, id: str) -> None:
        super().__init__(client)

        self.key(key).id(id)

    def key(self, value: str) -> Set:
        self._key = value

        return self

    def id(self, value: str) -> Set:
        self._id = value

        return self

    def ex(self, seconds: Optional[int]) -> Set:
        if seconds:
            self._ex = seconds

        return self

    def nx(self, flag: bool = True) -> Set:
        if flag:
            self._nx_or_xx = SubCommand.NX.value

        return self

    def xx(self, flag: bool = True) -> Set:
        if flag:
            self._nx_or_xx = SubCommand.XX.value

        return self

    def object(self, value: dict) -> Set:
        self._input = [SubCommand.OBJECT.value, json.dumps(value)]

        return self

    def point(self, lat: float, lon: float) -> Set:
        self._input = [SubCommand.POINT.value, lat, lon]

        return self

    def bounds(self, min_lat: float, min_lon: float, max_lat: float, max_lon) -> Set:
        self._input = [SubCommand.BOUNDS.value, min_lat, min_lon, max_lat, max_lon]

        return self

    def hash(self, value: str) -> Set:
        self._input = [SubCommand.HASH.value, value]

        return self

    def string(self, value: str) -> Set:
        self._input = [SubCommand.STRING.value, value]

        return self

    def compile(self) -> List[Union[str, List[Union[str, float, int]]]]:

        return [
            Command.SET.value,
            [
                self._key,
                self._id,
                *([SubCommand.EX.value, self._ex] if self._ex else []),
                *([self._nx_or_xx] if self._nx_or_xx else []),
                *(self._input if self._input else []),
            ],
        ]

    async def exec(self) -> JSONResponse:
        return JSONResponse(**(await self.client.command(*self.compile())))
