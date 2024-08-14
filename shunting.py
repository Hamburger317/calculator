from lexer import Category, Token
from operators import Associativity, Operator


_OPERATORS = (Category.OPERATOR, Category.UNARY_OPERATOR)


def _higher_priority(operator: Operator, other: Operator) -> bool:
    return operator.precedence > other.precedence or (
        operator.precedence == other.precedence
        and other.associativity == Associativity.LEFT
    )


def _top_is_open_parenthesis(stack):
    return stack[-1].category == Category.PARENTHESIS_OPEN


def _handle_operator(token, output_stack, operator_stack):
    assert isinstance(token.value, Operator)

    operator = token.value

    while (
        operator_stack
        and not _top_is_open_parenthesis(operator_stack)
        and _higher_priority(operator_stack[-1].value, operator)
    ):
        output_stack.append(operator_stack.pop())

    operator_stack.append(token)


def postfix(expression: list[Token]) -> list[Token]:
    output: list[Token] = []
    operators: list[Token] = []

    for token in expression:
        if token.category == Category.NUMBER:
            output.append(token)

        elif token.category == Category.PARENTHESIS_CLOSE:
            while operators and not _top_is_open_parenthesis(operators):
                output.append(operators.pop())

            operators.pop()

        elif token.category == Category.PARENTHESIS_OPEN:
            operators.append(token)

        elif token.category in _OPERATORS and not operators:
            operators.append(token)

        elif token.category in _OPERATORS:
            _handle_operator(token, output, operators)

    while operators:
        output.append(operators.pop())

    return output


def _evaluate_operator(operand, other, operator):
    if operator == "+":
        return operand + other
    
    elif operator == "-":
        return operand - other
    
    elif operator == "*":
        return operand * other
    
    elif operator == "/":
        return operand / other
    
    elif operator == "%":
        return int(operand) % int(other)
    
    elif operator == "^":
        return operand ** other


def _evaluate_unary(operand, operator):
    if operator == "+":
        return +operand
    
    elif operator == "-":
        return -operand


def solve_postfix(postfix_tokens: list[Token]) -> float:
    solve_stack: list[float] = []

    for token in postfix_tokens:
        if token.category == Category.NUMBER:
            assert isinstance(token.value, float)
            solve_stack.append(token.value)

        elif token.category == Category.OPERATOR:
            assert len(solve_stack) >= 2

            operand2 = solve_stack.pop()
            operand = solve_stack.pop()

            result = _evaluate_operator(operand, operand2, token.symbol)
            solve_stack.append(result)

        elif token.category == Category.UNARY_OPERATOR:
            assert len(solve_stack) >= 1

            operand = solve_stack.pop()

            result = _evaluate_unary(operand, token.symbol)
            solve_stack.append(result)

    return solve_stack[0]
