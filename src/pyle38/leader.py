from typing import Literal

from .client import Command, CommandArg
from .commands.fset import FSet
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
    """
    A class to interact with a Tile38 leader instance, extending the Follower class
    with additional write and administrative commands.

    Attributes:
        client (Client): An instance of the Client class for connecting to Tile38.
    """

    async def delete(self, key: str, oid: str) -> JSONResponse:
        """Delete an object from a collection.

        Tile38 Command:
            DEL key id

        Args:
            key (str): The collection key.
            id (str): The object ID.

        Returns:
            JSONResponse: Confirmation of deletion.
        """
        return JSONResponse(**(await self.client.command(Command.DEL, [key, oid])))

    async def delchan(self, name: str) -> JSONResponse:
        """Delete a channel.

        Tile38 Command:
            DELCHAN name

        Args:
            name (str): The channel name.

        Returns:
            JSONResponse: Confirmation of channel deletion.
        """
        return JSONResponse(**(await self.client.command(Command.DELCHAN, [name])))

    async def delhook(self, name: str) -> JSONResponse:
        """Delete a geofence hook.

        Tile38 Command:
            DELHOOK name

        Args:
            name (str): The hook name.

        Returns:
            JSONResponse: Confirmation of hook deletion.
        """
        return JSONResponse(**(await self.client.command(Command.DELHOOK, [name])))

    async def drop(self, key: str) -> JSONResponse:
        """Drop an entire collection.

        Tile38 Command:
            DROP key

        Args:
            key (str): The collection key.

        Returns:
            JSONResponse: Confirmation of collection drop.
        """
        return JSONResponse(**(await self.client.command(Command.DROP, [key])))

    async def expire(self, key: str, oid: str, seconds: int) -> JSONResponse:
        """Set an expiration time for an object.

        Tile38 Command:
            EXPIRE key id seconds

        Args:
            key (str): The collection key.
            id (str): The object ID.
            seconds (int): The expiration time in seconds.

        Returns:
            JSONResponse: Confirmation of expiration set.
        """
        # TODO: fix mypy
        # for reasons unknown [key, id, seconds] has type List[object]
        # and fails mypy validation
        p: list[CommandArg] = [key, oid, seconds]
        response = await self.client.command(Command.EXPIRE, p)

        return JSONResponse(**response)

    async def flushdb(self) -> JSONResponse:
        """Delete all data from the Tile38 database.

        Tile38 Command:
            FLUSHDB

        Returns:
            JSONResponse: Confirmation of database flush.
        """
        return JSONResponse(**(await self.client.command(Command.FLUSHDB)))

    def fset(self, key: str, oid: str, fields: Fields) -> FSet:
        """Set fields on an existing object.

        Tile38 Command:
            FSET key id field value...

        Args:
            key (str): The collection key.
            id (str): The object ID.
            fields (Fields): The fields to set.

        Returns:
            Fset: An object to perform field set operations.
        """
        return FSet(self.client, key, oid, fields)

    # TODO: how can I override supertype Follower here correctly?
    async def info(self) -> InfoLeaderResponse:  # type: ignore[override]
        """Get detailed server information specific to the leader.

        Tile38 Command:
            INFO

        Returns:
            InfoLeaderResponse: Server information and statistics.
        """
        return InfoLeaderResponse(**(await self.client.command(Command.INFO)))

    async def jset(
        self,
        key: str,
        oid: str | int,
        path: str,
        value: str,
        mode: Literal["RAW", "STR"] | None = None,
    ) -> JSONResponse:
        """Set a JSON value in an object.

        Tile38 Command:
            JSET key id path value [RAW|STR]

        Args:
            key (str): The collection key.
            id (Union[str, int]): The object ID.
            path (str): The JSON path.
            value (str): The value to set.
            mode (Optional[Literal["RAW", "STR"]]): Mode for setting value.

        Returns:
            JSONResponse: Confirmation of JSON value set.
        """
        return JSONResponse(
            **(
                await self.client.command(
                    Command.JSET, [key, oid, path, value, *([mode] if mode else [])]
                )
            )
        )

    async def jdel(self, key: str, oid: str, path: str) -> JSONResponse:
        """Delete a JSON value from an object.

        Tile38 Command:
            JDEL key id path

        Args:
            key (str): The collection key.
            id (str): The object ID.
            path (str): The JSON path.

        Returns:
            JSONResponse: Confirmation of JSON value deletion.
        """
        return JSONResponse(
            **(await self.client.command(Command.JDEL, [key, oid, path]))
        )

    async def pdel(self, key: str, pattern: str) -> JSONResponse:
        """Delete objects matching a pattern.

        Tile38 Command:
            PDEL key pattern

        Args:
            key (str): The collection key.
            pattern (str): The pattern to match IDs.

        Returns:
            JSONResponse: Confirmation of pattern-based deletion.
        """
        return JSONResponse(**(await self.client.command(Command.PDEL, [key, pattern])))

    async def pdelchan(self, pattern: str) -> JSONResponse:
        """Delete channels matching a pattern.

        Tile38 Command:
            PDELCHAN pattern

        Args:
            pattern (str): The pattern to match channel names.

        Returns:
            JSONResponse: Confirmation of channel deletion.
        """
        return JSONResponse(**(await self.client.command(Command.PDELCHAN, [pattern])))

    async def pdelhook(self, pattern: str) -> JSONResponse:
        """Delete hook matching a pattern.

        Tile38 Command:
            PDELHOOK pattern

        Args:
            pattern (str): The pattern to match hook names.

        Returns:
            JSONResponse: Confirmation of hook deletion.
        """
        return JSONResponse(**(await self.client.command(Command.PDELHOOK, [pattern])))

    async def persist(self, key: str, oid: str) -> JSONResponse:
        """Remove expiration from an object.

        Tile38 Command:
            PERSIST key id

        Args:
            key (str): The collection key.
            id (str): The object ID.

        Returns:
            JSONResponse: Confirmation of persistence.
        """
        return JSONResponse(**(await self.client.command(Command.PERSIST, [key, oid])))

    async def readonly(self, value: bool = True) -> JSONResponse:
        """Set the server to readonly mode.

        Tile38 Command:
            READONLY yes|no

        Args:
            value (bool): True to enable readonly mode, False to disable.

        Returns:
            JSONResponse: Confirmation of readonly status.
        """
        return JSONResponse(
            **(await self.client.command(Command.READONLY, ["yes" if value else "no"]))
        )

    async def rename(self, key: str, newkey: str, nx: bool = False) -> JSONResponse:
        """Rename a collection key.

        Tile38 Command:
            RENAME key newkey
            RENAMENX key newkey

        Args:
            key (str): The current collection key.
            newkey (str): The new collection key.
            nx (bool): If True, rename only if the new key does not exist.

        Returns:
            JSONResponse: Confirmation of key renaming.
        """
        command = Command.RENAMENX if nx else Command.RENAME
        return JSONResponse(**(await self.client.command(command, [key, newkey])))

    def set(self, key: str, oid: str) -> Set:
        """Set an object in a collection.

        Tile38 Command:
            SET key id

        Args:
            key (str): The collection key.
            id (str): The object ID.

        Returns:
            Set: An object to perform set operations.
        """
        return Set(self.client, key, oid)

    # TODO: how can I override supertype Follower here correctly?
    async def server(self) -> ServerStatsResponseLeader:  # type: ignore[override]
        """Get server stats specific to the leader.

        Tile38 Command:
            SERVER

        Returns:
            ServerStatsResponseLeader: Server statistics.
        """
        return ServerStatsResponseLeader(**(await self.client.command(Command.SERVER)))

    def sethook(self, name: str, endpoint: str) -> SetHook:
        """Set a geofence hook.

        Tile38 Command:
            SETHOOK name endpoint

        Args:
            name (str): The hook name.
            endpoint (str): The endpoint URL.

        Returns:
            SetHook: An object to configure the hook.
        """
        return SetHook(self.client, name, endpoint)

    def setchan(self, name: str) -> SetChan:
        """Create a pub/sub channel.

        Tile38 Command:
            SETCHAN name

        Args:
            name (str): The channel name.

        Returns:
            SetChan: An object to configure the channel.
        """
        return SetChan(self.client, name)

    async def ttl(self, key: str, oid: str) -> TTLResponse:
        """Get the time-to-live (TTL) of an object.

        Tile38 Command:
            TTL key id

        Args:
            key (str): The collection key.
            id (str): The object ID.

        Returns:
            TTLResponse: The TTL in seconds.
        """
        return TTLResponse(**(await self.client.command(Command.TTL, [key, oid])))
