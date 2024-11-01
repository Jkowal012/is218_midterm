This is my midterm project!
Video Explanation: https://1drv.ms/v/s!Alp2pvja38_Egsxvx8EOArRY9hVOEw?e=XZOFz8

Introduction

This is a command-line calculator application built in Python. It features a modular plugin architecture that allows for easy addition of new operations. The application uses a Read-Eval-Print Loop (REPL) interface, enabling users to enter commands interactively and receive immediate results.
Features

    Interactive REPL Interface: Enter commands and receive results in real-time.
    Plugin Architecture: Easily extend the calculator by adding new plugins.
    Command Parsing: Robust command parsing for flexible user input.
    Calculation History: View and manage a history of your calculations.
    Comprehensive Testing: Ensures reliability and correctness of the calculator.

Installation
    1)
    Download and extract the zip or open the command line and type
    git clone https://github.com/Jkowal012/is218_midterm.git
    2)
    Once in the file, open the command prompt and change directories to where the file is stored using the "cd" command.
    3)
    Download the virtual env with:
    python -m venv venv
    and run it with: 
    venv\Scripts\activate(Windows)
    source venv/bin/activate(Linux/MacOS)
    4)
    Install dependencies using:
    pip install -r requirements.txt
    5)Start the main application with
    python3 main.py

Commands:
    Add
    Subtract
    Multiply
    Divide
    History
    History clear

License

    This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

    Faker Library: Used for generating test data.
    Pytest: Used for testing the application.