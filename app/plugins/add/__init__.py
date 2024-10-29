# app/plugins/add/__init__.py
import logging

command_name = 'add'
logger = logging.getLogger(f"plugin.{command_name}")

def run(args):
    logger.info(f"Executing add with args: {args}")
    if len(args) < 2:
        logger.warning("Add operation requires at least two operands.")
        raise ValueError("Add operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        logger.error("Invalid operands. Please provide numbers.", exc_info=True)
        raise ValueError("Invalid operands. Please provide numbers.")
    result = sum(operands)
    logger.info(f"Result of add: {result}")
    return result
