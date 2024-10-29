# app/calculator/calculator.py
import logging
from app.commands.command_parser import parse_command
from app.plugins.plugin_manager import PluginManager

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.plugin_manager = PluginManager()
        self.logger.info("Calculator initialized.")

    def run(self):
        self.logger.info("Calculator REPL started.")
        while True:
            try:
                user_input = input(">>> ")
                self.logger.info(f"User input: {user_input}")
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    self.logger.info("User exited the application.")
                    break
                command_name, args = parse_command(user_input)
                self.logger.info(f"Command: {command_name}, Args: {args}")
                result = self.plugin_manager.execute(command_name, args)
                print(f"The answer is: {result}")
                self.logger.info(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
                self.logger.error(f"An error occurred: {e}", exc_info=True)
        self.logger.info("Calculator REPL terminated.")

