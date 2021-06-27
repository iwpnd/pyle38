from typing import List, Literal, Optional, Union

from .client import Client, Command, SubCommand
from .commands.get import Get
from .commands.intersects import Intersects
from .commands.nearby import Nearby
from .commands.scan import Scan
from .commands.search import Search
from .commands.within import Within
from .errors import Tile38Error
from .responses import (
    BoundsResponse,
    ChansResponse,
    ConfigGetResponse,
    ConfigKeys,
    HooksResponse,
    InfoFollowerResponse,
    JSONGetResponse,
    JSONResponse,
    KeysResponse,
    PingResponse,
    ServerStatsExtendedResponse,
    ServerStatsResponseFollower,
    StatsResponse,
)


class Follower(Client):
    client: Client

    def __init__(self, url: str) -> None:
        if not url:
            raise Tile38Error("No Tile38 follower uri set")
        super().__init__(url)

        self.client = Client(url)

    async def bounds(self, key: str) -> BoundsResponse:
        return BoundsResponse(**(await self.client.command(Command.BOUNDS, [key])))

    async def chans(self, pattern: str = "*") -> ChansResponse:
        return ChansResponse(**(await self.client.command(Command.CHANS, [pattern])))

    async def config_get(self, name: ConfigKeys) -> ConfigGetResponse:
        return ConfigGetResponse(
            **(await self.client.command(Command.CONFIG, [Command.GET, name]))
        )

    async def config_set(
        self, name: ConfigKeys, value: Union[str, int, float]
    ) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.CONFIG, [Command.SET, name, value]))
        )

    async def config_rewrite(self) -> JSONResponse:
        return JSONResponse(
            **(await self.client.command(Command.CONFIG, [SubCommand.REWRITE]))
        )

    async def gc(self) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.GC)))

    def get(self, key: str, id: str) -> Get:
        return Get(self.client, key, id)

    async def hooks(self, pattern: str = "*") -> HooksResponse:
        return HooksResponse(**(await self.client.command(Command.HOOKS, [pattern])))

    async def healthz(self) -> JSONResponse:
        return JSONResponse(**(await self.client.command(Command.HEALTHZ)))

    async def info(self) -> InfoFollowerResponse:

        return InfoFollowerResponse(**(await self.client.command(Command.INFO)))

    def intersects(self, key: str) -> Intersects:
        return Intersects(self.client, key)

    async def jget(
        self,
        key: str,
        id: str,
        path: Optional[str] = None,
        mode: Optional[Literal["RAW"]] = None,
    ) -> JSONGetResponse:
        return JSONGetResponse(
            **(
                await self.client.command(
                    Command.JGET,
                    [key, id, *([path] if path else []), *([mode] if mode else [])],
                )
            )
        )

    async def keys(self, pattern: str = "*") -> KeysResponse:
        return KeysResponse(**(await self.client.command(Command.KEYS, [pattern])))

    def nearby(self, key: str) -> Nearby:
        return Nearby(self.client, key)

    async def ping(self) -> PingResponse:
        return PingResponse(**(await self.client.command(Command.PING)))

    def scan(self, key: str) -> Scan:
        return Scan(self.client, key)

    def search(self, key: str) -> Search:
        return Search(self.client, key)

    async def server(self) -> ServerStatsResponseFollower:
        return ServerStatsResponseFollower(
            **(await self.client.command(Command.SERVER))
        )

    async def server_extended(self) -> ServerStatsExtendedResponse:
        return ServerStatsExtendedResponse(
            **(await self.client.command(Command.SERVER, [SubCommand.EXT]))
        )

    async def stats(self, keys: List[str]) -> StatsResponse:
        response = await self.client.command(Command.STATS, keys)

        if response["stats"] == [None]:
            response["stats"] = []

        return StatsResponse(**response)

    async def quit(self) -> str:

        await self.client.quit()

        return "OK"

    def within(self, key: str) -> Within:
        return Within(self.client, key)
