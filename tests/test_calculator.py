# tests/test_calculator.py

import unittest
from unittest.mock import patch
from faker import Faker
from app.calculator.calculator import Calculator
import pandas as pd

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.calculator = Calculator()
        # Mock history load and save to avoid file operations
        self.calculator.load_history = lambda: pd.DataFrame(columns=['Input', 'Result'])
        self.calculator.save_history = lambda: None

    def test_run_addition(self):
        num1 = self.fake.pyfloat()
        num2 = self.fake.pyfloat()
        inputs = [f'add {num1} {num2}', 'quit']
        expected_output = f"The answer is: {num1 + num2}"

        with patch('builtins.input', side_effect=inputs):
            with patch('builtins.print') as mock_print:
                self.calculator.run()
                mock_print.assert_any_call(expected_output)
                mock_print.assert_any_call("Goodbye!")

    def test_run_unknown_command(self):
        command = self.fake.word()
        inputs = [f'{command} 1 2', 'quit']
        error_message = f"Error: Unknown command: {command}"

        with patch('builtins.input', side_effect=inputs):
            with patch('builtins.print') as mock_print:
                self.calculator.run()
                mock_print.assert_any_call(error_message)
                mock_print.assert_any_call("Goodbye!")

    def test_run_divide_by_zero(self):
        num = self.fake.pyfloat()
        inputs = [f'divide {num} 0', 'quit']
        error_message = "Error: Cannot divide by zero."

        with patch('builtins.input', side_effect=inputs):
            with patch('builtins.print') as mock_print:
                self.calculator.run()
                mock_print.assert_any_call(error_message)
                mock_print.assert_any_call("Goodbye!")

    def test_run_history(self):
        # Pre-populate history
        self.calculator.history_data = pd.DataFrame([
            {'Input': 'add 1 2', 'Result': 3.0}
        ])
        inputs = ['history', 'quit']
        expected_output = "Calculation History:"

        with patch('builtins.input', side_effect=inputs):
            with patch('builtins.print') as mock_print:
                self.calculator.run()
                mock_print.assert_any_call(expected_output)
                mock_print.assert_any_call("Goodbye!")

if __name__ == '__main__':
    unittest.main()
