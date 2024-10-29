# app/calculator/calculator.py
import logging
import pandas as pd
from app.commands.command_parser import parse_command
from app.plugins.plugin_manager import PluginManager

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.plugin_manager = PluginManager()
        self.history_file = 'history.csv'
        self.history_data = self.load_history()
        self.logger.info("Calculator initialized.")

    def load_history(self):
        try:
            history = pd.read_csv(self.history_file)
            self.logger.info("History loaded from CSV file.")
            return history
        except FileNotFoundError:
            self.logger.info("No existing history file found. Starting with empty history.")
            return pd.DataFrame(columns=['Input', 'Result'])
        except Exception as e:
            self.logger.error(f"Error loading history: {e}", exc_info=True)
            return pd.DataFrame(columns=['Input', 'Result'])

    def save_history(self):
        try:
            self.history_data.to_csv(self.history_file, index=False)
            self.logger.info("History saved to CSV file.")
        except Exception as e:
            self.logger.error(f"Error saving history: {e}", exc_info=True)

    def run(self):
        self.logger.info("Calculator REPL started.")
        try:
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

                    context = {'history_data': self.history_data}

                    result = self.plugin_manager.execute(command_name, args, context=context)
                    if result is not None:
                        print(f"The answer is: {result}")
                        self.logger.info(f"Result: {result}")
                        # Record the successful operation in history
                        self.record_history(user_input, result)

                except Exception as e:
                    print(f"Error: {e}")
                    self.logger.error(f"An error occurred: {e}", exc_info=True)
        finally:
            self.save_history()
            self.logger.info("Calculator REPL terminated.")

    def record_history(self, input_str, result):
        new_entry = {'Input': input_str, 'Result': result}
        self.history_data = self.history_data.append(new_entry, ignore_index=True)
        self.logger.info(f"Recorded history: {new_entry}")
