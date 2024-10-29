# app/plugins/plugin_manager.py
import os
import importlib
import logging

class PluginManager:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        self.logger.info("Loading plugins...")
        plugins_dir = os.path.dirname(__file__)
        for foldername in os.listdir(plugins_dir):
            folder_path = os.path.join(plugins_dir, foldername)
            if os.path.isdir(folder_path) and foldername not in ['__pycache__', 'plugin_manager']:
                module_name = f"app.plugins.{foldername}"
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, 'command_name') and hasattr(module, 'run'):
                        self.plugins[module.command_name] = module.run
                        self.logger.info(f"Loaded plugin: {module.command_name}")
                    else:
                        self.logger.warning(f"Module {module_name} missing required attributes.")
                except ModuleNotFoundError as e:
                    self.logger.error(f"Could not load plugin {module_name}: {e}")

    def execute(self, command_name, args):
        self.logger.info(f"Executing command: {command_name} with args: {args}")
        if command_name in self.plugins:
            try:
                result = self.plugins[command_name](args)
                self.logger.info(f"Command {command_name} executed successfully.")
                return result
            except Exception as e:
                self.logger.error(f"Error executing command {command_name}: {e}", exc_info=True)
                raise
        else:
            self.logger.warning(f"Unknown command: {command_name}")
            raise ValueError(f"Unknown command: {command_name}")
