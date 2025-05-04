from collections.abc import Generator
from typing import Any


def flatten(arr: list[list[Any]] | list[Any]) -> Generator:
    for x in arr:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x
