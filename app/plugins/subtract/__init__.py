# app/plugins/subtract/__init__.py
import logging

command_name = 'subtract'
logger = logging.getLogger(f"plugin.{command_name}")

def run(args):
    logger.info(f"Executing subtract with args: {args}")
    if len(args) < 2:
        logger.warning("Subtract operation requires at least two operands.")
        raise ValueError("Subtract operation requires at least two operands.")
    try:
        operands = [float(arg) for arg in args]
    except ValueError:
        logger.error("Invalid operands. Please provide numbers.", exc_info=True)
        raise ValueError("Invalid operands. Please provide numbers.")
    
    result = operands[0]
    for operand in operands[1:]:
        result -= operand
    
    logger.info(f"Result of subtract: {result}")
    return result
