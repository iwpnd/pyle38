from typing import Dict
from typing import Literal
from typing import Union

from ..client import Command
from ..client import CommandArgs
from ..responses import JSONResponse
from .withclient import WithClient

Compiled = Literal[str, CommandArgs]


class Executable(WithClient):
    def compile(self) -> Compiled:
        raise NotImplementedError("Not implemented")

    async def exec(self) -> Union[JSONResponse, Dict]:
        compiled_command = self.compile()
        if compiled_command[0] == Command.SET:

            return JSONResponse(**(await self.client.command(*compiled_command)))

        return await self.client.command(*compiled_command)
