# hello_world.py

def simple_hello():
    """Simple Hello World function"""
    print("Hello, World!")

def personalized_hello(name):
    """Personalized Hello World function"""
    print(f"Hello, {name}!")

def main():
    # Simple hello world
    simple_hello()
    
    # Get user input for personalized greeting
    user_name = input("Please enter your name: ")
    personalized_hello(user_name)

if __name__ == "__main__":
    main()