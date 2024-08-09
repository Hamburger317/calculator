import parser

import lexer
import shunting


def evaluate(expression: str) -> float:
    split_expression = lexer.tokenize(expression)
    tokens = lexer.analyze(split_expression)
    parsed_tokens = parser.parse_tokens(tokens)
    postfixed_expression = shunting.postfix(parsed_tokens)
    answer = shunting.solve_postfix(postfixed_expression)

    return answer
