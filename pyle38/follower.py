from .client import Client
from .commands.get import Get


class Follower(Client):
    client: Client

    def __init__(self, url: str) -> None:
        super().__init__(url)

        self.client = Client(url)

    def get(self, key: str, id: str) -> Get:
        return Get(self.client, key, id)
