# tests/test_calculator.py

import pytest
from app.calculator.calculator import Calculator
from unittest.mock import patch

def test_calculator_run_quit():
    calculator = Calculator()
    with patch('builtins.input', side_effect=['quit']):
        with patch('builtins.print') as mock_print:
            calculator.run()
            mock_print.assert_called_with("Goodbye!")

def test_calculator_run_add():
    calculator = Calculator()
    with patch('builtins.input', side_effect=['add 1 2', 'quit']):
        with patch('builtins.print') as mock_print:
            calculator.run()
            mock_print.assert_any_call("The answer is: 3.0")

def test_calculator_run_invalid_command():
    calculator = Calculator()
    with patch('builtins.input', side_effect=['unknown 1 2', 'quit']):
        with patch('builtins.print') as mock_print:
            calculator.run()
            mock_print.assert_any_call("Error: Unknown command: unknown")
