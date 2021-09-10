from enum import Enum
from typing import Dict, Optional, Sequence, Union

import aioredis

from .parse_response import parse_response


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

    async def __force_json(self) -> None:
        if self.__format == Format.JSON.value:
            return

        await self.__command_async(Command.OUTPUT.value, [Format.JSON.value])

        self.__format = Format.JSON.value

    async def __getRedis(self) -> aioredis.Redis:
        if not self.__redis:
            self.__redis = aioredis.from_url(
                self.url, encoding="utf-8", decode_responses=True
            )
            self.__format = Format.RESP.value

        return self.__redis

    async def __command_async(
        self, command: str, command_args: Optional[CommandArgs] = []
    ):
        pool = await self.__getRedis()
        async with pool.client() as c:
            await c.connection.send_command(command, *command_args)
            response = await c.connection.read_response()
            return response

    async def command(
        self, command: str, command_args: Optional[CommandArgs] = []
    ) -> Dict:
        await self.__force_json()

        response = await self.__command_async(command, command_args)

        return parse_response(response)

    async def quit(self) -> str:
        if not self.__redis:
            return "OK"

        c = await self.__getRedis()

        await c.close()
        await c.connection_pool.disconnect()

        self.__redis = None

        return "OK"
