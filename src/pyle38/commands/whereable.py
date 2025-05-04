import abc
from typing import TypeVar

from ..client import CommandArgs, SubCommand

TWhereable = TypeVar("TWhereable", bound="Whereable")

Where = list[list[str | int]]
Wherein = list[list[str | int | float]]


class Whereable(abc.ABC):
    _where: Where
    _wherein: Wherein

    def compile_where(self) -> CommandArgs:
        """__compile_where.

        Args:

        Returns:
            CommandArgs
        """
        w = []

        if len(self._where) > 0:
            for i in self._where:
                w.extend(i)
            return w

        return w

    def compile_wherein(self) -> CommandArgs:
        """__compile_wherein.

        Args:

        Returns:
            CommandArgs
        """
        w = []

        if len(self._wherein) > 0:
            for i in self._wherein:
                w.extend(i)
            return w
        return []

    def wherein(
        self: TWhereable, field: str, values: list[int | str | float]
    ) -> TWhereable:
        """Filter the search by fields values containing input values

        Args:
            field (str): field name
            values (list): values to lookup in field values

        Returns:
            TWhereable
        """
        self._wherein.append([SubCommand.WHEREIN, field, len(values), *values])

        return self

    def where(self: TWhereable, field: str, minimum: int, maximum: int) -> TWhereable:
        """Filter the search by field

        Args:
            field (str): field name
            minimum (int): minimum value of field
            maximum (int): maximum value of field

        Returns:
            TWhereable
        """

        self._where.append([SubCommand.WHERE, field, minimum, maximum])

        return self

    def where_expr(self: TWhereable, expr: str) -> TWhereable:
        """Filter the search with an expression

        Args:
            expr (str): expression

        Returns:
            TWhereable

        Example:

        ```python
        await tile38.set('fleet', 'truck').fields({ 'driver': 'John'})
        await tile38.scan('fleet').where_expr("driver === 'John'")
        ```

        """

        self._where.append([SubCommand.WHERE, expr])

        return self
