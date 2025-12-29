from __future__ import annotations

from pyle38.errors import Tile38FieldNotFoundError
from pyle38.responses import JSONGetResponse

from ..client import Client, Command
from .executable import Compiled


class FGet:
    """Get the value for a field of an id.

    Example::

        key = fleet
        id = truck1
        fields = {"driver":"John"}
        await tile38.set(key, id).point(52.25, 13.37).exec()
        await tile38.fget(key, id, "driver")
    """

    _client: Client
    _key: str
    _id: str
    _field: str

    def __init__(self, client: Client, key: str, oid: str, field: str) -> None:
        self.client = client
        self.key(key).id(oid).field(field)

    def key(self, key: str) -> FGet:
        """Set key of id to get field for

        Args:
        key (str): key of a collection

        Returns:
            Self
        """
        self._key = key

        return self

    def id(self, oid: str) -> FGet:
        """Set id to get field for

        Args:
        id (str): id of an object

        Returns:
            Self
        """
        self._id = oid

        return self

    def field(self, field: str) -> FGet:
        """Set field to get

        Args:
        field (str): field name of an object

        Returns:
            Self
        """
        self._field = field

        return self

    def compile(self) -> Compiled:
        return [
            Command.FGET.value,
            [
                self._key,
                self._id,
                self._field,
            ],
        ]  # type: ignore

    async def exec(self) -> JSONGetResponse:
        """Execute the FGet command with input parameters.

        Zero Value fields that return as {"ok":true,"value":0} from Tile38
        are fields that are not set with Tile38, hence we know they do not exist
        and can raise a Tile38FieldNotFoundError.

        Args:
        field (str): field name of an object

        Returns:
            Self
        """
        resp = await self.client.command(*self.compile())

        if resp["ok"] and resp["value"] == 0:
            msg = "field not found"
            raise Tile38FieldNotFoundError(msg)

        return JSONGetResponse(**resp)
