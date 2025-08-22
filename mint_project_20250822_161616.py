# main.py
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# test_calculator.py
import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()

# integration_test.py
import pytest
from main import Calculator

def test_complex_calculation():
    calc = Calculator()
    # Test a more complex calculation
    result = calc.multiply(calc.add(5, 3), calc.subtract(10, 4))
    assert result == 48

def test_chain_operations():
    calc = Calculator()
    # Test chaining multiple operations
    step1 = calc.add(10, 5)  # 15
    step2 = calc.multiply(step1, 2)  # 30
    step3 = calc.subtract(step2, 5)  # 25
    final = calc.divide(step3, 5)  # 5
    assert final == 5

# Run with: python -m pytest integration_test.py

# requirements.txt
"""
pytest==7.3.1
unittest2==1.1.0
"""

# README.md
"""
# Calculator Test Application

This is a simple calculator application that demonstrates unit testing and integration testing in Python.

## Installation

1. Clone the repository
2. Create a virtual environment: