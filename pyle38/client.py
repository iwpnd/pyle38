import os
from typing import Dict
from typing import List
from typing import Union

import aioredis

from .parse_response import parse_response


class Client:
    _redis = None
    _format: str = "RESP"

    async def __force_json(self) -> None:
        if self._format == "JSON":
            return

        response = await self.command_async("OUTPUT", ["JSON"])

        parse_response(response)

        self._format = "JSON"

    async def getRedis(self) -> aioredis.Redis:
        if not self._redis:
            self._redis = await aioredis.create_redis(os.getenv("TILE38_URI"))
        return self._redis

    async def command_async(
        self, command: str, command_args: List[Union[float, int, str]] = []
    ):
        c = await self.getRedis()
        return await c.execute(command, *command_args)

    async def command(
        self, command: str, command_args: List[Union[float, int, str]] = []
    ) -> Dict[str, Union[int, float, str]]:
        await self.__force_json()

        response = await self.command_async(command, command_args)

        return parse_response(response)

    async def quit(self) -> str:
        c = await self.getRedis()

        await c.quit()

        return "OK"
