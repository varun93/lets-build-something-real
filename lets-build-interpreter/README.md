## Lets build an interpreter

Just came from a talk from Brian Kernighan in Stony Brook on Programming Languages. What a day to start!

I am following the [this](https://ruslanspivak.com/lsbasi-part1/) tutorial. 

- Part-1
    - Most basic lexer. expr method is the one which intreprets the text. Uses a helper called eat which validates the current token and consumes the next token.
    - Supports only one operation, doesn't handle white space and expects the number to a single number.

- Part-2
    - Accept multidigit
    - Skip Whitespace
    - Support for minus