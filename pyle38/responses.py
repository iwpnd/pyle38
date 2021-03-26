from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class LatLon(BaseModel):
    lat: int
    lon: int


class NeSw(BaseModel):
    ne: LatLon
    sw: LatLon


Fields = Dict[str, int]
Meta = Dict[str, str]


class JSONResponse(BaseModel):
    ok: bool
    elapsed: str
    err: Optional[str] = None


class ObjectResponse(JSONResponse):
    object: Any
    fields: Optional[Fields] = None


class Object(BaseModel):
    object: Any
    id: Union[str, int]
    distance: Optional[float] = None


class ObjectsResponse(JSONResponse):
    objects: List[Object]
    count: int
    cursor: int
    fields: Optional[List[str]] = None


class StringObjectsResponse(JSONResponse):
    objects: List[Object]
    count: int
    cursor: int


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


class Hash(BaseModel):
    hash: str
    id: Union[str, int]
    distance: Optional[float] = None


class HashesResponse(JSONResponse):
    hashes: List[Hash]
    count: int
    cursor: int


class Bounds(BaseModel):
    bounds: NeSw
    id: Union[str, int]
    distance: Optional[float] = None


class BoundsNeSwResponse(JSONResponse):
    bounds: NeSw
    fields: Optional[Fields] = None


class BoundsNeSwResponses(JSONResponse):
    bounds: List[Bounds]
    count: int
    cursor: int


Position = List[float]


class Polygon(BaseModel):
    type = "Polygon"
    coordinates: List[List[Position]]


class BoundsResponse(JSONResponse):
    bounds: Polygon


class KeysResponse(JSONResponse):
    keys: List[str]


class PingResponse(JSONResponse):
    ping = "pong"


class TTLResponse(JSONResponse):
    ttl: Union[str, int]


class Stats(BaseModel):
    in_memory_size: Union[int, float]
    num_objects: Union[int, float]
    num_points: Union[int, float]
    num_strings: Union[int, float]


class StatsResponse(JSONResponse):
    stats: List[Union[Stats, Any]]


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
    tile38_pid: int
    tile38_pointer_size: int
    tile38_read_only: bool
    tile38_total_commands_processed: int
    tile38_total_connections_received: int
    tile38_total_messages_sent: int
    tile38_type: int
    tile38_uptime_in_seconds: int
    tile38_version: int


class ServerStatsExtendedResponse(JSONResponse):
    stats: ServerStatsExtended


ConfigKey = Literal[
    "requirepass", "leaderauth", "protected-mode", "maxmemory", "autogc", "keepalive"
]


class ConfigGetResponse(JSONResponse):
    properties: Dict[ConfigKey, Union[int, float, str]]


class JsonGetResponse(JSONResponse):
    value: Union[int, float, str]


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


class SetChanResponse(JSONResponse):
    chans: List[Chans]


Detect = Literal["enter", "exit", "inside", "outside", "crosses"]

Command = Literal["set", "del"]


class GeoFence(BaseModel):
    command: Command
    group: str
    detect: Detect
    hook: str
    key: str
    time: str
    id: str
    object: Dict
