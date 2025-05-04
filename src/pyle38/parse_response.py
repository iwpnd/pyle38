import json

from redis.typing import EncodableT

from .errors import (
    Tile38Error,
    Tile38IdNotFoundError,
    Tile38KeyNotFoundError,
    Tile38NotCaughtUpError,
    Tile38PathNotFoundError,
)


def parse_response(
    response: bytes
    | memoryview
    | str
    | int
    | float
    | list[EncodableT]
    | None
    | None = None,
) -> dict[str, float | str | int | list | dict]:
    if not isinstance(response, str) or isinstance(response, bytes):
        raise Tile38Error("invalid response")  # noqa: TRY003

    try:
        obj = json.loads(response)
    except Exception as e:
        raise Tile38Error(e) from e

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

    return obj  # type:ignore[no-any-return]
