# tests/test_command_parser.py

import pytest
from app.commands.command_parser import parse_command

def test_parse_command_valid():
    user_input = "add 1 2 3"
    command_name, args = parse_command(user_input)
    assert command_name == "add"
    assert args == ["1", "2", "3"]

def test_parse_command_no_input():
    user_input = ""
    with pytest.raises(ValueError, match="No input provided."):
        parse_command(user_input)

def test_parse_command_only_spaces():
    user_input = "   "
    with pytest.raises(ValueError, match="No input provided."):
        parse_command(user_input)

def test_parse_command_extra_spaces():
    user_input = "  multiply   2   3  "
    command_name, args = parse_command(user_input)
    assert command_name == "multiply"
    assert args == ["2", "3"]
