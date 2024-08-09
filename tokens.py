from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Self

from operators import Operator, OPERATORS, UNARY_OPERATORS


class Category(Enum):
    UNKNOWN = auto()
    NUMBER = auto()  # i.e "1", "35", "3.14"
    OPERATOR = auto()  # i.e "+", "*", "%"
    UNARY_OPERATOR = auto()  # i.e negation (-)
    PARENTHESIS_OPEN = auto()  # "("
    PARENTHESIS_CLOSE = auto()  # ")"


@dataclass
class Token:
    category: Category
    symbol: str
    value: Optional[float | Operator] = None

    @classmethod
    def from_operator(cls, token: Self) -> Self:
        """Helper constructor used internally by the parser.

        Args:
            token (Self): Another token of `Category.OPERATOR`.

        Returns:
            Self: A token.
        """
        symbol = token.symbol

        return cls(Category.OPERATOR, symbol, OPERATORS[symbol])

    @classmethod
    def from_unary(cls, token: Self) -> Self:
        symbol = token.symbol

        return cls(Category.UNARY_OPERATOR, symbol, UNARY_OPERATORS[symbol])
