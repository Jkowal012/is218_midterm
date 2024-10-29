# app/plugins/divide/__init__.py
import logging

command_name = 'divide'
logger = logging.getLogger(f"plugin.{command_name}")

def run(args, context=None):
    logger.info(f"Executing divide with args: {args}")
    if len(args) < 2:
        logger.warning("Divide operation requires at least two operands.")
        raise ValueError("Divide operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        logger.error("Invalid operands. Please provide numbers.", exc_info=True)
        raise ValueError("Invalid operands. Please provide numbers.")

    result = operands[0]
    for operand in operands[1:]:
        if operand == 0:
            logger.error("Cannot divide by zero.")
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= operand

    logger.info(f"Result of divide: {result}")
    return result
