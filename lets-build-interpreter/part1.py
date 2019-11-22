INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token:

    def __init__(self, type, value):
        # type can be integer, plus or eof
        self.type = type
        # value is 0-9, +, eof represents end of input
        self.value = value


    def __str__(self):
        return 'Token({type}, {value})'.format(self.type, self.value)



class Interpreter:

    def __init__(self, text):
        self.text = text
        self.current_token = None
        self.pos = 0

    def error(self):
        raise Exception("Parse Error")

    def get_next_token(self):
        
        text, token = self.text, None

        if self.pos == len(text):
            token = Token(EOF, None)
        else:
            
            current_char = text[self.pos]

            if current_char.isdigit():
                self.pos += 1
                token = Token(INTEGER, int(current_char))

            elif current_char == '+':
                self.pos += 1
                token = Token(PLUS, current_char) 

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
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        
        return result


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