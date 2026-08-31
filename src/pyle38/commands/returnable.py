from typing import Literal, Self

from pyle38.client import Client
from pyle38.commands.executable import Compiled, Executable
from pyle38.responses import (
    BoundsNeSwResponse,
    HashResponse,
    ObjectResponse,
    PointResponse,
)

Formats = Literal["BOUNDS", "HASH", "OBJECT", "POINT", "STRING"]
Output = list[Formats | int]


class Returnable(Executable):
    """Returnable is class for defining Tile38 returnables."""

    _output: Output

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def output(self, fmt: Formats, precision: int | None = None) -> Self:
        self._output = [fmt]
        if fmt == "HASH" and precision:
            self._output = [fmt, precision]

        return self

    def compile(self) -> Compiled:
        raise NotImplementedError()

    async def asObject(self) -> ObjectResponse:
        """Return query results as objects.

        Args:

        Returns:
            ObjectsResponse
        """
        self.output("OBJECT")
        return ObjectResponse(**(await self.client.command(*self.compile())))

    async def asBounds(self) -> BoundsNeSwResponse:
        """Return query result as bounds.

        Args:

        Returns:
            BoundsNeSwResponse
        """
        self.output("BOUNDS")

        return BoundsNeSwResponse(**(await self.client.command(*self.compile())))

    async def asHash(self, precision: int) -> HashResponse:
        """Return query result as geohash.

        Args:
            precision (int): precision of the returned geohash

        Returns:
            HashesResponse
        """
        self.output("HASH", precision)

        return HashResponse(**(await self.client.command(*self.compile())))

    async def asPoint(self) -> PointResponse:
        """Return query result as point.

        Args:

        Returns:
            PointResponse
        """
        self.output("POINT")

        return PointResponse(**(await self.client.command(*self.compile())))

    async def asStringObject(self) -> ObjectResponse[str]:
        """Return query result as string object.

        Args:

        Returns:
            StringResponse[str]
        """
        self.output("OBJECT")

        return ObjectResponse[str](**(await self.client.command(*self.compile())))
