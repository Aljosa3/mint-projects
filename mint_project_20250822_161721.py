# hello_world.py

def main():
    """Main function that prints Hello World"""
    print("Hello, World!")

def hello_with_name(name):
    """Prints a personalized hello message"""
    print(f"Hello, {name}!")

def hello_multiple_languages():
    """Prints hello in multiple languages"""
    greetings = {
        "English": "Hello, World!",
        "Spanish": "¡Hola, Mundo!",
        "French": "Bonjour, Monde!",
        "German": "Hallo, Welt!",
        "Italian": "Ciao, Mondo!"
    }
    
    for language, greeting in greetings.items():
        print(f"{language}: {greeting}")

if __name__ == "__main__":
    # Basic Hello World
    main()
    
    # Personalized greeting
    hello_with_name("Alice")
    
    # Print hello in multiple languages
    print("\nHello in different languages:")
    hello_multiple_languages()