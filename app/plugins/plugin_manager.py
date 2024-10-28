# apps/plugins/plugin_manager.py
import os
import importlib

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        plugins_dir = os.path.dirname(__file__)
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename not in ['__init__.py', 'plugin_manager.py']:
                module_name = filename[:-3]
                module = importlib.import_module(f"apps.plugins.{module_name}")
                if hasattr(module, 'command_name') and hasattr(module, 'run'):
                    self.plugins[module.command_name] = module.run

    def execute(self, command_name, args):
        if command_name in self.plugins:
            return self.plugins[command_name](args)
        else:
            raise ValueError(f"Unknown command: {command_name}")
