# commands/command_handler.py

import logging
from commands.command import Command
from plugins.plugin_loader import PluginLoader

class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.plugin_loader = PluginLoader()

    def load_plugins(self):
        plugins = self.plugin_loader.load_plugins()
        for name, command_class in plugins.items():
            self.register_command(name, command_class)

    def register_command(self, name, command_class):
        if issubclass(command_class, Command):
            self.commands[name] = command_class()
            logging.info(f"Command '{name}' registered.")
        else:
            logging.warning(f"Command '{name}' does not implement the Command interface.")

    def handle_command(self, user_input):
        parts = user_input.split()
        if not parts:
            return
        command_name, *args = parts
        command = self.commands.get(command_name)
        if command:
            try:
                command.execute(*args)
            except Exception as e:
                logging.error(f"Error executing command '{command_name}': {e}")
        else:
            logging.warning(f"Unknown command: '{command_name}'. Type 'help' for available commands.")
