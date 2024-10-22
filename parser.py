from typing import Optional

from operators import PREFIX_OPERATORS, SUFFIX_OPERATORS
from tokens import Category, Token

def _iterate_with_next(iterable: list[Token]):
    return zip(iterable, iterable[1:] + [None])

def _is_prefix(previous: Optional[Token], token: Token) -> bool:
    # For cases where an unary operator is at the beginning
    # like "-5 + ..."
    if previous is None:
        return True

    has_prefix_operation = token.symbol in PREFIX_OPERATORS
    treated_as_prefix: bool = (
        previous.category != Category.NUMBER
        and previous.category != Category.PARENTHESIS_CLOSE
        and previous.category != Category.SUFFIX_OPERATOR
    ) or previous.category == Category.PREFIX_OPERATOR

    return has_prefix_operation and treated_as_prefix

def _is_suffix(previous: Optional[Token], token: Token, next_: Optional[Token]):

    # It's an unimplemented prefix operator.
    # Here's where we'll raise an error.
    if previous is None:
        return False
    
    if next_ is None:
        return True

    has_suffix_operation = token.symbol in SUFFIX_OPERATORS
    treated_as_suffix = (
        previous.category == Category.NUMBER
        and next_.category != Category.NUMBER
        and next_.category != Category.PARENTHESIS_OPEN
    ) or next_.category == Category.OPERATOR or next_.category == Category.PARENTHESIS_CLOSE

    return has_suffix_operation and treated_as_suffix

def parse_tokens(tokens: list[Token]) -> list[Token]:
    """Reconstructs a series of tokens (lexemes) using a simple AST.

    Args:
        tokens (list[Token]): A list of tokens.

    Returns:
        list[Token]: Parsed tokens.
    """

    parsed_tokens: list[Token] = []

    previous_token = None
    for token, next_token in _iterate_with_next(tokens):
        cooked_token = None

        if token.category != Category.OPERATOR:
            cooked_token = token
            
        elif _is_prefix(previous_token, token):
            cooked_token = Token.from_prefix(token)

        elif _is_suffix(previous_token, token, next_token):
            cooked_token = Token.from_suffix(token)

        elif token.category == Category.OPERATOR:
            cooked_token = Token.from_operator(token)
        
        else:
            raise ValueError("unknown token.")
        
        parsed_tokens.append(cooked_token)
        previous_token = cooked_token

    return parsed_tokens
