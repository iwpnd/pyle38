from .client import Client
from .client import Command


class Follower(Client):
    client: Client

    def __init__(self, url: str) -> None:
        super().__init__(url)

        self.client = Client(url)

    async def get(self, key: str, id: str):
        return await self.client.command(Command.GET, [key, id])
