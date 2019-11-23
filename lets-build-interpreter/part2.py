INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token:

    def __init__(self, type, value):
        # type can be integer, plus or eof
        self.type = type
        # value is 0-9, +, eof represents end of input
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(self.type, self.value)

# why don't we have a token for a whitespace?
class Interpreter:

    def __init__(self, text):
        self.text = text
        self.current_token = None
        self.pos = 0

    def error(self):
        raise Exception("Parse Error")
    
    def skip_white_spaces(self):

        text = self.text

        while self.pos < len(text) and text[self.pos].isspace():
            self.pos += 1 
   
    def integer(self):

        number = 0
        text = self.text

        while self.pos < len(text) and text[self.pos].isdigit():
            number = number*10 + int(text[self.pos])
            self.pos += 1
        
        return number

    def get_next_token(self):
        
        text, token = self.text, None
    
        while self.pos < len(text):
                
            current_char = text[self.pos]

            if current_char.isspace():
                self.skip_white_spaces()

            elif current_char.isdigit():
                token = Token(INTEGER, self.integer())
                break

            elif current_char == '+':
                self.pos += 1
                token = Token(PLUS, '+') 
                break
            
            elif current_char == '-':
                self.pos += 1
                token = Token(MINUS, '-') 
                break

            else:
                self.error()

        return token

    def eat(self, token_type):
        
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token

        if op.type == PLUS:
            self.eat(PLUS)
        elif op.type == MINUS:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            return left.value + right.value
        elif op.type == MINUS:
            return left.value - right.value
        
def main():
    
    while True:

        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result) 

if __name__ == '__main__':
    main()