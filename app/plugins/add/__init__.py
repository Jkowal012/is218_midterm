# apps/plugins/__init__.py
command_name = 'add'

def run(args):
    if len(args) < 2:
        raise ValueError("Add operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        raise ValueError("Invalid operands. Please provide numbers.")
    result = sum(operands)
    return result
