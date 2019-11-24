## Lets build an interpreter

Just came from a talk from Brian Kernighan in Stony Brook on Programming Languages. What a day to start!

I am following the [this](https://ruslanspivak.com/lsbasi-part1/) tutorial. 

- Part-1
    - Most basic lexer. expr method is the one which intreprets the text. Uses a helper called eat which    validates the current token and consumes the next token.
    - Supports only one operation, doesn't handle white space and expects the number to a single number.

- Part-2
    - Accept multidigit
    - Skip Whitespace  
    - Support for minus
    - Lexeme is a sequence of characters that form a token.
    - The logic to scan the next character is abstracted by using a self.advance method

- Part-3
    - Multiple terms to add and subtract

- Part-4
    - A note about BNF or Context Free grammars
    - Contains several rules
    - Rules are formed by having non-terminals as LHS and terminals/non-terminals at RHS.
    - Sample Grammar for multiplication/divison of grammar 
        - expr : factor ((MUL | DIV) factor) * 
        - factor : INTEGER
    -  3 * 7 / 2
        - expr 
        - factor ((MUL | DIV) factor)*
        - factor MUL factor DIV factor
        - INTEGER MUL INTEGER DIV INTEGER
        -   3     *     7      /   2

- Part-5
    - Gramamar for evaluting arithmetic expressions
    - expr : term ((PLUS | MINUS) term)*
    - term : factor ((MUL | DIV) factor)*
    - factor : INTEGER

    Example: 3  +  4  *  5  -  6
    
    => (3  +  4  *  5)  -  (6)
    => ((3 + (4 * 5)) - 6) 
    => T1 - T3
    => T1 <- T2 + T3
    => T2 <- 3
    => T3 <- 4 MUL 5
    => T3 <- 6 

- Part-6
    - expr : term ((PLUS | MINUS) term)*
    - term : factor ((MUL | DIV) factor)*
    - factor : INTEGER | LPAREN expr RPAREN