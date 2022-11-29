from typing import Any, Dict, Generic, List, Literal, Optional, TypeVar, Union

from pydantic import BaseModel as PydanticBaseModel
from pydantic.generics import GenericModel as PydanticGenericModel

T = TypeVar("T")
S = TypeVar("S", bound=str)


class GenericModel(PydanticGenericModel):
    def dict(self, exclude_unset=True, **kwargs):
        return super().dict(exclude_unset=exclude_unset, **kwargs)


class BaseModel(PydanticBaseModel):
    def dict(self, exclude_unset=True, **kwargs):
        return super().dict(exclude_unset=exclude_unset, **kwargs)


class LatLon(BaseModel):
    lat: float
    lon: float


class NeSw(BaseModel):
    ne: LatLon
    sw: LatLon


Fields = Dict[str, Any]
Meta = Dict[str, str]


class JSONResponse(BaseModel):
    ok: bool
    elapsed: str
    err: Optional[str] = None


class Object(GenericModel, Generic[T]):
    object: T
    id: Union[str, int]
    distance: Optional[float] = None
    fields: Optional[List[int]] = None


class ObjectResponse(JSONResponse, GenericModel, Generic[T]):
    object: T
    fields: Optional[Fields] = None


class ObjectsResponse(JSONResponse, GenericModel, Generic[T]):
    objects: List[Object[T]] = []
    count: int
    cursor: int
    fields: Optional[List[str]] = None


class IdsResponse(JSONResponse):
    ids: List[str]
    count: int
    cursor: int


class CountResponse(JSONResponse):
    count: int
    cursor: int


class PointResponse(JSONResponse):
    point: LatLon
    fields: Optional[Fields] = None


class Point(BaseModel):
    point: LatLon
    id: Union[str, int]
    distance: Optional[int] = None
    fields: Optional[List[Any]] = None


class PointsResponse(JSONResponse):
    points: List[Point] = []
    count: int
    cursor: int
    fields: Optional[List[str]] = None


class Hash(BaseModel):
    hash: str
    id: Union[str, int]
    distance: Optional[float] = None
    fields: Optional[List[Any]]


class HashResponse(JSONResponse):
    hash: str
    fields: Optional[Fields] = None


class HashesResponse(JSONResponse):
    hashes: List[Hash]
    count: int
    cursor: int
    fields: Optional[List[str]] = None


class Bounds(BaseModel):
    bounds: NeSw
    id: Union[str, int]
    distance: Optional[float] = None
    fields: Optional[List[Any]] = None


class BoundsNeSwResponse(JSONResponse):
    bounds: NeSw
    fields: Optional[Fields] = None


class BoundsNeSwResponses(JSONResponse):
    bounds: List[Bounds]
    count: int
    cursor: int
    fields: Optional[List[str]] = None


Position = List[float]


class Polygon(BaseModel):
    type = "Polygon"
    coordinates: List[List[Position]]


class BoundsResponse(JSONResponse):
    bounds: Polygon


class KeysResponse(JSONResponse):
    keys: List[str]


class TTLResponse(JSONResponse):
    # if no ttl -1
    ttl: float


class Stats(BaseModel):
    in_memory_size: Union[int, float]
    num_objects: Union[int, float]
    num_points: Union[int, float]
    num_strings: Union[int, float]


class StatsResponse(JSONResponse):
    stats: Optional[List[Stats]] = []


class ServerStatsLeader(BaseModel):
    aof_size: Union[int, float]
    avg_item_size: Union[int, float]
    cpus: Union[int, float]
    heap_released: Union[int, float]
    heap_size: Union[int, float]
    http_transport: bool
    id: str
    in_memory_size: Union[int, float]
    max_heap_size: Union[int, float]
    mem_alloc: Union[int, float]
    num_collections: int
    num_hooks: int
    num_objects: int
    num_points: int
    num_strings: int
    pid: int
    pointer_size: Union[int, float]
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
    frees_total: Union[int, float]
    gc_cpu_fraction: int
    gc_sys_bytes: int
    go_goroutines: int
    go_threads: int
    go_version: str
    heap_alloc_bytes: int
    heap_idle_bytes: int
    heap_inuse_bytes: int
    heap_objects: int
    heap_released_bytes: int
    heap_sys_bytes: int
    last_gc_time_seconds: int
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
    tile38_uptime_in_seconds: int
    tile38_version: str


class ServerStatsExtendedResponse(JSONResponse):
    stats: ServerStatsExtended


ConfigKeys = Literal[
    "requirepass", "leaderauth", "protected-mode", "maxmemory", "autogc", "keepalive"
]


class ConfigGetResponse(JSONResponse):
    properties: Dict[ConfigKeys, Union[int, float, str]]


class JSONGetResponse(JSONResponse):
    value: Optional[Union[int, float, str]] = "{}"


class Hooks(BaseModel):
    name: str
    endpoints: List[str]
    key: str
    meta: Dict
    command: List[str]


class HooksResponse(JSONResponse):
    hooks: List[Hooks]


class Chans(BaseModel):
    name: str
    key: str
    meta: Dict
    command: List[str]


class ChansResponse(JSONResponse):
    chans: List[Chans]


class PingResponse(JSONResponse):
    ping: Literal["pong"] = "pong"


FenceDetect = Literal["enter", "exit", "inside", "outside", "crosses"]
FenceCommand = Literal["set", "del"]


class GeoFence(GenericModel, Generic[T]):
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
    master_port: str


class InfoLeader(Info):
    # to allow for additional slaves
    # slave0, slave1..
    class Config:
        extra = "allow"


class InfoFollowerResponse(JSONResponse):
    info: InfoFollower


class InfoLeaderResponse(JSONResponse):
    info: InfoLeader
