from __future__ import annotations

from typing import Literal, Optional

from ..client import Client, Command, SubCommand
from ..commands.intersects import Intersects
from ..commands.nearby import Nearby
from ..commands.within import Within
from ..responses import Meta
from .executable import Compiled, Executable


class SetHook(Executable):
    _command: Literal["SETHOOK"] = "SETHOOK"
    _endpoint: Optional[str] = None
    _meta: Optional[Meta] = {}
    _ex: Optional[int] = None

    def __init__(self, client: Client, name: str, endpoint: str) -> None:
        super().__init__(client)

        self.name(name)
        self.endpoint(endpoint)
        self._meta = {}

    def name(self, name) -> SetHook:
        self._name = name

        return self

    def endpoint(self, endpoint: str) -> SetHook:
        self._endpoint = endpoint

        return self

    def meta(self, meta: Meta) -> SetHook:
        self._meta = meta

        return self

    def ex(self, ex: int) -> SetHook:
        self._ex = ex

        return self

    def nearby(self, key: str) -> Nearby:
        return Nearby(self.client, key, self).fence()

    def within(self, key: str) -> Within:
        return Within(self.client, key, self).fence()

    def intersects(self, key: str) -> Intersects:
        return Intersects(self.client, key, self).fence()

    @staticmethod
    def __unpack_meta(meta: Meta):
        command = []
        for k, v in meta.items():
            command.extend([SubCommand.META.value, k, v])

        return command

    def compile(self) -> Compiled:
        return [
            Command.SETHOOK.value,
            [
                self._name,
                *([self._endpoint] if self._endpoint else []),
                *(SetHook.__unpack_meta(self._meta) if self._meta else []),
                *([SubCommand.EX.value, self._ex] if self._ex else []),
            ],
        ]
