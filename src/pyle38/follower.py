from collections.abc import Callable
from typing import Literal

from .client import Client, Command, SubCommand
from .client_options import ClientOptions
from .commands.fget import FGet
from .commands.get import Get
from .commands.intersects import Intersects
from .commands.nearby import Nearby
from .commands.scan import Scan
from .commands.search import Search
from .commands.within import Within
from .errors import Pyle38NoFollowerSetError
from .responses import (
    BoundsResponse,
    ChansResponse,
    ConfigGetResponse,
    ConfigKeys,
    ExistsResponse,
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


class Follower:
    """
    A class to interact with a Tile38 follower instance using various Tile38 commands.

    Attributes:
        client (Client): An instance of the Client class for connecting to Tile38.
    """

    client: Client

    def __init__(self, url: str, opts: list[Callable[..., ClientOptions]] = []) -> None:
        """Initialize the Follower client.

        Args:
            url (str): The URL for connecting to the Tile38 follower server.
            opts (List[Callable[..., ClientOptions]], optional): A list of callables that modify client options.

        Raises:
            Tile38Error: If the follower URL is not provided.
        """
        if not url:
            raise Pyle38NoFollowerSetError

        self.client = Client(url, opts)

    async def aofshrink(self) -> JSONResponse:
        """Shrink the append only file on"""
        return JSONResponse(**(await self.client.command(Command.AOFSHRINK)))

    async def exists(self, key: str, oid: str) -> ExistsResponse:
        """Check if an object exists in a collection.

        Tile38 Command:
            EXISTS key id

        Args:
            key (str): The collection key.
            id (str): The object ID.

        Returns:
            ExistsResponse: Response indicating if the object exists.
        """
        return ExistsResponse(**(await self.client.command(Command.EXISTS, [key, oid])))

    async def fexists(self, key: str, oid: str, field: str) -> ExistsResponse:
        """Check if a field exists within an object.

        Tile38 Command:
            FEXISTS key id field

        Args:
            key (str): The collection key.
            id (str): The object ID.
            field (str): The field name.

        Returns:
            ExistsResponse: Response indicating if the field exists.
        """
        return ExistsResponse(
            **(await self.client.command(Command.FEXISTS, [key, oid, field]))
        )

    async def bounds(self, key: str) -> BoundsResponse:
        """Get the bounds of a collection.

        Tile38 Command:
            BOUNDS key

        Args:
            key (str): The collection key.

        Returns:
            BoundsResponse: The bounding box of the specified collection.
        """
        return BoundsResponse(**(await self.client.command(Command.BOUNDS, [key])))

    async def chans(self, pattern: str = "*") -> ChansResponse:
        """List active channels.

        Tile38 Command:
            CHANS pattern

        Args:
            pattern (str, optional): The pattern to match channel names.

        Returns:
            ChansResponse: A list of active channels.
        """
        return ChansResponse(**(await self.client.command(Command.CHANS, [pattern])))

    async def config_get(self, name: ConfigKeys) -> ConfigGetResponse:
        """Get a configuration value.

        Tile38 Command:
            CONFIG GET name

        Args:
            name (ConfigKeys): The configuration key.

        Returns:
            ConfigGetResponse: The value of the requested configuration key.
        """
        return ConfigGetResponse(
            **(await self.client.command(Command.CONFIG, [Command.GET, name]))
        )

    async def config_set(
        self, name: ConfigKeys, value: str | int | float
    ) -> JSONResponse:
        """Set a configuration value.

        Tile38 Command:
            CONFIG SET name value

        Args:
            name (ConfigKeys): The configuration key.
            value (Union[str, int, float]): The value to set.

        Returns:
            JSONResponse: Confirmation of the configuration update.
        """
        return JSONResponse(
            **(await self.client.command(Command.CONFIG, [Command.SET, name, value]))
        )

    async def config_rewrite(self) -> JSONResponse:
        """Rewrite the configuration file.

        Tile38 Command:
            CONFIG REWRITE

        Returns:
            JSONResponse: Confirmation of the rewrite.
        """
        return JSONResponse(
            **(await self.client.command(Command.CONFIG, [SubCommand.REWRITE]))
        )

    async def gc(self) -> JSONResponse:
        """Trigger garbage collection.

        Tile38 Command:
            GC

        Returns:
            JSONResponse: Confirmation of garbage collection.
        """
        return JSONResponse(**(await self.client.command(Command.GC)))

    def get(self, key: str, oid: str) -> Get:
        """Get a specific object.

        Tile38 Command:
            GET key id

        Args:
            key (str): The collection key.
            id (str): The object ID.

        Returns:
            Get: An object that allows retrieving data from Tile38.
        """
        return Get(self.client, key, oid)

    def fget(self, key: str, oid: str, field: str) -> FGet:
        """Get a specific field on an object.

        Tile38 Command:
            FGET key id field

        Args:
            key (str): The collection key.
            id (str): The object ID.
            field (str): The field to look up.

        Returns:
            FGet: An object that allows retrieving field data from Tile38.
        """
        return FGet(self.client, key, oid, field)

    async def hooks(self, pattern: str = "*") -> HooksResponse:
        """List active hooks.

        Tile38 Command:
            HOOKS pattern

        Args:
            pattern (str, optional): The pattern to match hook names.

        Returns:
            HooksResponse: A list of active hooks.
        """
        return HooksResponse(**(await self.client.command(Command.HOOKS, [pattern])))

    async def healthz(self) -> JSONResponse:
        """Check the health of the Tile38 server.

        Tile38 Command:
            HEALTHZ

        Returns:
            JSONResponse: Server health status.
        """
        return JSONResponse(**(await self.client.command(Command.HEALTHZ)))

    async def info(self) -> InfoFollowerResponse:
        """Get server information.

        Tile38 Command:
            INFO

        Returns:
            InfoFollowerResponse: Server information and statistics.
        """
        return InfoFollowerResponse(**(await self.client.command(Command.INFO)))

    def intersects(self, key: str) -> Intersects:
        """Query objects that intersect a specified area.

        Tile38 Command:
            INTERSECTS

        Args:
            key (str): The collection key.

        Returns:
            Intersects: An object to perform intersection queries.
        """
        return Intersects(self.client, key)

    async def keys(self, pattern: str = "*") -> KeysResponse:
        """List keys matching a pattern.

        Tile38 Command:
            KEYS pattern

        Args:
            pattern (str, optional): The pattern to match keys.

        Returns:
            KeysResponse: A list of matching keys.
        """
        return KeysResponse(**(await self.client.command(Command.KEYS, [pattern])))

    async def jget(
        self,
        key: str,
        oid: str,
        path: str | None = None,
        mode: Literal["RAW"] | None = None,
    ) -> JSONGetResponse:
        """Get a JSON field.

        Tile38 Command:
            JGET key id [path] [RAW]

        Args:
            key (str): The collection key.
            id (str): The object ID.
            path (Optional[str], optional): The JSON path.
            mode (Optional[Literal["RAW"]], optional): RAW mode for unparsed output.

        Returns:
            JSONGetResponse: The requested JSON data.
        """
        return JSONGetResponse(
            **(
                await self.client.command(
                    Command.JGET,
                    [key, oid, *([path] if path else []), *([mode] if mode else [])],
                )
            )
        )

    def nearby(self, key: str) -> Nearby:
        """Find objects near a specified location.

        Tile38 Command:
            NEARBY

        Args:
            key (str): The collection key.

        Returns:
            Nearby: An object to perform nearby queries.
        """
        return Nearby(self.client, key)

    async def ping(self) -> PingResponse:
        """Ping the Tile38 server.

        Tile38 Command:
            PING

        Returns:
            PingResponse: Ping response from the server.
        """
        return PingResponse(**(await self.client.command(Command.PING)))

    def scan(self, key: str) -> Scan:
        """Scan a collection.

        Tile38 Command:
            SCAN

        Args:
            key (str): The collection key.

        Returns:
            Scan: An object to perform scan queries.
        """
        return Scan(self.client, key)

    def search(self, key: str) -> Search:
        """Search a collection.

        Tile38 Command:
            SEARCH key

        Args:
            key (str): The collection key.

        Returns:
            Search: An object to perform search queries.
        """
        return Search(self.client, key)

    async def server(self) -> ServerStatsResponseFollower:
        """Get server stats.

        Tile38 Command:
            SERVER

        Returns:
            ServerStatsResponseFollower: Basic server statistics.
        """
        return ServerStatsResponseFollower(
            **(await self.client.command(Command.SERVER))
        )

    async def server_extended(self) -> ServerStatsExtendedResponse:
        """Get extended server stats.

        Tile38 Command:
            SERVER

        Returns:
            ServerStatsExtendedResponse: Extended server statistics.
        """
        return ServerStatsExtendedResponse(
            **(await self.client.command(Command.SERVER, [SubCommand.EXT]))
        )

    async def stats(self, keys: list[str]) -> StatsResponse:
        """Get statistics for specified keys.

        Tile38 Command:
            STATS key...

        Args:
            keys (List[str]): A list of keys to get statistics for.

        Returns:
            StatsResponse: Statistics for the given keys.
        """
        response = await self.client.command(Command.STATS, keys)
        if response["stats"] == [None]:
            response["stats"] = []
        return StatsResponse(**response)

    async def quit(self) -> str:
        """Disconnect from Tile38.

        Tile38 Command:
            QUIT

        Returns:
            str: A confirmation message ("OK") upon successful termination.
        """
        await self.client.quit()
        return "OK"

    def within(self, key: str) -> Within:
        """Query objects within a specified area.

        Tile38 Command:
            WITHIN

        Args:
            key (str): The collection key.

        Returns:
            Within: An object to perform within-area queries.
        """
        return Within(self.client, key)
