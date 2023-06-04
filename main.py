#################COMPILADOR########################
from ply import yacc, lex

import compilacion.variables
from GeneralUtils.printUtils import printAllResults
from gramatica import reglas
from semantica import regex
from virtualMachine.virtualMachine import virutalMachineRun

lexer = lex.lex(module=regex)

parser = yacc.yacc(module=reglas)


def main():
    file = open("/Users/chuca/PycharmProjects/compiladorSL/gramatica/testsFiles/arrays.txt").read()
    parser.parse(file)
    virutalMachineRun()

main()
