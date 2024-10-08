from typing import Optional

from operators import PREFIX_OPERATORS
from tokens import Category, Token


def _is_prefix(previous: Optional[Token], token: Token) -> bool:
    # For cases where an unary operator is at the beginning
    # like "-5 + ..."
    if previous is None:
        return True

    has_prefix_operation = token.symbol in PREFIX_OPERATORS
    treated_as_prefix: bool = (
        previous.category != Category.NUMBER
        and previous.category != Category.PARENTHESIS_CLOSE
    ) or previous.category == Category.PREFIX_OPERATOR

    return has_prefix_operation and treated_as_prefix


def parse_tokens(tokens: list[Token]) -> list[Token]:
    """Reconstructs a series of tokens (lexemes) using a simple AST.

    Args:
        tokens (list[Token]): A list of tokens.

    Returns:
        list[Token]: Parsed tokens.
    """

    parsed_tokens: list[Token] = []

    # Pad tokens, so that unary operators can be handled if they are at
    # the front or the back of an expression.
    # i.e "-3 + 2" or "5 * 15%".
    tokens: list[Optional[Token]] = [None, *tokens, None]

    for prev_token, token, next_token in zip(tokens, tokens[1:], tokens[2:]):
        # Type checkers consider the entire list to be of type
        # `Token | None` when in practice only `prev_token` and
        # `next_token` could possibly be None.
        assert token is not None

        if token.category != Category.OPERATOR:
            # No use reconstructing Token.
            parsed_tokens.append(token)
            continue

        if _is_prefix(prev_token, token):
            parsed_tokens.append(Token.from_prefix(token))

        else:
            parsed_tokens.append(Token.from_operator(token))

    return parsed_tokens
