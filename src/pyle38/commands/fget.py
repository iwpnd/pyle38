from __future__ import annotations

from ..client import Client, Command
from ..responses import FgetResponse
from .executable import Compiled, Executable


class Fget(Executable):
    """Get the value of a specific field of an id.

    Returns None if the field doesn't exist (checked via FEXISTS).
    Returns the actual value (including 0) if the field exists.

    Example::

        key = fleet
        id = truck1
        field = "speed"
        await tile38.set(key, id).point(52.25, 13.37).exec()
        await tile38.fset(key, id, {"speed": 90}).exec()
        response = await tile38.fget(key, id, field).exec()
        # response.value will be 90 or None if field doesn't exist
    """

    _key: str
    _id: str
    _field: str

    def __init__(self, client: Client, key: str, oid: str, field: str) -> None:
        super().__init__(client)

        self.key(key).id(oid).field(field)

    def key(self, key: str) -> Fget:
        """Set key of id to get field from

        Args:
        key (str): key of a collection

        Returns:
            Self
        """
        self._key = key

        return self

    def id(self, oid: str) -> Fget:
        """Set id to get field from

        Args:
        id (str): id of an object

        Returns:
            Self
        """
        self._id = oid

        return self

    def field(self, field: str) -> Fget:
        """Set field to retrieve from object in collection

        Args:
        field (str): Field name to get

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

    async def exec(self) -> FgetResponse:  # type: ignore[override]
        # First check if the field exists using FEXISTS
        fexists_response = await self.client.command(
            Command.FEXISTS.value, [self._key, self._id, self._field]
        )
        
        # Get the field value
        fget_response = await self.client.command(*self.compile())
        
        # If field doesn't exist, set value to None
        if not fexists_response.get("exists", False):
            fget_response["value"] = None
        
        return FgetResponse(**fget_response)

