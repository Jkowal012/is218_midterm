# tests/test_plugins.py

import pytest
from app.plugins.add import run as add_run
from app.plugins.subtract import run as subtract_run
from app.plugins.multiply import run as multiply_run
from app.plugins.divide import run as divide_run
from faker import Faker

faker = Faker()

@pytest.mark.parametrize('num_operands', [2, 3, 5, 10])
def test_add(num_operands):
    operands = [str(faker.pyfloat(left_digits=3, right_digits=2, positive=False)) for _ in range(num_operands)]
    expected = sum(map(float, operands))
    result = add_run(operands)
    assert pytest.approx(result, 0.0001) == expected

def test_add_insufficient_operands():
    with pytest.raises(ValueError, match="Add operation requires at least two operands."):
        add_run(['5'])

def test_add_invalid_operands():
    with pytest.raises(ValueError, match="Invalid operands. Please provide numbers."):
        add_run(['a', 'b'])

@pytest.mark.parametrize('num_operands', [2, 3, 5])
def test_subtract(num_operands):
    operands = [str(faker.pyfloat(left_digits=3, right_digits=2, positive=False)) for _ in range(num_operands)]
    expected = float(operands[0])
    for operand in operands[1:]:
        expected -= float(operand)
    result = subtract_run(operands)
    assert pytest.approx(result, 0.0001) == expected

def test_subtract_insufficient_operands():
    with pytest.raises(ValueError, match="Subtract operation requires at least two operands."):
        subtract_run(['5'])

def test_subtract_invalid_operands():
    with pytest.raises(ValueError, match="Invalid operands. Please provide numbers."):
        subtract_run(['a', 'b'])

@pytest.mark.parametrize('num_operands', [2, 3, 5])
def test_multiply(num_operands):
    operands = [str(faker.pyfloat(left_digits=2, right_digits=2, positive=False)) for _ in range(num_operands)]
    expected = 1.0
    for operand in operands:
        expected *= float(operand)
    result = multiply_run(operands)
    assert pytest.approx(result, 0.0001) == expected

def test_multiply_insufficient_operands():
    with pytest.raises(ValueError, match="Multiply operation requires at least two operands."):
        multiply_run(['5'])

def test_multiply_invalid_operands():
    with pytest.raises(ValueError, match="Invalid operands. Please provide numbers."):
        multiply_run(['a', 'b'])

def test_divide():
    numerator = str(faker.pyfloat(left_digits=3, right_digits=2, positive=False))
    # Ensure denominator is not zero
    denominator = str(faker.pyfloat(left_digits=3, right_digits=2, positive=False, min_value=0.1))
    operands = [numerator, denominator]
    expected = float(numerator) / float(denominator)
    result = divide_run(operands)
    assert pytest.approx(result, 0.0001) == expected

def test_divide_insufficient_operands():
    with pytest.raises(ValueError, match="Divide operation requires at least two operands."):
        divide_run(['5'])

def test_divide_invalid_operands():
    with pytest.raises(ValueError, match="Invalid operands. Please provide numbers."):
        divide_run(['a', 'b'])

def test_divide_by_zero():
    numerator = str(faker.pyfloat(left_digits=3, right_digits=2, positive=False))
    denominator = '0'
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        divide_run([numerator, denominator])
