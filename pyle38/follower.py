from .client import Client
from .client import Command
from .commands.get import Get
from .responses import BoundsResponse


class Follower(Client):
    client: Client

    def __init__(self, url: str) -> None:
        super().__init__(url)

        self.client = Client(url)

    async def bounds(self, key: str) -> BoundsResponse:
        return BoundsResponse(
            **(await self.client.command(Command.BOUNDS.value, [key]))
        )

    def get(self, key: str, id: str) -> Get:
        return Get(self.client, key, id)
