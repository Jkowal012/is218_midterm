# tests/test_main.py

import pytest
from unittest.mock import patch
import logging

def test_main_run(mocker):
    mocker.patch('app.calculator.calculator.Calculator.run')
    mocker.patch('app.calculator.calculator.Calculator.__init__', return_value=None)
    from main import main
    with patch('builtins.print') as mock_print:
        main()
        mock_print.assert_any_call("Welcome to the calculator!")
        