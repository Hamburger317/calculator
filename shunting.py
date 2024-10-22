import math
from typing import TypeAlias

from lexer import Category, Token
from operators import Associativity, Operator


_OPERATORS = (Category.OPERATOR,
              Category.PREFIX_OPERATOR,
              Category.SUFFIX_OPERATOR)

Stack: TypeAlias = list[Token]


def _higher_priority(operator: Operator, other: Operator) -> bool:
    return operator.precedence > other.precedence or (
        operator.precedence == other.precedence
        and other.associativity == Associativity.LEFT
    )


def _top_is_open_parenthesis(stack: Stack) -> bool:
    return stack[-1].category == Category.PARENTHESIS_OPEN


def _handle_operator(token: Token, output: Stack, operator_stack: Stack):
    assert isinstance(token.value, Operator)

    operator = token.value

    if token.category == Category.SUFFIX_OPERATOR:
        output.append(token)
        return

    while (
        operator_stack
        and not _top_is_open_parenthesis(operator_stack)
        and _higher_priority(operator_stack[-1].value, operator)
    ):
        output.append(operator_stack.pop())

    operator_stack.append(token)


def postfix(expression: Stack) -> Stack:
    output: Stack = []
    operators: Stack = []

    for token in expression:
        if token.category == Category.NUMBER:
            output.append(token)

        elif token.category == Category.PARENTHESIS_CLOSE:
            while operators and not _top_is_open_parenthesis(operators):
                output.append(operators.pop())

            operators.pop()

        elif token.category == Category.PARENTHESIS_OPEN:
            operators.append(token)

        elif token.category in _OPERATORS:
            _handle_operator(token, output, operators)

    while operators:
        output.append(operators.pop())

    return output


def _evaluate(operand: float, other: float, operator: Operator) -> float:
    if operator == "+":
        return operand + other

    elif operator == "-":
        return operand - other

    elif operator == "*":
        return operand * other

    elif operator == "/":
        return operand / other

    elif operator == "%":
        return operand % other

    elif operator == "^":
        return operand**other


def _evaluate_prefix(operand: float, operator: Stack) -> float:
    if operator == "+":
        return +operand

    elif operator == "-":
        return -operand
    

def _evaluate_suffix(operand: float, operator: Operator) -> float:
    if operator == "%":
        return operand / 100

    elif operator == "!":
        # math.factorial only takes in integers, since we're working
        # with floats, we instead find the Gamma function of the
        # operand after we shift it by one.
        return math.gamma(operand + 1)


def solve_postfix(postfix_tokens: Stack) -> float:
    solve_stack: list[float] = []

    for token in postfix_tokens:
        if token.category == Category.NUMBER:
            assert isinstance(token.value, float)
            solve_stack.append(token.value)

        elif token.category == Category.OPERATOR:
            assert len(solve_stack) >= 2

            operand2 = solve_stack.pop()
            operand = solve_stack.pop()

            result = _evaluate(operand, operand2, token.symbol)
            solve_stack.append(result)

        elif token.category == Category.PREFIX_OPERATOR:
            assert len(solve_stack) >= 1

            operand = solve_stack.pop()

            result = _evaluate_prefix(operand, token.symbol)
            solve_stack.append(result)

        elif token.category == Category.SUFFIX_OPERATOR:
            assert len(solve_stack) >= 1

            operand = solve_stack.pop()

            result = _evaluate_suffix(operand, token.symbol)
            solve_stack.append(result)

    return solve_stack[0]
