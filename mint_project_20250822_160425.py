# hello_app.py

import datetime
import sys

class HelloApp:
    def __init__(self):
        self.name = ""

    def get_greeting(self):
        """Returns appropriate greeting based on time of day"""
        hour = datetime.datetime.now().hour
        
        if 5 <= hour < 12:
            return "Good morning"
        elif 12 <= hour < 17:
            return "Good afternoon"
        elif 17 <= hour < 22:
            return "Good evening"
        else:
            return "Good night"

    def welcome_message(self):
        """Displays welcome message"""
        print("Welcome to the Hello App!")
        print("------------------------")

    def get_user_name(self):
        """Gets user's name from input"""
        while True:
            name = input("Please enter your name (or 'exit' to quit): ").strip()
            if name.lower() == 'exit':
                sys.exit("Thank you for using Hello App. Goodbye!")
            elif name:
                self.name = name
                break
            else:
                print("Name cannot be empty. Please try again.")

    def display_greeting(self):
        """Displays personalized greeting"""
        greeting = self.get_greeting()
        print(f"\n{greeting}, {self.name}!")
        
    def run(self):
        """Main application loop"""
        self.welcome_message()
        
        while True:
            self.get_user_name()
            self.display_greeting()
            
            # Ask if user wants to continue
            while True:
                choice = input("\nWould you like to try again? (yes/no): ").lower()
                if choice in ['yes', 'no']:
                    break
                print("Please enter 'yes' or 'no'")
                
            if choice == 'no':
                print("\nThank you for using Hello App. Goodbye!")
                break

def main():
    """Main function to start the application"""
    try:
        app = HelloApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()