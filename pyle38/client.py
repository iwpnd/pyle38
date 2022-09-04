from enum import Enum
from typing import Dict, Sequence, Union

import redis.asyncio as redis
from redis.asyncio.connection import parse_url

from .parse_response import parse_response

TILE38_DEFAULT_HOST = "localhost"
TILE38_DEFAULT_PORT = 9851


class Command(str, Enum):
    AUTH = "AUTH"
    AOFSHRINK = "AOFSHRINK"
    BOUNDS = "BOUNDS"
    CHANS = "CHANS"
    DEL = "DEL"
    DELCHAN = "DELCHAN"
    GC = "GC"
    HOOKS = "HOOKS"
    HEALTHZ = "HEALTHZ"
    INFO = "INFO"
    PDEL = "PDEL"
    PERSIST = "PERSIST"
    TTL = "TTL"
    DELHOOK = "DELHOOK"
    DROP = "DROP"
    EXPIRE = "EXPIRE"
    SET = "SET"
    FSET = "FSET"
    GET = "GET"
    OUTPUT = "OUTPUT"
    PING = "PING"
    FLUSHDB = "FLUSHDB"
    KEYS = "KEYS"
    WITHIN = "WITHIN"
    READONLY = "READONLY"
    SERVER = "SERVER"
    SETCHAN = "SETCHAN"
    SETHOOK = "SETHOOK"
    STATS = "STATS"
    RENAME = "RENAME"
    RENAMENX = "RENAMENX"
    INTERSECTS = "INTERSECTS"
    CONFIG = "CONFIG"
    JGET = "JGET"
    JSET = "JSET"
    JDEL = "JDEL"
    NEARBY = "NEARBY"
    PDELCHAN = "PDELCHAN"
    PDELHOOK = "PDELHOOK"
    SCAN = "SCAN"
    SEARCH = "SEARCH"


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
    SECTOR = "SECTOR"


class Format(str, Enum):
    JSON = "JSON"
    RESP = "RESP"


CommandArgs = Union[
    Sequence[Union[str, float, int]], Sequence[Sequence[Union[str, float, int]]]
]


class Client:
    __redis = None
    __format: str = Format.RESP.value

    def __init__(self, url: str) -> None:
        self.url = url
        self.__redis = None
        self.__format = Format.RESP.value

    async def force_json(self) -> None:
        if self.__format == Format.JSON.value:
            return

        await self.__execute_and_read_response(
            Command.OUTPUT.value, [Format.JSON.value]
        )
        self.__format = Format.JSON.value

    async def __on_connect(self, connection: redis.Connection):
        await connection.on_connect()
        self.format = Format.RESP.value

    async def __get_redis(self) -> redis.Redis:
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

        return self.__redis

    async def __execute_and_read_response(
        self, command: str, command_args: CommandArgs = []
    ):
        r = await self.__get_redis()
        await r.initialize()

        if r.connection:
            await r.connection.send_command(command, *command_args)
            response = await r.connection.read_response()
            return response

    async def command(self, command: str, command_args: CommandArgs = []) -> Dict:
        await self.force_json()
        response = await self.__execute_and_read_response(command, command_args)

        return parse_response(response)

    async def quit(self) -> str:
        if not self.__redis:
            return "OK"

        c = await self.__get_redis()

        await c.close()
        await c.connection_pool.disconnect()

        self.__redis = None

        return "OK"
