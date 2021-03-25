from .commands.set import Set
from .follower import Follower


class Leader(Follower):
    async def flush_db(self) -> dict:
        return await self.client.command("FLUSHDB")

    def set(self, key: str, id: str) -> Set:
        return Set(self.client, key, id)
