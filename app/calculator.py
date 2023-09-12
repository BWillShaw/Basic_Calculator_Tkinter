# The 'calculator.py' module contains
# the primary arithmetic logic used

import math


# Basic arithmetic functions
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Error: cannot divide by zero"
    return x / y


# Exponential and root functions (manual)
def power_man(x, y):
    result = 1
    while y > 0:
        result = result * x
        y -= 1
    return result


def nth_root_man(a, n, tol=1e-10, max_iter=100):
    x = a
    for _ in range(max_iter):
        new_x = x - (x**n - a) / (n * x ** (n - 1))
        if abs(x - new_x) < tol:
            break
        x = new_x
    return x


# Exponential and root functions (built-in)
def power_builtin(x, y):
    return math.pow(x, y)


def nth_root_builtin(x, y):
    return math.pow(x, 1 / y)


# Logic to parse through and tokenise user input
def create_tokens(expression):
    temp_num = ""
    user_tokens = []
    operators = ["+", "-", "*", "/", "(", ")"]

    for char in expression:
        if char.isdigit() or char == ".":
            temp_num = temp_num + char
        else:
            if temp_num:
                user_tokens.append(float(temp_num))
                temp_num = ""
            if char in operators:
                user_tokens.append(char)

    # Additional code to handle the last number
    # in the expression post-UT fail
    if temp_num:
        user_tokens.append(float(temp_num))

    return user_tokens


# Convert to postfix notation - BEDMAS
def convert_to_postfix(user_tokens):
    output = []
    operators = []
    precedence = {"^": 1, "+": 2, "-": 2, "*": 3, "/": 3}  # Order of operation

    for token in user_tokens:
        # If the token is a number the take directly
        # to output
        if isinstance(token, float):
            output.append(token)

        # If the token is an operator
        elif token in ["^", "+", "-", "*", "/"]:
            # while 'operators' is not blank and
            # precedence value of token is <=
            # precedence value of the last operator
            # in the 'operators' list
            while operators and precedence.get(token, 0) <= precedence.get(
                operators[-1], 0
            ):
                output.append(operators.pop())

            # place the operator at the end of the
            # 'operators' list
            operators.append(token)

        # If the token is not a number nor an operator
        # and if token = '(' then add token to operators
        elif token == "(":
            operators.append(token)

        # If the token is not a number nor an operator
        # and if token = ')'
        elif token == ")":
            # loop through operators and while the last
            # element (LIFO) of operators is not '('
            # remove the last element of operators and
            # place in output list
            while operators[-1] != "(":
                output.append(operators.pop())

            # remove '(' after removing operators
            # and preceeding
            operators.pop()

    # remove any remaining operators in operators
    # list and append to output list
    while operators:
        output.append(operators.pop())

    return output


def evaluate_postfix(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            b, a = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
    return stack[0]


# Example usage
# result = evaluate_postfix(postfix_tokens)
# print("Result:", result)
