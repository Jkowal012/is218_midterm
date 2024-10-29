# app/plugins/multiply/__init__.py
import logging

command_name = 'multiply'
logger = logging.getLogger(f"plugin.{command_name}")

def run(args, context=None):
    logger.info(f"Executing multiply with args: {args}")
    if len(args) < 2:
        logger.warning("Multiply operation requires at least two operands.")
        raise ValueError("Multiply operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        logger.error("Invalid operands. Please provide numbers.", exc_info=True)
        raise ValueError("Invalid operands. Please provide numbers.")

    result = 1.0
    for operand in operands:
        result *= operand

    logger.info(f"Result of multiply: {result}")
    return result
