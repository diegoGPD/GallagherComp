#################COMPILADOR########################
from ply import yacc, lex

from GeneralUtils.printUtils import printAllResults
from gramatica import reglas
from semantica import regex
from virtualMachine.virtualMachine import virutalMachineRun

lexer = lex.lex(module=regex)

parser = yacc.yacc(module=reglas)

#"/Users/chuca/PycharmProjects/compiladorSL/gramatica/testsFiles/arrays.txt"
def main():
    print('Hi Welcome to Gallagher compiler')
    print('To start enter the path to your text file with your Gallagher code to start')
    print('#Pss rembmer to enter the full path, like this : /Users/chuca/PycharmProjects/compiladorSL/gramatica/testsFiles/arrays.txt')
    file = input("Your file path: ")
    openFile = open(file).read()
    parser.parse(openFile)
    virutalMachineRun()

    printAllResults()
main()
