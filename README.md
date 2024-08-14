# A Simple Calculator

Written to teach myself how to use the Shunting Yard Algorithm,
this calculator can handle simple arithmetic expressions such as `1 + 5`,
`(27.5 * -4)^2`, and `(34 * (1 / 2)) - 52 * 2`.

## Usage

Simply run `calculator.py`.

```none
Input expression.
>>>
```

A better CLI will be worked on soon.

Alternatively, use the `evaluate` function from the `evaluate` module.

```py
import evaluate

print(evaluate.evaluate("10 - 2"))  # prints "8.0"

```

## Operator Table

| Operation | Description                                                                      | Example | Result | Precedence | Associativity |
|-----------|----------------------------------------------------------------------------------|---------|--------|------------|---------------|
| (         | Left parenthesis. Used for grouping expressions.                                 | N/A     | N/A    | N/A        | N/A           |
| )         | Right parenthesis. Used for grouping expressions.                                | N/A     | N/A    | N/A        | N/A           |
| + (unary) | Evaluates its operand to itself.                                                 | +10     | 10     | 3          | Right to Left |
| - (unary) | Negation. Negates its operand. Used for negative numbers.                        | -10     | -10    | 3          | Right to Left |
| ^         | Exponent. Raises its left operand to the power of its right operand.             | 2^4     | 16     | 3          | Right to Left |
| %         | Modulo. Converts its 2 operands to integers, and returns the remainder of the 2. | 8 % 3   | 2      | 2          | Left to Right |
| /         | Division. Divides its 2 operands.                                                | 5 / 2   | 2.5    | 2          | Left to Right |
| *         | Multiplication. Multiplies its 2 operands.                                       | 6 * 2   | 12     | 2          | Left to Right |
| -         | Subtraction. Subtracts its 2 operands.                                           | 12 - 10 | 2      | 1          | Left to Right |
| +         | Addition. Adds its 2 operands.                                                   | 2 + 2   | 4      | 1          | Left to Right |

## Credits

### Helpful Resources

[Wikipedia article on the Shunting Yard Algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)

[Wikipedia article on Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

[Javidx9's video covering the Shunting Yard Algorithm](https://www.youtube.com/watch?v=unh6aK8WMwM)

### Reference Implementations

[Javidx9's Implementation for his DIY Programming Language series](https://github.com/OneLoneCoder/Javidx9/blob/master/SimplyCode/OneLoneCoder_ShuntingYardAlgo.cpp)

[Boris' Implementation of the Shunting Yard Algorithm](https://github.com/BorisAnastasov/Shunting-Yard-Algorithm--CSharp/tree/main)
