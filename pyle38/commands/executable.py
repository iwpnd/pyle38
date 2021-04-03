from typing import Any, Dict, Literal

from ..client import Client, Command, CommandArgs

# TODO: fix invalid parameter of Literal
Compiled = Literal[Command, CommandArgs]  # type: ignore


class Executable:
    client: Client

    def __init__(self, client: Client) -> None:
        self.client = client

    def compile(self) -> Compiled:
        raise NotImplementedError("Not implemented")

    async def exec(self) -> Dict[Any, Any]:
        return await self.client.command(*self.compile())
