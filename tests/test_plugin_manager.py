# tests/test_plugin_manager.py

import pytest
from app.plugins.plugin_manager import PluginManager

def test_plugin_manager_load_plugins():
    plugin_manager = PluginManager()
    assert "add" in plugin_manager.plugins
    assert "subtract" in plugin_manager.plugins
    assert "multiply" in plugin_manager.plugins
    assert "divide" in plugin_manager.plugins

def test_plugin_manager_execute_valid_command():
    plugin_manager = PluginManager()
    result = plugin_manager.execute("add", ["1", "2"])
    assert result == 3.0

def test_plugin_manager_execute_invalid_command():
    plugin_manager = PluginManager()
    with pytest.raises(ValueError, match="Unknown command: invalid"):
        plugin_manager.execute("invalid", ["1", "2"])
