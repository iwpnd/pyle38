from collections.abc import Callable, Sequence
from enum import Enum
from typing import Any

from redis.asyncio import Connection, Redis
from redis.asyncio.connection import parse_url

from .client_options import ClientOptions
from .parse_response import parse_response

TILE38_DEFAULT_HOST = "localhost"
TILE38_DEFAULT_PORT = 9851


class Command(str, Enum):
    AOFSHRINK = "AOFSHRINK"
    AUTH = "AUTH"
    BOUNDS = "BOUNDS"
    CHANS = "CHANS"
    CONFIG = "CONFIG"
    DELCHAN = "DELCHAN"
    DEL = "DEL"
    DELHOOK = "DELHOOK"
    DROP = "DROP"
    EXISTS = "EXISTS"
    EXPIRE = "EXPIRE"
    FEXISTS = "FEXISTS"
    FLUSHDB = "FLUSHDB"
    FGET = "FGET"
    FSET = "FSET"
    GC = "GC"
    GET = "GET"
    HEALTHZ = "HEALTHZ"
    HOOKS = "HOOKS"
    INFO = "INFO"
    INTERSECTS = "INTERSECTS"
    JDEL = "JDEL"
    JGET = "JGET"
    JSET = "JSET"
    KEYS = "KEYS"
    NEARBY = "NEARBY"
    OUTPUT = "OUTPUT"
    PDELCHAN = "PDELCHAN"
    PDELHOOK = "PDELHOOK"
    PDEL = "PDEL"
    PERSIST = "PERSIST"
    PING = "PING"
    READONLY = "READONLY"
    RENAMENX = "RENAMENX"
    RENAME = "RENAME"
    SCAN = "SCAN"
    SEARCH = "SEARCH"
    SERVER = "SERVER"
    SETCHAN = "SETCHAN"
    SETHOOK = "SETHOOK"
    SET = "SET"
    STATS = "STATS"
    TTL = "TTL"
    WITHIN = "WITHIN"


class SubCommand(str, Enum):
    FIELD = "FIELD"
    EX = "EX"
    NX = "NX"
    XX = "XX"
    WITHFIELDS = "WITHFIELDS"
    CURSOR = "CURSOR"
    LIMIT = "LIMIT"
    NOFIELDS = "NOFIELDS"
    MATCH = "MATCH"
    OBJECT = "OBJECT"
    TILE = "TILE"
    QUADKEY = "QUADKEY"
    HASH = "HASH"
    BOUNDS = "BOUNDS"
    GET = "GET"
    CIRCLE = "CIRCLE"
    POINT = "POINT"
    OBJECTS = "OBJECTS"
    HASHES = "HASHES"
    IDS = "IDS"
    COUNT = "COUNT"
    POINTS = "POINTS"
    STRING = "STRING"
    META = "META"
    FENCE = "FENCE"
    DETECT = "DETECT"
    COMMANDS = "COMMANDS"
    REWRITE = "REWRITE"
    ASC = "ASC"
    DESC = "DESC"
    EXT = "EXT"
    WHERE = "WHERE"
    WHEREIN = "WHEREIN"
    SECTOR = "SECTOR"


class Format(str, Enum):
    JSON = "JSON"
    RESP = "RESP"


CommandArg = str | float | int
CommandArgs = Sequence[CommandArg] | Sequence[Sequence[CommandArg]]

NO_RESPONSE_CALLBACKS_FOR = [
    Command.SET,
    Command.SCAN,
    Command.RENAME,
    Command.RENAMENX,
    Command.PING,
    Command.PERSIST,
    Command.INFO,
    Command.EXPIRE,
    Command.FLUSHDB,
    Command.DEL,
    Command.READONLY,
]


class Client:
    """
    A class to manage the connection and communication with a Tile38 instance using Redis.

    Attributes:
        url (str): The connection URL for the Tile38 instance.
        __redis (Optional[redis.Redis]): A Redis connection object (initialized as None).
        __client_options (ClientOptions): Configuration options for the Redis client.
    """

    __redis = None
    __client_options: ClientOptions
    __url = ""

    def __init__(
        self, url: str, options: list[Callable[..., ClientOptions]] | None = None
    ) -> None:
        """Initialize the Client.

        Args:
            url (str): The URL for connecting to the Tile38 server.
            options (List[Callable[..., ClientOptions]], optional): A list of callables that modify client options.

        Returns:
            None
        """
        self.__url = url
        self.__redis = None
        self.__client_options = {}

        default_options: list[Callable[..., ClientOptions]] = []
        if options:
            default_options.extend(options)

        for option in default_options:
            self.__client_options = option(self.__client_options)

    @property
    def url(self) -> str:
        """The client url

        Returns:
            str: returns the clients url
        """
        return self.__url

    def client_options(self) -> ClientOptions:
        """Get the current ClientOptions.

        Returns:
            ClientOptions: The current configuration options for the client.
        """
        return self.__client_options

    async def __on_connect(self, connection: Connection) -> None:
        """Callback executed upon connection to Redis.

        Sets the OUTPUT format to JSON.

        Args:
            connection (redis.Connection): The Redis connection instance.

        Returns:
            None
        """
        await connection.on_connect()
        await connection.send_command(Command.OUTPUT, Format.JSON)
        await connection.read_response()  # pyright: ignore[reportUnusedCallResult]

    async def __delete_response_callbacks(self) -> None:
        """Delete unnecessary response callbacks in redis-py.

        This removes default callbacks for certain commands that cause issues with Tile38.
        These commands are specified in NO_RESPONSE_CALLBACKS_FOR.

        Returns:
            None
        """
        r = await self.__get_redis()
        for command in NO_RESPONSE_CALLBACKS_FOR:
            try:
                del r.response_callbacks[command]
            except KeyError:
                continue

    async def __get_redis(self) -> Redis:
        """Establish or retrieve the Redis connection.

        This method acts as a singleton for the Redis connection, ensuring that only one connection
        is maintained. It sets up the connection with specified host, port, and client options.

        Returns:
            redis.Redis: The Redis connection instance.
        """
        if not self.__redis:
            url_components = parse_url(self.__url)
            host: str = url_components.get("host") or TILE38_DEFAULT_HOST
            port: int = url_components.get("port") or TILE38_DEFAULT_PORT

            r: Redis = Redis(
                host=host,
                port=port,
                encoding="utf-8",
                single_connection_client=True,
                decode_responses=True,
                redis_connect_func=self.__on_connect,
                **self.__client_options,
            )

            self.__redis = r

            # Remove unnecessary response callbacks specific to Tile38
            await self.__delete_response_callbacks()

        return self.__redis

    async def __execute_and_read_response(  # pyright: ignore[reportUnknownParameterType]
        self, command: str, command_args: CommandArgs | None
    ) -> Any:
        """Execute a command and read its response from Redis.

        Args:
            command (str): The command to execute.
            command_args (CommandArgs, optional): Arguments for the command.

        Returns:
            Any: The response from the Redis server.
        """
        command_args = command_args if command_args else []
        r = await self.__get_redis()
        return await r.execute_command(command, *command_args)

    async def command(
        self, command: str, command_args: CommandArgs | None = None
    ) -> dict:
        """Send a command to Tile38 and parse the response.

        Args:
            command (str): The command to execute on the Tile38 server.
            command_args (CommandArgs, optional): Arguments for the command.

        Returns:
            Dict: The parsed response from the server.
        """
        if not command_args:
            command_args = []

        response = await self.__execute_and_read_response(command, command_args)
        return parse_response(response)

    async def quit(self) -> str:
        """Terminate the Redis connection.

        Closes the connection to the Tile38 instance and resets the Redis client.

        Returns:
            str: A confirmation message ("OK") upon successful termination.
        """
        if not self.__redis:
            return "OK"

        c = await self.__get_redis()

        # TODO: remove ignore once types have been updated
        await c.aclose()  # type: ignore[attr-defined]
        await c.connection_pool.disconnect()

        self.__redis = None

        return "OK"
