import sys
from dataclasses import replace

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
# from SimpleLangErrorListener import SimpleLangErrorListener  # This is our custom error listener


class SimpleLangErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Real-time error detection: Raise an error with detailed info
        raise SyntaxError(f"Parsing error at line {line}, column {column}: {msg}")


class SimpleLangChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def check(self):
        try:
            # Read the content from the file
            with open(self.file_path, 'r') as file:
                code = file.read()

            # Create an input stream from the code
            input_stream = InputStream(code)

            # Initialize lexer and parser
            lexer = SimpleLangLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = SimpleLangParser(stream)

            # Add our custom error listener to the lexer and parser
            lexer.removeErrorListeners()  # Remove default error listeners
            parser.removeErrorListeners()  # Remove default error listeners
            error_listener = SimpleLangErrorListener()  # Our custom error listener
            lexer.addErrorListener(error_listener)
            parser.addErrorListener(error_listener)

            # Attempt to parse the input code
            tree = parser.program()  # Try parsing the program

            # If no error occurs, this means the code is parsed successfully
            print("Code parsed successfully!")

        except SyntaxError as e:
            # If an error occurs, capture the exception and print it
            raise SyntaxError(f"Syntax error detected: {e}")


if __name__ == "__main__":
    # Provide the path to your code file
    file_path = "code1.txt"  # Modify this to your actual file path

    # Check the code in the file
    checker = SimpleLangChecker(file_path)
    checker.check()
