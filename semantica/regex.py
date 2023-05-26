from semantica import objectos

######### REGEX ############

tokens = objectos.tokens

########### SYMBOL REGEX ##############

t_ADD = r'\+'
t_LESS = r'\-'
t_MULT_BY = r'\*'
t_SPLIT_BY = r'\/'
t_SAME = r'\=='
t_SET = r'\='
t_COMMA = r'\,'
t_DOTCOMMA = r'\;'
t_TWOPOINTS = r'\:'
t_LEFTPARENT = r'\('
t_RIGHTPARENT = r'\)'
t_LEFTBRACK = r'\['
t_RIGHTBRACK = r'\]'
t_LEFTKEY = r'\{'
t_RIGHTKEY = r'\}'
t_LESSTN = r'\<'
t_GREATERTN = r'\>'
t_NOTSAME = r'\!='

########### FUNCTION REGEX #################

def t_INI_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INI_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IGNORE(t):
    r' \s'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.value = objectos.palabrasReservadas.get(t.value, 'ID')
    return t

def t_INI_STRING(t):
    r'"([^"\n]|(\\"))*"$'
    t.type = 'INI_STRING'
    t.value = str(t.value)
    return t


def t_error(t):
    print('ERROR: CHARACTERS')
    print('CHECK YOUR CODE FOR ERROR')
    t.lexer.skip(1)
    return
