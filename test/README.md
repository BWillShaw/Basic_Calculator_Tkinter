# Unit Test Documentation for Calculator Application

## Overview

This document outlines the unit tests designed for the Calculator application. The tests were implemented using Python's `unittest` framework. These tests are part of the development phase to ensure that all calculator functionalities are working as expected. All tests outlined in this document have passed successfully.

## Methodology

### Test Environment

- Python version: 3.x
- Testing framework: unittest
- Package: Calculator Application (`app.calculator`)

### Agile Iteration

This testing phase corresponds to sprint #3, which is focused on creating a reliable calculator module with basic arithmetic and advanced capabilities.

### Running the Tests

To run the tests, execute the following command from the root (app) directory of the project:

`'' cmd
python -m unittest test_calculator.py
```

## Test Cases

### Test Case 1: Addition

- **Method Under Test**: `addition(a, b)`
- **Objective**: To test if the method correctly adds two numbers
- **Test IDs**: `test_addition`

#### Outcome:

All test cases passed.

---

### Test Case 2: Subtraction

- **Method Under Test**: `subtraction(a, b)`
- **Objective**: To test if the method correctly subtracts two numbers
- **Test IDs**: `test_subtraction`

#### Outcome:

All test cases passed.

---

### Test Case 3: Multiplication

- **Method Under Test**: `multiplication(a, b)`
- **Objective**: To test if the method correctly multiplies two numbers
- **Test IDs**: `test_multiplication`

#### Outcome:

All test cases passed.

---

### Test Case 4: Division

- **Method Under Test**: `division(a, b)`
- **Objective**: To test if the method correctly divides two numbers, including division by zero
- **Test IDs**: `test_division`

#### Outcome:

All test cases passed, including the division by zero error scenario.

---

### Test Case 5: Manual Power Calculation

- **Method Under Test**: `power_man(a, b)`
- **Objective**: To test if the method correctly calculates the power of a number using a manual implementation
- **Test IDs**: `test_power_man`

#### Outcome:

All test cases passed.

---

### Test Case 6: Manual Nth Root Calculation

- **Method Under Test**: `nth_root_man(a, b)`
- **Objective**: To test if the method correctly calculates the nth root of a number using a manual implementation
- **Test IDs**: `test_nth_root_man`

#### Outcome:

All test cases passed within the expected margin of error.

---

### Test Case 7: Built-in Power Calculation

- **Method Under Test**: `power_builtin(a, b)`
- **Objective**: To test if the method correctly calculates the power of a number using Python’s built-in function
- **Test IDs**: `test_power_builtin`

#### Outcome:

All test cases passed.

---

### Test Case 8: Built-in Nth Root Calculation

- **Method Under Test**: `nth_root_builtin(a, b)`
- **Objective**: To test if the method correctly calculates the nth root of a number using Python’s built-in function
- **Test IDs**: `test_nth_root_builtin`

#### Outcome:

All test cases passed within the expected margin of error.

---

### Test Case 9: Create Tokens from Expression

- **Method Under Test**: `create_tokens(expression)`
- **Objective**: To test if the method correctly tokenizes a mathematical expression
- **Test IDs**: `test_create_tokens`

#### Outcome:

All test cases passed.

---

### Test Case 10: Convert to Postfix Notation

- **Method Under Test**: `convert_to_postfix(tokens)`
- **Objective**: To test if the method correctly converts an expression in infix notation to postfix notation
- **Test IDs**: `test_convert_to_postfix`

#### Outcome:

All test cases passed.

---

### Test Case 11: Evaluate Postfix Expression

- **Method Under Test**: `evaluate_postfix(postfix_tokens)`
- **Objective**: To test if the method correctly evaluates an expression in postfix notation
- **Test IDs**: `test_evaluate_postfix`

#### Outcome:

All test cases passed.

---

## Summary

All unit tests for the Calculator application were successful. These tests validate the functional integrity of the calculator module, ensuring that it performs reliably under different scenarios.