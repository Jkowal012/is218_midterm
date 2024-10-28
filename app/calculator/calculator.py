# apps/calculator/calculator.py
from apps.commands.command_parser import parse_command
from apps.plugins.plugin_manager import PluginManager

class Calculator:
    def __init__(self):
        self.plugin_manager = PluginManager()

    def run(self):
        while True:
            try:
                user_input = input(">>> ")
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                command_name, args = parse_command(user_input)
                result = self.plugin_manager.execute(command_name, args)
                print(f"The answer is: {result}")
            except Exception as e:
                print(f"Error: {e}")
