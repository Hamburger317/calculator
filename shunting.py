from lexer import Category, Token
from operators import Associativity, Operator


def postfix(expression: list[Token]) -> list[Token]:
    output: list[Token] = []
    operators: list[Token] = []

    for token in expression:
        if token.category == Category.NUMBER:
            output.append(token)

        elif token.category == Category.PARENTHESIS_CLOSE:
            while operators and operators[-1].category != Category.PARENTHESIS_OPEN:
                output.append(operators.pop())

            operators.pop()

        elif token.category == Category.PARENTHESIS_OPEN:
            operators.append(token)

        elif (
            token.category == Category.OPERATOR
            or token.category == Category.UNARY_OPERATOR
        ):
            assert isinstance(token.value, Operator)
            operator = token.value

            if operators:
                top = operators[-1]
                top_operator = top.value

                while (
                    top.category != Category.PARENTHESIS_OPEN
                    and top_operator.precedence > operator.precedence
                    or (
                        top.category != Category.PARENTHESIS_OPEN
                        and operator.precedence == top_operator.precedence
                        and top_operator.associativity == Associativity.LEFT
                    )
                ):
                    output.append(top)
                    top = operators.pop()

                    if not operators or top.category:
                        break

            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output


def solve_postfix(postfix_tokens: list[Token]) -> float:
    solve_stack: list[float] = []

    for token in postfix_tokens:
        if token.category == Category.NUMBER:
            assert isinstance(token.value, float)
            solve_stack.append(token.value)

        elif token.category == Category.OPERATOR:
            assert isinstance(token.value, Operator)
            # Operands flipped due to popping.
            if token.symbol == "+":
                assert len(solve_stack) >= 2
                operand1 = solve_stack.pop()
                operand2 = solve_stack.pop()

                solve_stack.append(operand2 + operand1)

            elif token.symbol == "-":
                assert len(solve_stack) >= 2
                operand1 = solve_stack.pop()
                operand2 = solve_stack.pop()

                solve_stack.append(operand2 - operand1)

            elif token.symbol == "*":
                assert len(solve_stack) >= 2
                operand1 = solve_stack.pop()
                operand2 = solve_stack.pop()

                solve_stack.append(operand2 * operand1)

            elif token.symbol == "/":
                assert len(solve_stack) >= 2
                operand1 = solve_stack.pop()
                operand2 = solve_stack.pop()

                solve_stack.append(operand2 / operand1)

            elif token.symbol == "%":
                assert len(solve_stack) >= 2
                operand1 = int(solve_stack.pop())
                operand2 = int(solve_stack.pop())

                solve_stack.append(operand2 % operand1)

            elif token.symbol == "^":
                assert len(solve_stack) >= 2
                operand1 = solve_stack.pop()
                operand2 = solve_stack.pop()

                solve_stack.append(operand2**operand1)

        elif token.category == Category.UNARY_OPERATOR:
            if token.symbol == "-":
                operand = solve_stack.pop()

                solve_stack.append(-operand)

            elif token.symbol == "+":
                operand = solve_stack.pop()

                solve_stack.append(+operand)

    return float(solve_stack[0])
