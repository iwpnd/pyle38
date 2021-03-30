import os
from typing import Optional

from .errors import Tile38Error
from .follower import Follower
from .leader import Leader


class Tile38(Leader):

    _follower: Optional[Follower] = None

    # TODO: get url from os.getenv
    def __init__(
        self,
        url=os.getenv("TILE38_LEADER_URI"),
        follower_url=os.getenv("TILE38_FOLLOWER_URI"),
    ):
        if not url:
            raise Tile38Error("No Tile38 url set")

        super().__init__(url)

        if follower_url:
            self._follower = Follower(follower_url)

    def follower(self) -> Follower:
        if not self._follower:
            raise Tile38Error("No follower")

        return self._follower

    async def quit(self) -> str:
        if self._follower:
            await self.follower().quit()

        await super().quit()

        return "OK"
