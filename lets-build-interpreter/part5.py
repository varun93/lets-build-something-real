INTEGER, PLUS, MINUS, MUL, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'

class Token:

    def __init__(self, type, value):
        # type can be integer, plus or eof
        self.type = type
        # value is 0-9, +, eof represents end of input
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(self.type, self.value)

class Lexer:

    def __init__(self, text):
        self.text = text
        self.current_char = text[0]
        self.pos = 0

    def skip_white_spaces(self):
        text = self.text
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
   
    def integer(self):

        number = 0
        while self.current_char is not None and self.current_char.isdigit():
            number = number*10 + int(self.current_char)
            self.advance()
        
        return number

    # advance the current position and set the current char
    def advance(self):
        
        text = self.text 

        self.pos += 1     

        if self.pos < len(text):
            self.current_char = text[self.pos]
        else:
            self.current_char = None


    def get_next_token(self):
        
        text, token = self.text, Token(None, EOF)
    
        while self.current_char is not None:
                
            if self.current_char.isspace():
                self.skip_white_spaces()

            elif self.current_char.isdigit():
                token = Token(INTEGER, self.integer())
                break
            
            elif self.current_char == '+':
                self.advance()
                token = Token(PLUS, '+')
                break

            elif self.current_char == '-':
                self.advance()
                token = Token(MINUS, '-')
                break

            elif self.current_char == '*':
                self.advance()
                token = Token(MUL, '*') 
                break
            
            elif self.current_char == '/':
                self.advance()
                token = Token(DIV, '/') 
                break

            else:
                self.error()

        return token

# why don't we have a token for a whitespace?
class Interpreter:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def error(self):
        raise Exception("Parse Error")
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    # currently assume term to be 
    def term(self):

        result = self.factor()

        while self.current_token.type in (MUL, DIV): 
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()

        return result

    def expr(self):
        
        result = self.term()

        while self.current_token.type in (PLUS, MINUS): 
            
            token = self.current_token
            
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result

def main():
    
    while True:

        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result) 

if __name__ == '__main__':
    main()