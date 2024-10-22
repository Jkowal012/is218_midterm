# app.py

import sys
from commands.command_handler import CommandHandler

def main():
    handler = CommandHandler()
    handler.load_plugins()

    print("Welcome to the Calculator App!")
    print("Type 'help' to see available commands or 'exit' to quit.")

    while True:
        try:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            handler.handle_command(user_input)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
