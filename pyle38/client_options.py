from typing import Callable, List

from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from typing_extensions import NotRequired, TypedDict

from .errors import Pyle38Error

Pyle38Retry = Retry
Pyle38ExponentialBackoff = ExponentialBackoff

ClientOptions = TypedDict(
    "ClientOptions",
    {
        "retry": NotRequired[Pyle38Retry],
        "retry_on_error": NotRequired[List[type[Pyle38Error]]],
    },
)


def WithRetryExponentialBackoff(retries: int) -> Callable[..., ClientOptions]:
    try:
        t = int(retries)
    except ValueError:
        raise ValueError("Retries must be a positive integer")

    if t < 0:
        raise ValueError("Retries must be a positive integer")

    def _with_retry_exponential_backoff(opts: ClientOptions) -> ClientOptions:
        opts["retry"] = Pyle38Retry(Pyle38ExponentialBackoff(), retries=retries)
        return opts

    return _with_retry_exponential_backoff


def WithRetryOnError(
    *errs: type[Pyle38Error],
) -> Callable[..., ClientOptions]:
    def _with_retry_on_error(opts: ClientOptions) -> ClientOptions:
        opts["retry_on_error"] = []
        if len(errs) > 0:
            opts["retry_on_error"] = list(errs)
        return opts

    return _with_retry_on_error
