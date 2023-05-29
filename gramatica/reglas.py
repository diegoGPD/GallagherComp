####### REGLAS GRAMATICALES ############
import compilacion.variables
from semantica import regex

tokens = regex.tokens

def p_compile(p):
    """
      compile : PROG ID seen_program DOTCOMMA lets
    """

def p_seen_program(p):
    """seen_program : """
    compilacion.variables.variables['funciones'][p[-1]] = {'type': 'Programa'}
    compilacion.variables.variables['progName'] = p[-1]
    compilacion.variables.variables['currentFunc'] = p[-1]

def p_lets(p):
    """ lets : LET seen_lets type ID seen_ID_let aux_let DOTCOMMA lets
                | empty
    """

def p_seen_lets(p):
    """seen_lets : """
    print('asdfasdfadsfadsf')

    if not ('letsTable' in compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]):
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'] = {}


def p_type(p):
    """
      type : INT seen_type
           | FLOAT seen_type
           | BOOL seen_type
    """


def p_seen_type(p):
    """seen_type : """
    compilacion.variables.variables['currentType'] = p[-1]
    print(compilacion.variables.variables['currentType'])


def p_seen_ID_let(p):
    """ seen_ID_let : """
    newLet = p[-1]
    try:
        if newLet in compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable']:
            print('Redeclaration on variable', newLet)
    except (NameError, AttributeError) as e:
        print(e)
        pass
    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][newLet] = {
        'type': compilacion.variables.variables['currentType']}

def p_aux_let(p):
    """
      aux_let : COMMA ID seen_ID_let aux_let
              |
    """

def p_empty(p):
    """
      empty :
    """

def p_error(p):
    print(p)
    print("Syntax error found!")