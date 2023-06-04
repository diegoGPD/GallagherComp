#################COMPILADOR########################
from ply import yacc, lex

import compilacion.variables
from GeneralUtils.printUtils import printAllResults
from directions.excecutionMemoryAssignation import initVirtualMemory
from gramatica import reglas
from gramatica.tests import parser
from semantica import regex
from virtualMachine.virtualMachine import virutalMachineRun

lexer = lex.lex(module=regex)

parser = yacc.yacc(module=reglas)


def main():
    file = open("/Users/chuca/PycharmProjects/compiladorSL/gramatica/testsFiles/test2.txt").read()
    parser.parse(file)
    virutalMachineRun(compilacion.variables.variables['quads'])
    printAllResults()

main()
