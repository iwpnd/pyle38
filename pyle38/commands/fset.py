from __future__ import annotations

from typing import Literal, Optional

from ..client import Client, Command
from ..responses import Fields, JSONResponse
from .executable import Compiled, Executable


class Fset(Executable):
    _key: str
    _id: str
    _xx: Optional[Literal["XX"]] = None
    _fields: Fields = {}

    def __init__(self, client: Client, key: str, id: str, fields: Fields) -> None:
        super().__init__(client)

        self._fields = {}
        self.key(key).id(id).fields(fields)

    def key(self, key: str) -> Fset:
        self._key = key

        return self

    def id(self, id: str) -> Fset:
        self._id = id

        return self

    def fields(self, fields: Fields) -> Fset:
        self._fields = fields

        return self

    def xx(self, flag: bool = True) -> Fset:
        self._xx = "XX" if flag else None

        return self

    @staticmethod
    def __unpack_fields(fields: Fields):
        command = []
        for k, v in fields.items():
            command.extend([k, v])

        return command

    def compile(self) -> Compiled:
        return [
            Command.FSET.value,
            [
                self._key,
                self._id,
                *([self._xx] if self._xx else []),
                *(Fset.__unpack_fields(self._fields) if self._fields else []),
            ],
        ]

    async def exec(self) -> JSONResponse:  # type: ignore
        return JSONResponse(**(await self.client.command(*self.compile())))
