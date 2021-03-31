from typing import Literal
from typing import Optional
from typing import Union

from .client import Command
from .commands.set import Set
from .follower import Follower
from .responses import JSONResponse
from .responses import ServerStatsResponseLeader
from .responses import TTLResponse


class Leader(Follower):
    async def flushdb(self) -> dict:
        return await self.client.command("FLUSHDB")

    async def expire(self, key: str, id: str, seconds: int) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.EXPIRE, [key, id, seconds]))
        )

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

    async def pdel(self, key: str, pattern: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.PDEL, [key, pattern])))

    async def persist(self, key: str, id: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.PERSIST, [key, id])))

    async def readonly(self, value=True) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.READONLY, ["yes" if value else "no"]))
        )

    def set(self, key: str, id: str) -> Set:
        return Set(self.client, key, id)

    async def server(self) -> ServerStatsResponseLeader:
        return ServerStatsResponseLeader(**(await self.client.command(Command.SERVER)))

    async def ttl(self, key: str, id: str) -> TTLResponse:
        return TTLResponse(**(await self.client.command(Command.TTL, [key, id])))
