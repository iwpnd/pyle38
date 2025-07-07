from __future__ import annotations

import json
from collections.abc import Sequence
from typing import Any, Literal

from typing_extensions import override

from ..client import Client, Command, SubCommand
from ..responses import Fields, JSONResponse
from .executable import Compiled, Executable


class Set(Executable):
    _key: str
    _id: str
    _ex: int | None = None
    _nx_or_xx: Literal["NX", "XX"] | None = None
    _fields: Fields | None
    _input: (
        Sequence[
            Literal["POINT", "OBJECT", "BOUNDS", "HASH", "STRING"] | str | float | int
        ]
        | None
    )

    def __init__(self, client: Client, key: str, oid: str) -> None:
        super().__init__(client)

        self.key(key).id(oid)
        self._fields = {}

    def key(self, value: str) -> Set:
        self._key = value

        return self

    def id(self, value: str) -> Set:
        self._id = value

        return self

    def fields(self, fields: Fields) -> Set:
        self._fields = fields

        return self

    def ex(self, seconds: int) -> Set:
        if seconds:
            self._ex = seconds

        return self

    def nx(self, flag: bool = True) -> Set:
        if flag:
            self._nx_or_xx = "NX"

        return self

    def xx(self, flag: bool = True) -> Set:
        if flag:
            self._nx_or_xx = "XX"

        return self

    def object(self, value: dict) -> Set:
        self._input = ["OBJECT", json.dumps(value)]

        return self

    def point(self, lat: float, lon: float, z: float | None = None) -> Set:
        """Define a point as input.

        Args:
            lat (float): latitude of input point
            lon (float): longitude of input point
            z (float): height of input point (optional)

        Returns:
            Set
        """

        if z:
            self._input = ["POINT", lat, lon, z]
            return self

        self._input = ["POINT", lat, lon]

        return self

    def bounds(
        self, min_lat: float, min_lon: float, max_lat: float, max_lon: float
    ) -> Set:
        self._input = ["BOUNDS", min_lat, min_lon, max_lat, max_lon]

        return self

    def hash(self, value: str) -> Set:
        self._input = ["HASH", value]

        return self

    def string(self, value: str) -> Set:
        self._input = ["STRING", value]

        return self

    @staticmethod
    def __unpack_fields(fields: Fields) -> list[Any]:
        command = []
        for k, v in fields.items():
            if isinstance(v, dict):
                command.extend([SubCommand.FIELD.value, k, json.dumps(v)])
                continue

            command.extend([SubCommand.FIELD.value, k, v])

        return command

    def compile(self) -> Compiled:
        return [
            Command.SET.value,
            [
                self._key,
                self._id,
                *(Set.__unpack_fields(self._fields) if self._fields else []),
                *([SubCommand.EX.value, self._ex] if self._ex else []),
                *([self._nx_or_xx] if self._nx_or_xx else []),
                *(self._input if self._input else []),
            ],
        ]  # type: ignore

    @override
    async def exec(self) -> JSONResponse:  # type: ignore[override]
        return JSONResponse(**(await self.client.command(*self.compile())))
