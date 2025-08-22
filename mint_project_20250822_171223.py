#!/usr/bin/env python3

import sys
import os
import datetime
import json

class TestApp:
    def __init__(self):
        self.data = {}
        self.filename = "test_data.json"

    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            
            try:
                if choice == '1':
                    self.add_data()
                elif choice == '2':
                    self.view_data()
                elif choice == '3':
                    self.save_data()
                elif choice == '4':
                    self.load_data()
                elif choice == '5':
                    print("Goodbye!")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def display_menu(self):
        """Display the main menu"""
        print("\n=== Test Application ===")
        print("1. Add Data")
        print("2. View Data")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")

    def add_data(self):
        """Add new data to the application"""
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
            score = float(input("Enter score: "))
        except ValueError:
            print("Please enter valid numbers for age and score.")
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        entry = {
            "age": age,
            "score": score,
            "timestamp": timestamp
        }
        
        self.data[name] = entry
        print("Data added successfully!")

    def view_data(self):
        """Display all stored data"""
        if not self.data:
            print("No data available.")
            return

        print("\nCurrent Data:")
        print("-" * 50)
        for name, info in self.data.items():
            print(f"Name: {name}")
            print(f"Age: {info['age']}")
            print(f"Score: {info['score']}")
            print(f"Timestamp: {info['timestamp']}")
            print("-" * 50)

    def save_data(self):
        """Save data to a JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f, indent=4)
            print(f"Data saved to {self.filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        """Load data from a JSON file"""
        try:
            if not os.path.exists(self.filename):
                print("No saved data file exists.")
                return
            
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
            print(f"Data loaded from {self.filename}")
        except Exception as e:
            print(f"Error loading data: {e}")

def main():
    """Application entry point"""
    try:
        app = TestApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()