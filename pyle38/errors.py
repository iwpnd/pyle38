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


class Pyle38BadObjectInputException(Exception):
    def __init__(self):
        super().__init__(
            "Input object is type dict but neither Polygon nor Feature type"
        )
