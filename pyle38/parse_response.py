import json
from typing import Dict
from typing import Union

from .errors import Tile38Error
from .errors import Tile38IdNotFoundError
from .errors import Tile38KeyNotFoundError


def parse_response(response: str) -> Dict[str, Union[float, int, str]]:

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

        raise Tile38Error(msg)

    return obj
