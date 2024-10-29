# main.py
import logging
from app.calculator.calculator import Calculator

def setup_logging():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,  # Set the base level to INFO
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging is configured.")

def main():
    setup_logging()
    logging.info("Application started.")
    print("Welcome to the calculator!")
    calculator = Calculator()
    calculator.run()
    logging.info("Application terminated.")

if __name__ == "__main__":
    main()
