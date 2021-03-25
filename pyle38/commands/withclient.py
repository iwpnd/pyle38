from ..client import Client


class WithClient:

    client: Client

    def __init__(self, client: Client) -> None:
        self.client = client
