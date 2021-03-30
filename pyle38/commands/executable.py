from typing import Any
from typing import Dict
from typing import Literal

from ..client import Command
from ..client import CommandArgs
from .withclient import WithClient

Compiled = Literal[Command, CommandArgs]


class Executable(WithClient):
    def compile(self) -> Compiled:
        raise NotImplementedError("Not implemented")

    async def exec(self) -> Dict[Any, Any]:
        return await self.client.command(*self.compile())
