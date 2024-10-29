# app/plugins/history/__init__.py
import logging

command_name = 'history'
logger = logging.getLogger(f"plugin.{command_name}")

def run(args, context=None):
    logger.info(f"Executing history command with args: {args}")
    history_data = context.get('history_data') if context else None
    if history_data is None:
        print("History data is not available.")
        logger.error("History data is not provided in context.")
        return

    if args and args[0] == 'clear':
        clear_history(history_data)
    else:
        display_history(history_data)

def display_history(history_data):
    if history_data.empty:
        print("No history available.")
        logger.info("User requested history but it's empty.")
    else:
        print("Calculation History:")
        print(history_data.to_string(index=False))
        logger.info("Displayed calculation history.")

def clear_history(history_data):
    history_data.drop(history_data.index, inplace=True)
    print("History cleared.")
    logger.info("Calculation history cleared.")
