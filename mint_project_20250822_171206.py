# test_app.py

import unittest
import math

# Simple class to test
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)

# Test class
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_add(self):
        self.assertEqual(self.calc.add(4, 7), 11)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -2), 4)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
            
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertEqual(self.calc.square_root(2), math.sqrt(2))
        self.assertEqual(self.calc.square_root(0), 0)
        
        # Test negative number
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

# Integration test class
class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_complex_calculation(self):
        # (10 + 5) * 2 = 30
        result = self.calc.multiply(self.calc.add(10, 5), 2)
        self.assertEqual(result, 30)
        
        # √(16 - 7) = 3
        result = self.calc.square_root(self.calc.subtract(16, 7))
        self.assertEqual(result, 3)

def main():
    # Run the tests
    unittest.main()

if __name__ == '__main__':
    main()