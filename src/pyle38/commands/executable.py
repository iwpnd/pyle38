from typing import Any

from ..client import Client, Command, CommandArgs

Compiled = tuple[Command, CommandArgs]


class Executable:
    client: Client

    def __init__(self, client: Client) -> None:
        self.client = client

    def compile(self) -> Compiled:
        raise NotImplementedError("Not implemented")

    async def exec(self) -> dict[Any, Any]:
        return await self.client.command(*self.compile())
