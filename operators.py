from dataclasses import dataclass
from enum import Enum


class Associativity(Enum):
    LEFT = 0
    RIGHT = 1


@dataclass
class Operator:
    associativity: Associativity
    precedence: int


OPERATORS: dict[str, Operator] = {
    "+": Operator(Associativity.LEFT, 1),
    "-": Operator(Associativity.LEFT, 1),
    "*": Operator(Associativity.LEFT, 2),
    "/": Operator(Associativity.LEFT, 2),
    "%": Operator(Associativity.LEFT, 2),
    "^": Operator(Associativity.RIGHT, 3)
}

PREFIX_OPERATORS: dict[str, Operator] = {
    "+": Operator(Associativity.RIGHT, 3),
    "-": Operator(Associativity.RIGHT, 3)
}

SUFFIX_OPERATORS: dict[str, Operator] = {
    "%": Operator(Associativity.LEFT, 3)
}
