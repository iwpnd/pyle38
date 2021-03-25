from typing import Literal

from ..client import CommandArgs
from .withclient import WithClient

Compiled = Literal[str, CommandArgs]


class Executable(WithClient):
    def compile(self) -> Compiled:
        raise NotImplementedError("Not implemented")

    async def exec(self) -> dict:
        return await self.client.command(*self.compile())
