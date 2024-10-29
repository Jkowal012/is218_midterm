# main.py
import logging
from app.calculator.calculator import Calculator

def setup_logging():
    # Configure logging to only write to a file
    logging.basicConfig(
        level=logging.INFO,  # Set the base logging level
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Log messages go to app.log
            # Remove or comment out StreamHandler to stop console logging
            # logging.StreamHandler()
        ]
    )
    logging.info("Logging is configured.")

def main():
    setup_logging()
    print("Welcome to the calculator!")
    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()
