from typing import Any, Generator, List, Union


def flatten(arr: Union[List[List[Any]], List[Any]]) -> Generator:
    for x in arr:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            for y in flatten(x):
                yield y
        else:
            yield x
