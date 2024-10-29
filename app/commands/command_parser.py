# app/commands/command_parser.py
import logging

logger = logging.getLogger(__name__)

def parse_command(user_input):
    logger.debug(f"Parsing user input: {user_input}")
    tokens = user_input.strip().split()
    if not tokens:
        logger.warning("No input provided.")
        raise ValueError("No input provided.")
    command_name = tokens[0]
    args = tokens[1:]
    logger.debug(f"Command: {command_name}, Args: {args}")
    return command_name, args
