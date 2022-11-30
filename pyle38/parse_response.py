import json
from typing import Dict, List, Optional, Union

from redis.typing import EncodableT

from .errors import (
    Tile38Error,
    Tile38IdNotFoundError,
    Tile38KeyNotFoundError,
    Tile38NotCaughtUpError,
    Tile38PathNotFoundError,
)


def parse_response(
    response: Optional[
        Union[bytes, memoryview, str, int, float, List[EncodableT], None]
    ] = None
) -> Dict[str, Union[float, str, int, list, dict]]:
    if not isinstance(response, str) or isinstance(response, bytes):
        raise Tile38Error("invalid response")

    try:
        obj = json.loads(response)
    except Exception as e:
        raise Tile38Error(e)

    msg = "unknown"

    if not obj["ok"]:
        msg = obj["err"]

        if "key not found" in msg:
            raise Tile38KeyNotFoundError(msg)

        if "id not found" in msg:
            raise Tile38IdNotFoundError(msg)

        if "not caught up" in msg:
            raise Tile38NotCaughtUpError(msg)

        if "path not found" in msg:
            raise Tile38PathNotFoundError(msg)

        raise Tile38Error(msg)

    return obj
