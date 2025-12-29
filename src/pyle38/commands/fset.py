from __future__ import annotations

import json
from typing import Any, Literal

from ..client import Client, Command
from ..responses import Fields, JSONResponse
from .executable import Compiled, Executable


class FSet(Executable):
    """Set the value for one or more fields of an id.

    Example::

        key = fleet
        id = truck1
        fields = {"driver":"John"}
        await tile38.set(key, id).point(52.25, 13.37).exec()
        await tile38.fset(key, id, fields)
    """

    _key: str
    _id: str
    _xx: Literal["XX"] | None = None
    _fields: Fields

    def __init__(self, client: Client, key: str, oid: str, fields: Fields) -> None:
        super().__init__(client)

        self._fields = {}
        self.key(key).id(oid).fields(fields)

    def key(self, key: str) -> FSet:
        """Set key of id to add fields to

        Args:
        key (str): key of a collection

        Returns:
            Self
        """
        self._key = key

        return self

    def id(self, oid: str) -> FSet:
        """Set id to add fields to

        Args:
        id (str): id of an object

        Returns:
            Self
        """
        self._id = oid

        return self

    def fields(self, fields: Fields) -> FSet:
        """Set fields to add to object in collection

        Args:
        fields (Fields): Fields to set

        Returns:
            Self
        """
        self._fields = fields

        return self

    def xx(self, flag: bool = True) -> FSet:
        """Alter behaviour if key/id does not exists

        If set, command will return 0 if key/id was not foundotherwise errors

        Args:
        flag (bool): Set True to return 0 if
        key/id not found else False to error on key/id not found.

        Returns:
            Self
        """
        self._xx = "XX" if flag else None

        return self

    @staticmethod
    def __unpack_fields(fields: Fields) -> list[Any]:
        command = []
        for k, v in fields.items():
            if isinstance(v, dict):
                command.extend([k, json.dumps(v)])
                continue

            command.extend([k, v])

        return command

    def compile(self) -> Compiled:
        return [
            Command.FSET.value,
            [
                self._key,
                self._id,
                *([self._xx] if self._xx else []),
                *(FSet.__unpack_fields(self._fields) if self._fields else []),
            ],
        ]  # type: ignore

    async def exec(self) -> JSONResponse:  # type: ignore[override]
        return JSONResponse(**(await self.client.command(*self.compile())))
