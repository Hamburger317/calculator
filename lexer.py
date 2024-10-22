import re
from typing import Optional

from operators import OPERATORS, PREFIX_OPERATORS, SUFFIX_OPERATORS
from tokens import Category, Token


class LexerError(Exception):
    pass


def _is_float_like(s: str) -> bool:
    try:
        float(s)

    except ValueError:
        return False

    return True


def tokenize(expression: str) -> list[str]:
    expression = re.sub(r"\s+", "", expression)
    raw_tokens = re.split(r"(\+|\-|\*|/|%|\^|\(|\))", expression)

    return [raw_token for raw_token in raw_tokens if raw_token]


def analyze(raw_tokens: list[str]) -> list[Token]:
    tokens: list[Token] = []

    for raw_token in raw_tokens:
        token: Optional[Token] = None

        if _is_float_like(raw_token):
            token = Token(Category.NUMBER, raw_token, float(raw_token))

        elif raw_token == "(":
            token = Token(Category.PARENTHESIS_OPEN, raw_token)

        elif raw_token == ")":
            token = Token(Category.PARENTHESIS_CLOSE, raw_token)

        elif raw_token in OPERATORS | PREFIX_OPERATORS | SUFFIX_OPERATORS:
            token = Token(Category.OPERATOR, raw_token)

        if token is None:
            raise LexerError("syntax error.")

        tokens.append(token)

    return tokens
