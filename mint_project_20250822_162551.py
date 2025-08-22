# calculator.py

class Calculator:
    def add(self, x, y):
        """Add two numbers"""
        return x + y

    def subtract(self, x, y):
        """Subtract y from x"""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y

    def divide(self, x, y):
        """Divide x by y"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

# test_calculator.py

import unittest
from calculator import Calculator

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
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

# main.py

def main():
    calc = Calculator()
    
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = calc.add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
                
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
                
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
                
            elif choice == '4':
                try:
                    result = calc.divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    # If running the file directly, run the main program
    main()

# To run tests, use:
# python -m unittest test_calculator.py