class Tile38Error(Exception):
    pass


class Tile38IdNotFoundError(Exception):
    pass


class Tile38KeyNotFoundError(Exception):
    pass


class Tile38NotCaughtUpError(Exception):
    pass


class Tile38PathNotFoundError(Exception):
    pass


class Pyle38CountMismatchError(Exception):
    def __init__(self, count: int, actual_count: int):
        super().__init__(
            f"Count {count} does not match the length of values {actual_count}"
        )
        self.count = count
        self.actual_count = actual_count
