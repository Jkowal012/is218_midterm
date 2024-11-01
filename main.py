# main.py

import logging
from app.calculator.calculator import Calculator
from config import LOG_LEVEL, LOG_FILE, ENVIRONMENT  # Import from config.py

def setup_logging():
    # Configure logging to write to a file and optionally to the console
    handlers = [logging.FileHandler(LOG_FILE)]
    if ENVIRONMENT == 'development':
        handlers.append(logging.StreamHandler())  # Enable console logging in development

    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),  # Use LOG_LEVEL from config.py
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=handlers
    )
    logging.info("Logging is configured.")

def main():
    setup_logging()
    print("Welcome to the calculator!")
    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()
