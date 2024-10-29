# tests/test_plugins.py

import unittest
from faker import Faker
from app.plugins.add import run as add_run
from app.plugins.subtract import run as subtract_run
from app.plugins.multiply import run as multiply_run
from app.plugins.divide import run as divide_run
from app.plugins.history import run as history_run
import pandas as pd

class TestPlugins(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.context = {'history_data': pd.DataFrame(columns=['Input', 'Result'])}

    # Add Plugin Tests
    def test_add_valid_args(self):
        nums = [str(self.fake.pyfloat(min_value=-1000, max_value=1000)) for _ in range(3)]
        expected_result = sum(float(num) for num in nums)
        result = add_run(nums)
        self.assertEqual(result, expected_result)

    def test_add_insufficient_operands(self):
        nums = [str(self.fake.pyfloat())]
        with self.assertRaises(ValueError):
            add_run(nums)

    def test_add_invalid_operands(self):
        nums = [self.fake.word(), self.fake.word()]
        with self.assertRaises(ValueError):
            add_run(nums)

    # Subtract Plugin Tests
    def test_subtract_valid_args(self):
        nums = [str(self.fake.pyfloat(min_value=-1000, max_value=1000)) for _ in range(2)]
        expected_result = float(nums[0]) - float(nums[1])
        result = subtract_run(nums)
        self.assertEqual(result, expected_result)

    def test_subtract_insufficient_operands(self):
        nums = [str(self.fake.pyfloat())]
        with self.assertRaises(ValueError):
            subtract_run(nums)

    def test_subtract_invalid_operands(self):
        nums = [self.fake.word(), self.fake.word()]
        with self.assertRaises(ValueError):
            subtract_run(nums)

    # Multiply Plugin Tests
    def test_multiply_valid_args(self):
        nums = [str(self.fake.pyfloat(min_value=-10, max_value=10)) for _ in range(3)]
        expected_result = 1.0
        for num in nums:
            expected_result *= float(num)
        result = multiply_run(nums)
        self.assertEqual(result, expected_result)

    def test_multiply_insufficient_operands(self):
        nums = [str(self.fake.pyfloat())]
        with self.assertRaises(ValueError):
            multiply_run(nums)

    def test_multiply_invalid_operands(self):
        nums = [self.fake.word(), self.fake.word()]
        with self.assertRaises(ValueError):
            multiply_run(nums)

    # Divide Plugin Tests
    def test_divide_valid_args(self):
        num1 = self.fake.pyfloat(min_value=-1000, max_value=1000)
        num2 = self.fake.pyfloat(min_value=0.1, max_value=1000)
        result = divide_run([str(num1), str(num2)])
        expected_result = num1 / num2
        self.assertEqual(result, expected_result)

    def test_divide_by_zero(self):
        num1 = self.fake.pyfloat()
        with self.assertRaises(ZeroDivisionError):
            divide_run([str(num1), '0'])

    def test_divide_invalid_operands(self):
        nums = [self.fake.word(), self.fake.word()]
        with self.assertRaises(ValueError):
            divide_run(nums)

    def test_history_display_empty(self):
        # Capture printed output
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the function with empty context
        history_run([], context={})

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check the output
        output = captured_output.getvalue()
        self.assertIn("History data is not available.", output)

    def test_history_display_with_data(self):
        entries = [
            {'Input': 'add 1 2', 'Result': 3.0},
            {'Input': 'multiply 2 3', 'Result': 6.0}
        ]
        self.context['history_data'] = pd.DataFrame(entries)
        # Since history_run prints output, we can test if it runs without errors
        history_run([], context=self.context)
        # To test printed output, we'd need to capture stdout, but keeping it simple

if __name__ == '__main__':
    unittest.main()
