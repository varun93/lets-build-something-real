INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'

class Token(object):

    def __init__(self, type, value):
        # type can be integer, plus or eof
        self.type = type
        # value is 0-9, +, eof represents end of input
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(self.type, self.value)

class Lexer(object):

    def __init__(self, text):
        self.pos = 0
        self.text = text
        self.current_char = text[0]

    def advance(self):
        self.pos += 1

        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    # this is the current character
    def integer(self):
        number = 0
        while self.current_char is not None and self.current_char.isdigit():
            number = number*10 + int(self.current_char)
            self.advance()
        
        return number

    def skip_white_spaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_white_spaces()
                continue
            
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(MUL, "*")

            if self.current_char == "/":
                self.advance()
                return Token(DIV, "/")
            
            if self.current_char == "(":
                self.advance()
                return Token(LPAREN, "(")

            if self.current_char == ")":
                self.advance()
                return Token(RPAREN, ")")

        return Token(EOF, None)        

class ASTNode(object):
    pass

class OpNode(ASTNode):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right

class NumNode:
    def __init__(self, token):
        self.value = token.value

"""
    expr = term ((MUL | DIV) term)*
    term = factor ((PLUS | MINUS) factor)*
    factor = INTEGER | LPAREN expr RPAREN
"""
class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def error(self):
        raise Exception("Parse Error")

    def factor(self):
        
        if self.current_token.type == INTEGER:
            token = self.current_token
            self.eat(INTEGER)
            return NumNode(token)
        elif self.current_token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def term(self):
        
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = OpNode(left = node, op = token, right = self.factor())
        
        return node

    def expr(self):
        
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = OpNode(left = node, op = token, right = self.term())

        return node

    def parse(self):
        return self.expr()

class Interpreter:

    def __init__(self, parser):
        self.parser = parser

    # Why do we need a different node type for integers alone?
    # What is the type of the node?
    def visit(self, node):
        if isinstance(node, OpNode):
            return self.visitBinaryOp(node)
        elif isinstance(node, NumNode):
            return self.visitNum(node)
        else:
            self.error(node)

    def error(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def visitBinaryOp(self, node):
        operator = node.op.type

        if operator == PLUS:
            return self.visit(node.left) + self.visit(node.right)

        if operator == MINUS:
            return self.visit(node.left) - self.visit(node.right)

        if operator == MUL:
            return self.visit(node.left) * self.visit(node.right)

        if operator == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visitNum(self, node):
        return node.value

    def intrepret(self):
        tree = self.parser.parse()
        return self.visit(tree)

def main():
    
    while True:

        try:
            text = input("calc> ")
        except EOFError:
            break

        if not text:
            continue
        
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        print(interpreter.intrepret())

if __name__ == '__main__':
    main()

"""
def visit(self, node):

    if(root.type === INTEGER):
        return root.val

    left = visit(root.left)
    right = visit(root.right)

    return evaluate(left, root.op, right)
"""