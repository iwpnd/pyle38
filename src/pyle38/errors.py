from redis.exceptions import ConnectionError, RedisError, TimeoutError  # noqa: A004

Pyle38Error = RedisError
Pyle38ConnectionError = ConnectionError
Pyle38TimeoutError = TimeoutError


class Tile38Error(Exception):
    pass


class Tile38IdNotFoundError(Exception):
    pass


class Tile38KeyNotFoundError(Exception):
    pass


class Tile38FieldNotFoundError(Exception):
    pass


class Tile38NotCaughtUpError(Exception):
    pass


class Tile38PathNotFoundError(Exception):
    pass


class Pyle38BadObjectInputError(Exception):
    def __init__(self) -> None:
        return super().__init__(
            "Input object is type dict but neither Polygon nor Feature type"
        )


class Pyle38NoFollowerSetError(Exception):
    def __init__(self) -> None:
        return super().__init__("No Tile38 follower URI set")


class Pyle38NoLeaderSetError(Exception):
    def __init__(self) -> None:
        return super().__init__("No Tile38 leader URI set")


class Pyle38NoHookToActivateError(Exception):
    def __init__(self) -> None:
        return super().__init__("No hook to activate")
