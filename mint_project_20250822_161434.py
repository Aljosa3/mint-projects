#!/usr/bin/env python3

"""
A simple Hello World application with multiple greeting options.
"""

import random
import sys
import time

class HelloApp:
    def __init__(self):
        self.greetings = [
            "Hello, World!",
            "Hi there!",
            "Greetings!",
            "Welcome!",
            "Hello, friend!"
        ]

    def get_random_greeting(self):
        """Returns a random greeting from the list."""
        return random.choice(self.greetings)

    def greet(self, name=None):
        """
        Prints a greeting, optionally personalized with a name.
        """
        greeting = self.get_random_greeting()
        if name:
            # Remove exclamation mark if present and add personalized greeting
            greeting = greeting.rstrip('!')
            greeting += f", {name}!"
        print(greeting)

    def interactive_greeting(self):
        """
        Provides an interactive greeting experience.
        """
        print("Welcome to the Hello Application!")
        print("--------------------------------")
        
        while True:
            name = input("\nPlease enter your name (or 'quit' to exit): ").strip()
            
            if name.lower() == 'quit':
                print("\nGoodbye!")
                break
            elif name:
                self.greet(name)
            else:
                self.greet()

def main():
    """Main function to run the hello application."""
    # Parse command line arguments
    if len(sys.argv) > 1:
        # If name provided as command line argument, just greet and exit
        app = HelloApp()
        app.greet(' '.join(sys.argv[1:]))
    else:
        # Otherwise, run interactive mode
        try:
            app = HelloApp()
            app.interactive_greeting()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()