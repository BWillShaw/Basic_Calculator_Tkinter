if __name__ == "__main__" and __package__ is None:
    __package__ = "test"

import unittest
from app.calculator import addition, subtraction, multiplication, division, power_man, nth_root_man, power_builtin, nth_root_builtin, create_tokens, convert_to_postfix, evaluate_postfix

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(-1, 1), -2)
        self.assertEqual(subtraction(1, -1), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(5, 3), 15)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(-1, -1), 1)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(-6, 3), -2)
        self.assertEqual(division(6, -3), -2)
        self.assertEqual(division(0, 3), 0)
        self.assertEqual(division(3, 0), "Error: cannot divide by zero")

    def test_power_man(self):
        self.assertEqual(power_man(2, 3), 8)
        self.assertEqual(power_man(-2, 3), -8)

    def test_nth_root_man(self):
        self.assertAlmostEqual(nth_root_man(27, 3), 3, places=10)

    def test_power_builtin(self):
        self.assertEqual(power_builtin(2, 3), 8)

    def test_nth_root_builtin(self):
        self.assertAlmostEqual(nth_root_builtin(27, 3), 3, places=10)

    def test_create_tokens(self):
        self.assertEqual(create_tokens("5+3"), [5.0, '+', 3.0])
        self.assertEqual(create_tokens("3*(4+2)"), [3.0, '*', '(', 4.0, '+', 2.0, ')'])

    def test_convert_to_postfix(self):
        self.assertEqual(convert_to_postfix([3.0, '+', 4.0]), [3.0, 4.0, '+'])
        self.assertEqual(convert_to_postfix([3.0, '*', '(', 4.0, '+', 2.0, ')']), [3.0, 4.0, 2.0, '+', '*'])

    def test_evaluate_postfix(self):
        self.assertEqual(evaluate_postfix([3.0, 4.0, '+']), 7)
        self.assertEqual(evaluate_postfix([3.0, 4.0, 2.0, '+', '*']), 18)

if __name__ == '__main__':
    unittest.main()
