from enum import Enum
from typing import Dict, Sequence, Union

import redis.asyncio as redis
from redis.asyncio.connection import parse_url

from .parse_response import parse_response

TILE38_DEFAULT_HOST = "localhost"
TILE38_DEFAULT_PORT = 9851


class Command(str, Enum):
    AOFSHRINK = "AOFSHRINK"
    AUTH = "AUTH"
    BOUNDS = "BOUNDS"
    CHANS = "CHANS"
    CONFIG = "CONFIG"
    DELCHAN = "DELCHAN"
    DEL = "DEL"
    DELHOOK = "DELHOOK"
    DROP = "DROP"
    EXISTS = "EXISTS"
    EXPIRE = "EXPIRE"
    FEXISTS = "FEXISTS"
    FLUSHDB = "FLUSHDB"
    FSET = "FSET"
    GC = "GC"
    GET = "GET"
    HEALTHZ = "HEALTHZ"
    HOOKS = "HOOKS"
    INFO = "INFO"
    INTERSECTS = "INTERSECTS"
    JDEL = "JDEL"
    JGET = "JGET"
    JSET = "JSET"
    KEYS = "KEYS"
    NEARBY = "NEARBY"
    OUTPUT = "OUTPUT"
    PDELCHAN = "PDELCHAN"
    PDELHOOK = "PDELHOOK"
    PDEL = "PDEL"
    PERSIST = "PERSIST"
    PING = "PING"
    READONLY = "READONLY"
    RENAMENX = "RENAMENX"
    RENAME = "RENAME"
    SCAN = "SCAN"
    SEARCH = "SEARCH"
    SERVER = "SERVER"
    SETCHAN = "SETCHAN"
    SETHOOK = "SETHOOK"
    SET = "SET"
    STATS = "STATS"
    TTL = "TTL"
    WITHIN = "WITHIN"


class SubCommand(str, Enum):
    FIELD = "FIELD"
    EX = "EX"
    NX = "NX"
    XX = "XX"
    WITHFIELDS = "WITHFIELDS"
    CURSOR = "CURSOR"
    LIMIT = "LIMIT"
    NOFIELDS = "NOFIELDS"
    MATCH = "MATCH"
    OBJECT = "OBJECT"
    TILE = "TILE"
    QUADKEY = "QUADKEY"
    HASH = "HASH"
    BOUNDS = "BOUNDS"
    GET = "GET"
    CIRCLE = "CIRCLE"
    POINT = "POINT"
    OBJECTS = "OBJECTS"
    HASHES = "HASHES"
    IDS = "IDS"
    COUNT = "COUNT"
    POINTS = "POINTS"
    STRING = "STRING"
    META = "META"
    FENCE = "FENCE"
    DETECT = "DETECT"
    COMMANDS = "COMMANDS"
    REWRITE = "REWRITE"
    ASC = "ASC"
    DESC = "DESC"
    EXT = "EXT"
    WHERE = "WHERE"
    WHEREIN = "WHEREIN"
    SECTOR = "SECTOR"


class Format(str, Enum):
    JSON = "JSON"
    RESP = "RESP"


CommandArgs = Union[
    Sequence[Union[str, float, int]], Sequence[Sequence[Union[str, float, int]]]
]

NO_RESPONSE_CALLBACKS_FOR = [
    Command.SET,
    Command.SCAN,
    Command.RENAME,
    Command.RENAMENX,
    Command.PING,
    Command.PERSIST,
    Command.INFO,
    Command.EXPIRE,
    Command.FLUSHDB,
    Command.DEL,
    Command.READONLY,
]


class Client:
    __redis = None
    __format: str = Format.RESP.value

    def __init__(self, url: str) -> None:
        self.url = url
        self.__redis = None
        self.__format = Format.RESP.value

    async def force_json(self) -> None:
        """Force the OUTPUT to JSON

        When a new connection is established
        the on_connect callback makes sure to reset the
        OUTPUT to RESP.
        This method makes sure to enforce the OUTPUT to
        JSON on any consecutive command using the connection.
        """
        if self.__format == Format.JSON.value:
            return

        await self.__execute_and_read_response(
            Command.OUTPUT.value, [Format.JSON.value]
        )
        self.__format = Format.JSON.value

    async def __on_connect(self, connection: redis.Connection):
        """On connect callback to set OUTPUT to RESP

        That way we can keep track of the OUTPUT set
        for the connection.
        """
        await connection.on_connect()
        self.format = Format.RESP.value

    async def __delete_response_callbacks(self):
        """Delete response callbacks in redis-py

        redis-py has default callbacks for certain commands
        that are not necessary and cause issues using it with Tile38
        """
        r = await self.__get_redis()
        for command in NO_RESPONSE_CALLBACKS_FOR:
            try:
                del r.response_callbacks[command]
            except KeyError:
                continue

    async def __get_redis(self) -> redis.Redis:
        """Redis connection singleton"""
        if not self.__redis:
            url_components = parse_url(self.url)
            host: str = url_components.get("host") or TILE38_DEFAULT_HOST
            port: int = url_components.get("port") or TILE38_DEFAULT_PORT

            r: redis.Redis = redis.Redis(
                host=host,
                port=port,
                encoding="utf-8",
                single_connection_client=True,
                decode_responses=True,
                redis_connect_func=self.__on_connect,
            )

            self.__redis = r

            await self.__delete_response_callbacks()

        return self.__redis

    async def __execute_and_read_response(
        self, command: str, command_args: CommandArgs = []
    ):
        r = await self.__get_redis()
        return await r.execute_command(command, *command_args)

    async def command(self, command: str, command_args: CommandArgs = []) -> Dict:
        await self.force_json()
        response = await self.__execute_and_read_response(command, command_args)

        return parse_response(response)

    async def quit(self) -> str:
        if not self.__redis:
            return "OK"

        c = await self.__get_redis()

        # TODO: remove ignore once types have been updated
        await c.aclose()  # type: ignore
        await c.connection_pool.disconnect()

        self.__redis = None

        return "OK"
