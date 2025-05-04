import abc
from typing import Any

from ..client import Client, Command, CommandArgs

Compiled = tuple[Command, CommandArgs]


class Executable(abc.ABC):
    """Executable is an abstract base class for Tile38-style command execution."""

    client: Client

    def __init__(self, client: Client) -> None:
        """__init__.

        Args:
            client (Client): The client instance used to communicate with the backend.

        Returns:
            None
        """
        self.client = client

    def compile(self) -> Compiled:
        """compile.

        This method should be overridden by subclasses to provide the command and its arguments.

        Returns:
            Compiled: A tuple containing the Command and its associated arguments.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        raise NotImplementedError("Not implemented")

    async def exec(self) -> dict[Any, Any]:
        """exec.

        Executes the compiled command asynchronously using the associated client.

        Returns:
            dict[Any, Any]: The response from the client command execution.
        """
        return await self.client.command(*self.compile())
