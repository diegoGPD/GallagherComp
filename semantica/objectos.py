############Objectos necesarios para compilador##################

####CUBO SEMANTICO##############

cuboSemantico = {
    '+': {
        'int': {
            'int': 'int',
            'float': 'float',
            'string': 'string',
            'bool': 'int'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'string',
            'bool': 'float'
        },
        'string': {
            'int': 'string',
            'float': 'string',
            'string': 'string',
            'bool': 'string'
        },
        'bool': {
            'int': 'int',
            'float': 'float',
            'string': 'string',
            'bool': 'bool'
        },
    },
    '-': {
        'int': {
            'int': 'int',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'string': {
            'int': 'error',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        },
        'bool': {
            'int': 'int',
            'float': 'float',
            'string': 'error',
            'bool': 'bool'
        },
    },
    '*': {
        'int': {
            'int': 'int',
            'float': 'float',
            'string': 'error',
            'bool': 'int'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'float'
        },
        'string': {
            'int': 'string',
            'float': 'error',
            'string': 'error',
            'bool': 'string'
        },
        'bool': {
            'int': 'int',
            'float': 'float',
            'string': 'string',
            'bool': 'bool'
        },
    },
    '/': {
        'int': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'int'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'float'
        },
        'string': {
            'int': 'error',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        },
        'bool': {
            'int': 'float',
            'float': 'float',
            'string': 'int',
            'bool': 'bool'
        },
    },
    '=': {
            'int': {
                'int': 'int',
                'float': 'error',
                'string': 'error',
                'bool': 'error'
            },
            'float': {
                'int': 'error',
                'float': 'float',
                'string': 'error',
                'bool': 'error'
            },
            'string': {
                'int': 'error',
                'float': 'error',
                'string': 'string',
                'bool': 'error'
            },
            'bool': {
                'int': 'error',
                'float': 'error',
                'string': 'error',
                'bool': 'bool'
            },
        }
}

########## Tokens ###################

tokens = [
    'INI_INT',
    'INI_FLOAT',
    'INI_STRING',
    'INI_BOOL',
    'ID',
    'ADD',
    'LESS',
    'SPLIT_BY',
    'MULT_BY',
    'TIMES_BY_SAME',
    'SAME',
    'SET',
    'COMMA',
    'DOTCOMMA',
    'TWOPOINTS',
    'LEFTPARENT',
    'RIGHTPARENT',
    'LEFTBRACK',
    'RIGHTBRACK',
    'LEFTKEY',
    'RIGHTKEY',
    'LESSTN',
    'GREATERTN',
    'NOTSAME',
    'IGNORE'
    'GOTOFUNC',
    'GOTO',
    'GOTOT',
    'GOTOF',
    'ENDFUNC'
]

######### PALABRAS RESERVADAS #############

palabrasReservadas = {
    'Programa': 'PROG',
    'Main': 'MAIN',
    'func': 'FUNC',
    'let': 'LET',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'void': 'VOID',
    'printG' : 'PRINTG',
    'do' : 'DO',
    'while': 'WHILE',
}

######## RESERVADAS + TOKENS ############

tokens += list(palabrasReservadas.values())


