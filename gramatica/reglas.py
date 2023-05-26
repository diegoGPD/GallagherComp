####### REGLAS GRAMATICALES ############
from semantica import regex

tokens = regex.tokens

def p_INI_INT_found(p):
    'd : INI_INT'

def p_INI_FLOAT_found(p):
    'c : INI_FLOAT'

def p_ID_found(p):
    't : ID'
    print('gohan')

