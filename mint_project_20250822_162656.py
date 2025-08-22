#!/usr/bin/env python3

class TestApplication:
    def __init__(self):
        self.results = []
        
    def run_tests(self):
        """Run a series of sample tests"""
        try:
            # Test 1: Basic arithmetic
            assert 2 + 2 == 4
            self.results.append(("Arithmetic test", "PASS"))
            
            # Test 2: String operations
            test_string = "Hello, World!"
            assert len(test_string) == 13
            assert test_string.upper() == "HELLO, WORLD!"
            self.results.append(("String operations test", "PASS"))
            
            # Test 3: List operations
            test_list = [1, 2, 3, 4, 5]
            test_list.append(6)
            assert len(test_list) == 6
            assert sum(test_list) == 21
            self.results.append(("List operations test", "PASS"))
            
            # Test 4: Dictionary operations
            test_dict = {"a": 1, "b": 2, "c": 3}
            assert test_dict["b"] == 2
            assert len(test_dict.keys()) == 3
            self.results.append(("Dictionary operations test", "PASS"))
            
        except AssertionError:
            self.results.append(("Test failed", "FAIL"))
            
    def display_results(self):
        """Display the results of all tests"""
        print("\n=== Test Results ===")
        for test_name, result in self.results:
            print(f"{test_name}: {result}")
        print("==================\n")
        
    def run_sample_calculation(self, x, y):
        """Perform a sample calculation"""
        try:
            result = x * y
            print(f"Calculation result: {x} * {y} = {result}")
            return result
        except Exception as e:
            print(f"Error in calculation: {str(e)}")
            return None

def main():
    # Create instance of TestApplication
    app = TestApplication()
    
    # Print welcome message
    print("Welcome to the Test Application!")
    print("--------------------------------")
    
    # Run the tests
    app.run_tests()
    
    # Display test results
    app.display_results()
    
    # Perform some sample calculations
    print("Performing sample calculations:")
    app.run_sample_calculation(5, 3)
    app.run_sample_calculation(10, 2)
    
    # Interactive section
    try:
        print("\nInteractive Calculator:")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = app.run_sample_calculation(x, y)
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    print("\nThank you for using the Test Application!")

if __name__ == "__main__":
    main()