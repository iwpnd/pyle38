from collections.abc import Callable
from typing import TypeAlias

from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from typing_extensions import NotRequired, TypedDict

from .errors import Pyle38Error

Pyle38Retry: TypeAlias = Retry
Pyle38ExponentialBackoff: TypeAlias = ExponentialBackoff


class ClientOptions(TypedDict):
    retry: NotRequired[Pyle38Retry]
    retry_on_error: NotRequired[list[type[Pyle38Error]]]


def WithRetryExponentialBackoff(retries: int) -> Callable[..., ClientOptions]:
    """Return a callable that configures exponential backoff for retries.

    This function creates and returns a callable that, when invoked, will configure
    retry behavior with exponential backoff for the given number of retries.

    Args:
        retries (int): The number of retry attempts to make.

    Raises:
        ValueError: If the retries argument is not a positive integer.

    Returns:
        Callable[..., ClientOptions]: A function that accepts `ClientOptions` and
        configures exponential backoff retry with the specified number of retries.
    """
    try:
        t = int(retries)
    except ValueError as e:
        raise ValueError("Retries must be a positive integer") from e  # noqa: TRY003

    if t < 0:
        raise ValueError("Retries must be a positive integer")  # noqa: TRY003

    def _with_retry_exponential_backoff(opts: ClientOptions) -> ClientOptions:
        """Helper function to update options with retry strategy.

        This function modifies the `ClientOptions` by setting the `retry` field
        to the configured exponential backoff retry strategy.

        Args:
            opts (ClientOptions): The current client options to update.

        Returns:
            ClientOptions: The updated client options with retry configuration.
        """
        opts["retry"] = Pyle38Retry(Pyle38ExponentialBackoff(), retries=retries)
        return opts

    return _with_retry_exponential_backoff


def WithRetryOnError(
    *errs: type[Pyle38Error],
) -> Callable[..., ClientOptions]:
    """Return a callable that configures retry behavior based on specific errors.

    This function creates and returns a callable that, when invoked, will configure
    the retry behavior to only retry on the specified error types.

    Args:
        *errs (type[Pyle38Error]): One or more error types to retry on.

    Returns:
        Callable[..., ClientOptions]: A function that accepts `ClientOptions` and
        configures the retry behavior based on the specified error types.
    """

    def _with_retry_on_error(opts: ClientOptions) -> ClientOptions:
        """Helper function to update options with error-based retry configuration.

        This function modifies the `ClientOptions` by setting the `retry_on_error`
        field to the provided list of error types that should trigger retries.

        Args:
            opts (ClientOptions): The current client options to update.

        Returns:
            ClientOptions: The updated client options with error-based retry configuration.
        """
        opts["retry_on_error"] = []
        if len(errs) > 0:
            opts["retry_on_error"] = list(errs)
        return opts

    return _with_retry_on_error
