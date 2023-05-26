from past.builtins import raw_input
from ply import yacc, lex
from gramatica import reglas
from semantica import regex

lexer = lex.lex(module=regex)

parser = yacc.yacc(module=reglas)

def test():
    while True:
        try:
            s = raw_input('')
        except EOFError:
            break
        if not s: continue
        lexer.input(s)
        tok = lexer.token()
        print(tok)
        result = parser.parse(s)
        print(result)


test()

