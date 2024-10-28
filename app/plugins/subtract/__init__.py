# apps/plugins/subtract/__init__.py
command_name = 'subtract'

def run(args):
    if len(args) < 2:
        raise ValueError("Subtract operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        raise ValueError("Invalid operands. Please provide numbers.")
    result = operands[0]
    for operand in operands[1:]:
        result -= operand
    return result
