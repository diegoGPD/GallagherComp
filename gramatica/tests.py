from past.builtins import raw_input
from ply import yacc, lex
from gramatica import reglas
from semantica import regex

lexer = lex.lex(module=regex)

parser = yacc.yacc(module=reglas)

def test():
    file = open("/Users/chuca/PycharmProjects/compiladorSL/gramatica/test1.txt").read()
    print(file)
    parser.parse(file)


test()

