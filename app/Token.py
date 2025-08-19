
class Token:
    def __init__(self, token_type, lexeme, literal):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal


    def print(self):
        print(f"{self.token_type} {self.lexeme} {self.literal}")