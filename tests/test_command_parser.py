# tests/test_command_parser.py

import unittest
from app.commands.command_parser import parse_command
from faker import Faker

class TestCommandParser(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_parse_command_valid(self):
        command = self.fake.word()
        args = self.fake.words(nb=3)
        user_input = f"{command} {' '.join(args)}"
        command_name, parsed_args = parse_command(user_input)
        self.assertEqual(command_name, command)
        self.assertEqual(parsed_args, args)

    def test_parse_command_no_input(self):
        user_input = ""
        with self.assertRaises(ValueError):
            parse_command(user_input)

    def test_parse_command_only_spaces(self):
        user_input = "   "
        with self.assertRaises(ValueError):
            parse_command(user_input)

    def test_parse_command_extra_spaces(self):
        command = self.fake.word()
        args = self.fake.words(nb=2)
        user_input = f"  {command}   {'   '.join(args)}  "
        command_name, parsed_args = parse_command(user_input)
        self.assertEqual(command_name, command)
        self.assertEqual(parsed_args, args)

    def test_parse_command_special_characters(self):
        command = self.fake.word()
        special_args = [self.fake.pystr(min_chars=1, max_chars=5) for _ in range(3)]
        user_input = f"{command} {' '.join(special_args)}"
        command_name, parsed_args = parse_command(user_input)
        self.assertEqual(command_name, command)
        self.assertEqual(parsed_args, special_args)

if __name__ == '__main__':
    unittest.main()
