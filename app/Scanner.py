from .EToken import Token_type as EToken
from .Token import Token

class Scanner:
    def __init__(self, filename):
        """Initialize the scanner."""
        self.pos = 0 # my position for each character
        with open(filename) as file:
            self.file_contents = file.read() # Read whole file

    def tokenize(self):
        """Tokenize the file contents."""
        self.get_token_type()

    def get_token_type(self):
        while self.current_char():
            self.skip_whitespace()  # skip unnecessary spaces
            new_token = ()

            char = self.current_char()

            # Walrus operator since Py 3.8, set variable right in condition
            if identifier := self.read_identifier(): # Check if token is identifier
                new_token = Token("IDENTIFIER", identifier, "null")
            elif number := self.read_number(): # Check if token is number
                new_token = Token("NUMBER", number, number)
            elif string := self.read_string(): # Check if token is string
                new_token = Token("STRING", string, string)
            else: # Check other tokens
                for token in EToken:

                    if token.value == char:
                        new_token = Token(token.name, token.value, "null")
                        self.advance()
                        break
            new_token.print_()

        new_token = Token(EToken.EOF.name, "", "null")
        new_token.print_()

    def read_identifier(self):
        """Reads a complete identifier from current position
            :return identifier - in String format
        """
        char = self.current_char()

        # Check if first character is not number and if it is valid
        if not char or not (char.isalpha() or char == '_'):
            return None  # Not a valid identifier start

        identifier = ""

        # Read the complete identifier
        while (self.current_char() and
               (self.current_char().isalnum() or self.current_char() == '_')):
            identifier += self.current_char()
            self.advance()

        # Check reserved Keyword
        for token in EToken:
            if token.value == identifier:
                return None

        print("Vrací identifier: " + identifier)
        return identifier

    def read_number(self):
        """Reads a complete number from current position
            :return number - in String format
        """
        char = self.current_char()

        if not char or not char.isdigit():
            return None  # Not a valid number start

        number = ""
        has_decimal = False

        # Cycle through number
        while self.current_char():
            char = self.current_char()

            if char.isdigit():
                number += char
                self.advance()

            # Check if there is only one dot
            elif char == '.' and not has_decimal:
                next_pos = self.pos + 1
                # Index out of range handling
                if next_pos < len(self.file_contents):
                    # Check if after dot is another digit
                    if self.file_contents[next_pos].isdigit():
                        has_decimal = True
                        number += char
                        self.advance()
                    else:
                        break
                else:
                    break
            else:
                break

        return number # Return number in String

    def read_string(self):
        """Reads a complete string from current position
            :return string(name of variable) - in String format
        """
        char = self.current_char()

        if not char or not char == '"':
            return None  # Not a valid string start

        string = ""
        self.advance()
        # Check for ending "
        while self.current_char() != '"':
            char = self.current_char()
            string += char
            self.advance()

        return string # Return string message in type String

    def current_char(self):
        """Return current char position"""


        if self.pos >= len(self.file_contents):
            return None
        return self.file_contents[self.pos]

    def advance(self):
        """Move to next char by 1"""
        self.pos += 1

    def skip_whitespace(self):
        """Skips whitespace characters"""
        # it just checks if the position where self.pos is poiting is blank
        while self.current_char() and self.current_char().isspace():
            self.advance()