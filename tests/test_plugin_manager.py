# tests/test_plugin_manager.py

import unittest
from app.plugins.plugin_manager import PluginManager
from faker import Faker

class TestPluginManager(unittest.TestCase):
    def setUp(self):
        self.plugin_manager = PluginManager()
        self.fake = Faker()

    def test_load_plugins(self):
        expected_plugins = {"add", "subtract", "multiply", "divide", "history"}
        self.assertEqual(set(self.plugin_manager.plugins.keys()), expected_plugins)

    def test_execute_valid_command(self):
        num1 = self.fake.pyfloat(positive=True)
        num2 = self.fake.pyfloat(positive=True)
        result = self.plugin_manager.execute("add", [str(num1), str(num2)])
        self.assertEqual(result, num1 + num2)

    def test_execute_unknown_command(self):
        unknown_command = self.fake.word()
        with self.assertRaises(ValueError):
            self.plugin_manager.execute(unknown_command, ["1", "2"])

if __name__ == '__main__':
    unittest.main()
