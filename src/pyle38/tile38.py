import os
from collections.abc import Callable

from pyle38.client_options import ClientOptions

from .errors import Pyle38NoFollowerSetError, Pyle38NoLeaderSetError
from .follower import Follower
from .leader import Leader

TILE38_LEADER_URI: str | None = os.getenv("TILE38_LEADER_URI")
TILE38_FOLLOWER_URI: str | None = os.getenv("TILE38_FOLLOWER_URI")


class Tile38(Leader):
    """
    A class to manage a Tile38 leader instance with optional follower support.

    Attributes:
        __follower (Optional[Follower]): A private attribute holding the follower instance if a follower URL is provided.
    """

    __follower: Follower | None = None

    def __init__(
        self,
        url: str | None = TILE38_LEADER_URI,
        follower_url: str | None = TILE38_FOLLOWER_URI,
        options: list[Callable[..., ClientOptions]] = [],
    ) -> None:
        """Initialize the Tile38 leader and optional follower.

        Args:
            url (str, optional): The URL for the Tile38 leader instance.
                Defaults to the environment variable `TILE38_LEADER_URI`.
            follower_url (str, optional): The URL for the Tile38 follower instance.
                Defaults to the environment variable `TILE38_FOLLOWER_URI`.
            options (List[Callable[..., ClientOptions]], optional): A list of callables
                that return client options for configuring the Tile38 connection.

        Raises:
            Tile38Error: If the leader URL is not provided.

        Returns:
            None
        """
        if not url:
            raise Pyle38NoLeaderSetError

        super().__init__(url, options)

        if follower_url:
            self.__follower = Follower(follower_url, options)

    def follower(self) -> Follower:
        """Get the Tile38 follower instance.

        Raises:
            Tile38Error: If the follower instance is not available.

        Returns:
            Follower: The follower instance.
        """
        if not self.__follower:
            raise Pyle38NoFollowerSetError

        return self.__follower

    async def quit(self) -> str:
        """Asynchronously quit the Tile38 leader and follower connections.

        This method first quits the follower connection (if available),
        followed by quitting the leader connection.

        Returns:
            str: A confirmation message ("OK") upon successful termination.
        """
        if self.__follower:
            await self.follower().quit()

        await super().quit()

        return "OK"
