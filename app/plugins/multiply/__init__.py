# apps/plugins/multiply/__init__.py
command_name = 'multiply'

def run(args):
    if len(args) < 2:
        raise ValueError("Multiply operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        raise ValueError("Invalid operands. Please provide numbers.")
    result = 1
    for operand in operands:
        result *= operand
    return result
