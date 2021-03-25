from enum import Enum
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

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


class Format(str, Enum):
    JSON = "JSON"
    RESP = "RESP"


CommandArgs = Union[List[Union[str, float, int]], List[List[Union[str, float, int]]]]


class Client:
    _redis: Optional[aioredis.Redis] = None
    _format: str = Format.RESP.value

    def __init__(self, url: str):
        self.url = url

    async def __force_json(self) -> None:
        if self._format == Format.JSON.value:
            return

        response = await self.command_async(Command.OUTPUT.value, [Format.JSON.value])

        parse_response(response)

        self._format = Format.JSON.value

    async def getRedis(self) -> aioredis.Redis:
        if not self._redis:
            self._redis = await aioredis.create_redis_pool(self.url)
            self._format = Format.RESP.value
        return self._redis

    async def command_async(self, command: str, command_args: CommandArgs = []):
        # TODO: use context manager?
        c = await self.getRedis()
        return await c.execute(command, *command_args)

    async def command(
        self, command: str, command_args: CommandArgs = []
    ) -> Dict[str, Union[int, float, str]]:
        await self.__force_json()

        response = await self.command_async(command, command_args)

        return parse_response(response)

    async def quit(self) -> str:
        if not self._redis:
            return "OK"

        c = await self.getRedis()

        c.close()
        await c.wait_closed()

        self._redis = None

        return "OK"
