from __future__ import annotations

from typing import List, Literal, Optional, Sequence, Union

from ..client import Client, Command, CommandArgs, SubCommand
from ..errors import Tile38Error
from ..models import Options, PointQuery
from ..responses import (
    BoundsNeSwResponses,
    CountResponse,
    FenceCommand,
    FenceDetect,
    HashesResponse,
    IdsResponse,
    JSONResponse,
    ObjectsResponse,
    PointsResponse,
)
from ..utils import flatten
from .executable import Compiled, Executable
from .whereable import Whereable

Format = Literal["BOUNDS", "COUNT", "HASHES", "IDS", "OBJECTS", "POINTS"]
Output = Sequence[Union[Format, int]]


class Nearby(Executable, Whereable):
    """Nearby searches a key for objects that are close by."""

    _key: str
    _command: Literal["NEARBY"]
    _hook = None
    _options: Options = {}
    _query: PointQuery
    _output: Optional[Output] = None
    _all: bool = False
    _fence: bool = False
    _detect: Optional[List[FenceDetect]] = []
    _commands: Optional[List[FenceCommand]] = []

    def __init__(self, client: Client, key: str, hook=None) -> None:
        """__init__.

        Args:
            client (Client): client
            key (str): key to search in
            hook: Endpoint to send events to
                Options: AMQP, KAFKA, HTTPS/HTTP, SQS, MQTT, NATS, gRPC, Redis

        Returns:
            None
        """
        super().__init__(client)

        self.key(key)
        self._options = {}
        self._hook = hook
        self._where = []

    def key(self, key: str) -> Nearby:
        """Set key to search in

        Args:
            key (str): key of a collection to search in

        Returns:
            Nearby
        """
        self._key = key

        return self

    def cursor(self, value: int) -> Nearby:
        """Cursor used to iterate though objects of the search results.

        Used for pagination through search results.

        Args:
            value (int): cursor value to start at, default: 0 if not set

        Returns:
            Nearby
        """
        self._options["cursor"] = value

        return self

    def fence(self, flag: bool = True) -> Nearby:
        """Flag to indicate that the Nearby Query is used for a geo fence.

        Args:
            flag (bool): defaults to True if not set

        Returns:
            Nearby
        """
        self._fence = flag

        return self

    def detect(self, what: List[FenceDetect]) -> Nearby:
        """Option to filter the type of events in a geo fence.

        Args:
            what (List[FenceDetect]): what to detect in geo fence events.
                defaults to 'enter,exit,outside,inside,crosses' if not set

        Returns:
            Nearby
        """
        self._detect = what if len(what) > 0 else []

        return self

    def commands(self, which: Optional[List[FenceCommand]] = []) -> Nearby:
        """Option to filter what commands should be triggering a geo fence event.

        Args:
            which (Optional[List[FenceCommand]]): which commands trigger a geo fence
            event defaults to 'SET,DEL,JSET,JDEL' if not set

        Returns:
            Nearby
        """
        if which and len(which) > 0:
            self._commands = which

        return self

    def limit(self, value: int) -> Nearby:
        """Limit the number of returned objects in a search.

        Also used for pagination through search results.

        Args:
            value (int): limit value, defaults to 100 if not set

        Returns:
            Nearby
        """
        self._options["limit"] = value

        return self

    def nofields(self, flag: bool = True) -> Nearby:
        """Option to explicitly not return fields in search results.

        Args:
            flag (bool): flag

        Returns:
            Nearby
        """
        self._options["nofields"] = flag

        return self

    def match(self, value: str) -> Nearby:
        """Match can be used to filtered objects considered in the search with a
        glob pattern.

        Args:
            value (str): value

        Returns:
            Nearby
        """
        self._options["match"] = value

        return self

    def sparse(self, value: int) -> Nearby:
        """Instead of returning all results of a search. Return a sparse result evenly
        distributed in the given search area. EXPERIMENTAL

        Args:
            value (int): values between 1 and 8

        Returns:
            Nearby
        """
        self._options["sparse"] = value

        return self

    def distance(self, flag: bool = True) -> Nearby:
        """Return haversine distance to found objects

        Args:
            flag (bool): flag

        Returns:
            Nearby
        """
        self._options["distance"] = flag

        return self

    def point(self, lat: float, lon: float, radius: Optional[float] = None) -> Nearby:
        """Define a point as input bounding area for the nearby search.

        Args:
            lat (float): center latitude of point
            lon (float): center longitude of point
            radius (float): radius of point

        Returns:
            Nearby
        """
        self._query = PointQuery(lat=lat, lon=lon, radius=radius)

        return self

    def output(self, format: Format, precision: Optional[int] = None) -> Nearby:
        """Define an output format for query results.

        Args:
            format (Format): format,
                eg. 'OBJECTS', 'HASHES', 'BOUNDS', 'COUNT', 'IDS', 'POINTS'
            precision (Optional[int]): precision

        Returns:
            Nearby
        """
        if format == "OBJECTS":
            self._output = None
        elif format == "HASHES" and precision:
            self._output = [format, precision]
        elif format == "BOUNDS":
            self._output = [format]
        elif format == "COUNT":
            self._output = [format]
        elif format == "IDS":
            self._output = [format]
        elif format == "POINTS":
            self._output = [format]

        return self

    async def asObjects(self) -> ObjectsResponse:
        """Return query results as objects.

        Args:

        Returns:
            ObjectsResponse
        """
        self.output("OBJECTS")

        return ObjectsResponse(**(await self.exec()))

    async def asBounds(self) -> BoundsNeSwResponses:
        """Return query results as bounds.

        Args:

        Returns:
            BoundsNeSwResponses
        """
        self.output("BOUNDS")

        return BoundsNeSwResponses(**(await self.exec()))

    async def asHashes(self, precision: int) -> HashesResponse:
        """Return query results as geohashes.

        Args:
            precision (int): precision of the returned geohash

        Returns:
            HashesResponse
        """
        self.output("HASHES", precision)

        return HashesResponse(**(await self.exec()))

    async def asCount(self) -> CountResponse:
        """Return query results as count only.

        Args:

        Returns:
            CountResponse
        """
        self.output("COUNT")

        return CountResponse(**(await self.exec()))

    async def asIds(self) -> IdsResponse:
        """Return query results as object ids only.

        Args:

        Returns:
            IdsResponse
        """
        self.output("IDS")

        return IdsResponse(**(await self.exec()))

    async def asPoints(self) -> PointsResponse:
        """Return query results as points.

        Args:

        Returns:
            PointsResponse
        """
        self.output("POINTS")

        return PointsResponse(**(await self.exec()))

    def __compile_options(self) -> CommandArgs:
        """__compile_options.

        Args:

        Returns:
            CommandArgs
        """
        commands = []

        # raises mypy: TypedDict key must be string literal
        # open PR: https://github.com/python/mypy/issues/7867
        for k in self._options.keys():
            if isinstance(self._options[k], bool):  # type: ignore
                commands.append(k.upper())
            elif self._options[k]:  # type: ignore
                commands.extend([k.upper(), self._options[k]])  # type: ignore
            elif self._options[k] == 0:  # type: ignore
                commands.extend([k.upper(), self._options[k]])  # type: ignore

        return commands

    def __compile_fence(self) -> CommandArgs:
        """__compile_fence

        Args:

        Returns:
            CommandArgs
        """
        return (
            [
                SubCommand.FENCE.value,
                *(
                    [SubCommand.DETECT.value, ",".join(self._detect)]
                    if self._detect
                    else []
                ),
                *(
                    [SubCommand.COMMANDS.value, ",".join(self._commands)]
                    if self._commands
                    else []
                ),
            ]
            if self._fence
            else []
        )

    def compile(self) -> Compiled:
        """compile

        Args:

        Returns:
            Compiled
        """
        compiled = [
            Command.NEARBY.value,
            [
                self._key,
                *(self.__compile_options()),
                *(self.compile_where()),
                *(self.__compile_fence()),
                *(self._output if self._output else []),
                *(self._query.get()),
            ],
        ]

        if self._hook:
            command, args = self._hook.compile()
            return [command, [*(args), *(flatten(compiled))]]

        return compiled

    async def activate(self) -> JSONResponse:  # type: ignore
        """Activate is used in SetHook to activate a geo-fenced search.

        Args:

        Returns:
            JSONResponse
        """
        if self._hook:
            return JSONResponse(**(await self.client.command(*self.compile())))
        else:
            raise Tile38Error("No hook to activate")
