import pytest

from pyle38.errors import Tile38Error
from pyle38.parse_response import parse_response


def test_parse_response() -> None:
    with pytest.raises(Tile38Error):
        response = parse_response(1)
        assert response

    with pytest.raises(Tile38Error):
        response = parse_response("{},")
        assert response
