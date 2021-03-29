from typing import Literal
from typing import Optional
from typing import Union

from .client import Command
from .commands.set import Set
from .follower import Follower
from .responses import JSONResponse


class Leader(Follower):
    async def flushdb(self) -> dict:
        return await self.client.command("FLUSHDB")

    async def jset(
        self,
        key: str,
        id: Union[str, int],
        path: str,
        value: str,
        mode: Optional[Literal["RAW", "STR"]] = None,
    ) -> JSONResponse:
        return JSONResponse(
            **(
                await self.client.command(
                    Command.JSET, [key, id, path, value, *([mode] if mode else [])]
                )
            )
        )

    async def jdel(self, key: str, id: str, path: str) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.JDEL, [key, id, path]))
        )

    def set(self, key: str, id: str) -> Set:
        return Set(self.client, key, id)
