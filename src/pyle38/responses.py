from typing import Any, ClassVar, Generic, Literal, TypeVar

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict

T = TypeVar("T")
S = TypeVar("S", bound=str)


class BaseModel(PydanticBaseModel):
    def dict(self, exclude_unset: bool = True, **kwargs: Any) -> dict[str, Any]:
        return super().model_dump(exclude_unset=exclude_unset, **kwargs)  # type: ignore[no-any-return,unused-ignore]


class LatLon(BaseModel):
    lat: float
    lon: float
    z: float | None = None


class NeSw(BaseModel):
    ne: LatLon
    sw: LatLon


Fields = dict[str, Any]  # pyright: ignore[reportExplicitAny]
Meta = dict[str, str]


class WithFieldsArray:
    fields: list[Any] | None = None  # pyright: ignore[reportExplicitAny]


class JSONResponse(BaseModel):
    ok: bool
    elapsed: str
    err: str | None = None


class ExistsResponse(JSONResponse, BaseModel):
    exists: bool


class Object(BaseModel, WithFieldsArray, Generic[T]):
    object: T
    id: str | int
    distance: float | None = None


class ObjectResponse(JSONResponse, BaseModel, Generic[T]):
    object: T
    fields: Fields | None = None


class ObjectsResponse(JSONResponse, BaseModel, WithFieldsArray, Generic[T]):
    objects: list[Object[T]] = []
    count: int
    cursor: int


class IdsResponse(JSONResponse):
    ids: list[str]
    count: int
    cursor: int


class CountResponse(JSONResponse):
    count: int
    cursor: int


class PointResponse(JSONResponse):
    point: LatLon
    fields: Fields | None = None


class Point(BaseModel, WithFieldsArray):
    point: LatLon
    id: str | int
    distance: int | None = None


class PointsResponse(JSONResponse, WithFieldsArray):
    points: list[Point] = []
    count: int
    cursor: int


class Hash(BaseModel, WithFieldsArray):
    hash: str
    id: str | int
    distance: float | None = None


class HashResponse(JSONResponse):
    hash: str
    fields: Fields | None = None


class HashesResponse(JSONResponse, WithFieldsArray):
    hashes: list[Hash]
    count: int
    cursor: int


class Bounds(BaseModel, WithFieldsArray):
    bounds: NeSw
    id: str | int
    distance: float | None = None


class BoundsNeSwResponse(JSONResponse):
    bounds: NeSw
    fields: Fields | None = None


class BoundsNeSwResponses(JSONResponse, WithFieldsArray):
    bounds: list[Bounds]
    count: int
    cursor: int


Position = list[float]


class Polygon(BaseModel):
    type: Literal["Polygon"] = "Polygon"
    coordinates: list[list[Position]]


class BoundsResponse(JSONResponse):
    bounds: Polygon


class KeysResponse(JSONResponse):
    keys: list[str]


class TTLResponse(JSONResponse):
    # if no ttl -1
    ttl: float


class Stats(BaseModel):
    in_memory_size: int | float
    num_objects: int | float
    num_points: int | float
    num_strings: int | float


class StatsResponse(JSONResponse):
    stats: list[Stats] | None = []


class ServerStatsLeader(BaseModel):
    aof_size: int | float
    avg_item_size: int | float
    cpus: int | float
    heap_released: int | float
    heap_size: int | float
    http_transport: bool
    id: str
    in_memory_size: int | float
    max_heap_size: int | float
    mem_alloc: int | float
    num_collections: int
    num_hooks: int
    num_objects: int
    num_points: int
    num_strings: int
    pid: int
    pointer_size: int | float
    read_only: bool
    threads: int
    version: str


class ServerStatsFollower(ServerStatsLeader):
    caught_up: bool
    caught_up_once: bool
    following: str


class ServerStatsResponseLeader(JSONResponse):
    stats: ServerStatsLeader


class ServerStatsResponseFollower(JSONResponse):
    stats: ServerStatsFollower


class ServerStatsExtended(BaseModel):
    alloc_bytes: int
    alloc_bytes_total: int
    buck_hash_sys_bytes: int
    frees_total: float
    gc_cpu_fraction: float
    gc_sys_bytes: float
    go_goroutines: int
    go_threads: int
    go_version: str
    heap_alloc_bytes: int
    heap_idle_bytes: int
    heap_inuse_bytes: int
    heap_objects: int
    heap_released_bytes: int
    heap_sys_bytes: int
    last_gc_time_seconds: float
    lookups_total: int
    mallocs_total: int
    mcache_inuse_bytes: int
    mcache_sys_bytes: int
    mspan_inuse_bytes: int
    mspan_sys_bytes: int
    next_gc_bytes: int
    other_sys_bytes: int
    stack_inuse_bytes: int
    stack_sys_bytes: int
    sys_bytes: int
    sys_cpus: int
    tile38_aof_current_rewrite_time_sec: int
    tile38_aof_enabled: bool
    tile38_aof_last_rewrite_time_sec: int
    tile38_aof_rewrite_in_progress: bool
    tile38_aof_size: int
    tile38_avg_point_size: int
    tile38_cluster_enabled: bool
    tile38_connected_clients: int
    tile38_connected_slaves: int
    tile38_expired_keys: int
    tile38_http_transport: bool
    tile38_id: str
    tile38_in_memory_size: int
    tile38_max_heap_size: int
    tile38_num_collections: int
    tile38_num_hooks: int
    tile38_num_objects: int
    tile38_num_points: int
    tile38_num_strings: int
    tile38_num_object_groups: int
    tile38_num_hook_groups: int
    tile38_pid: int
    tile38_pointer_size: int
    tile38_read_only: bool
    tile38_total_commands_processed: int
    tile38_total_connections_received: int
    tile38_total_messages_sent: int
    tile38_type: str
    tile38_uptime_in_seconds: float
    tile38_version: str


class ServerStatsExtendedResponse(JSONResponse):
    stats: ServerStatsExtended


ConfigKeys = Literal[
    "requirepass", "leaderauth", "protected-mode", "maxmemory", "autogc", "keepalive"
]


class ConfigGetResponse(JSONResponse):
    properties: dict[ConfigKeys, str]


class JSONGetResponse(JSONResponse):
    value: int | float | str | None = "{}"


class Hooks(BaseModel):
    name: str
    endpoints: list[str]
    key: str
    meta: dict[str, Any]  # pyright: ignore[reportExplicitAny]
    command: list[str]


class HooksResponse(JSONResponse):
    hooks: list[Hooks]


class Chans(BaseModel):
    name: str
    key: str
    meta: dict[str, Any]  # pyright: ignore[reportExplicitAny]
    command: list[str]


class ChansResponse(JSONResponse):
    chans: list[Chans]


class PingResponse(JSONResponse):
    ping: Literal["pong"] = "pong"


FenceDetect = Literal["enter", "exit", "inside", "outside", "crosses"]
FenceCommand = Literal["set", "del"]


class GeoFence(BaseModel, Generic[T]):
    command: FenceCommand
    group: str
    detect: FenceDetect
    hook: str
    key: str
    time: str
    id: str
    object: T


class Info(BaseModel):
    aof_current_rewrite_time_sec: int
    aof_enabled: int
    aof_last_rewrite_time_sec: int
    aof_rewrite_in_progress: int
    cluster_enabled: int
    connected_clients: int
    connected_slaves: int
    expired_keys: int
    redis_version: str
    role: Literal["master", "slave"]
    tile38_version: str
    total_messages_sent: int
    total_connections_received: int
    total_commands_processed: int
    uptime_in_seconds: int
    used_cpu_sys: int
    used_cpu_sys_children: int
    used_cpu_user: int
    used_cpu_user_children: int
    used_memory: int


class InfoFollower(Info):
    master_host: str
    master_port: int


class InfoLeader(Info):
    # to allow for additional slaves
    # slave0, slave1..
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow")


class InfoFollowerResponse(JSONResponse):
    info: InfoFollower


class InfoLeaderResponse(JSONResponse):
    info: InfoLeader
