# apps/plugins/divide.py
command_name = 'divide'

def run(args):
    if len(args) < 2:
        raise ValueError("Divide operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        raise ValueError("Invalid operands. Please provide numbers.")
    result = operands[0]
    for operand in operands[1:]:
        # LBYL: Check if dividing by zero
        if operand == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= operand
    return result
