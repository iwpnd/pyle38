from typing import List, TypeVar, Union

from ..client import CommandArgs, SubCommand

TWhereable = TypeVar("TWhereable", bound="Whereable")

Where = List[List[Union[str, int]]]
Wherein = List[List[Union[str, int, float]]]


class Whereable:
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
        return []

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
        self: TWhereable, field: str, values: List[Union[int, str, float]]
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

    def where(self: TWhereable, field: str, min: int, max: int) -> TWhereable:
        """Filter the search by field

        Args:
            field (str): field name
            min (int): minimum value of field
            max (int): maximum value of field

        Returns:
            TWhereable
        """

        self._where.append([SubCommand.WHERE, field, min, max])

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
