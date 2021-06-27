from typing import Literal, Optional, Union

from .client import Command
from .commands.fset import Fset
from .commands.set import Set
from .commands.setchan import SetChan
from .commands.sethook import SetHook
from .follower import Follower
from .responses import (
    Fields,
    InfoLeaderResponse,
    JSONResponse,
    ServerStatsResponseLeader,
    TTLResponse,
)


class Leader(Follower):
    async def delete(self, key: str, id: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.DEL, [key, id])))

    async def delchan(self, name: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.DELCHAN, [name])))

    async def delhook(self, name: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.DELHOOK, [name])))

    async def drop(self, key: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.DROP, [key])))

    async def expire(self, key: str, id: str, seconds: int) -> JSONResponse:
        # TODO: fix mypy
        # for reasons unknown [key, id, seconds] has type List[object]
        # and fails mypy validation
        p = [key, id, seconds]
        response = await self.client.command(Command.EXPIRE, p)  # type: ignore

        return JSONResponse(**response)

    async def flushdb(self) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.FLUSHDB)))

    def fset(self, key: str, id: str, fields: Fields) -> Fset:
        return Fset(self.client, key, id, fields)

    async def info(self) -> InfoLeaderResponse:  # type: ignore

        return InfoLeaderResponse(**(await self.client.command(Command.INFO)))

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

    async def pdelchan(self, pattern: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.PDELCHAN, [pattern])))

    async def pdelhook(self, pattern: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.PDELHOOK, [pattern])))

    async def persist(self, key: str, id: str) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.PERSIST, [key, id])))

    async def readonly(self, value=True) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.READONLY, ["yes" if value else "no"]))
        )

    async def rename(self, key: str, newkey: str, nx=False) -> JSONResponse:
        if nx:
            return JSONResponse(
                **(await self.client.command(Command.RENAMENX, [key, newkey]))
            )

        return JSONResponse(
            **(await self.client.command(Command.RENAME, [key, newkey]))
        )

    def set(self, key: str, id: str) -> Set:
        return Set(self.client, key, id)

    async def server(self) -> ServerStatsResponseLeader:  # type: ignore
        return ServerStatsResponseLeader(**(await self.client.command(Command.SERVER)))

    def sethook(self, name: str, endpoint: str) -> SetHook:
        return SetHook(self.client, name, endpoint)

    def setchan(self, name: str) -> SetChan:
        return SetChan(self.client, name)

    async def ttl(self, key: str, id: str) -> TTLResponse:
        return TTLResponse(**(await self.client.command(Command.TTL, [key, id])))
