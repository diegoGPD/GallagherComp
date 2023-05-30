####### REGLAS GRAMATICALES ############
import compilacion.variables
from gramatica.utils import generateQuad
from semantica import regex
from semantica.utils import validate_set_type

tokens = regex.tokens


def p_compile(p):
    """
      compile : PROG ID seen_program DOTCOMMA lets modules
                |
    """


def p_modules(p):
    """
        modules : func modules
                |
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
    if not ('letsTable' in compilacion.variables.variables['funciones'][
        compilacion.variables.variables['currentFunc']]):
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


def p_seen_ID_let(p):
    """ seen_ID_let : """
    newLet = p[-1]
    try:
        if newLet in compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']][
            'letsTable']:
            print('Redeclaration on variable', newLet)
    except (NameError, AttributeError) as e:
        print(e)
        pass
    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
        newLet] = {
        'type': compilacion.variables.variables['currentType']}


def p_aux_let(p):
    """
      aux_let : COMMA ID seen_ID_let aux_let
              |
    """


def p_func(p):
    """
        func : FUNC ID seen_func_name params TWOPOINTS return_func_type TWOPOINTS func_code
              |
    """


def p_seen_func_name(p):
    """
        seen_func_name :
    """
    compilacion.variables.variables['currentFunc'] = p[-1]
    compilacion.variables.variables['funciones'][p[-1]] = {'type': ''}


def p_params(p):
    '''
        params : LEFTPARENT param_table_init param_declare RIGHTPARENT
    '''


def p_param_table_init(p):
    '''
      param_table_init :
    '''
    if not ('letsTable' in compilacion.variables.variables['funciones'][
        compilacion.variables.variables['currentFunc']]):
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'] = {}


def p_param_declare(p):
    '''
        param_declare : type ID seen_ID_let param_declare
                | COMMA param_declare
                | empty
    '''


def p_return_func_type(p):
    '''
      return_func_type : type
                        | VOID void_detect
    '''

    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]["type"] = \
        compilacion.variables.variables['currentType']


def p_void_detect(p):
    '''
        void_detect :
    '''

    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]["type"] = "void"


def p_func_code(p):
    """
        func_code : LEFTKEY func_code_aux RIGHTKEY
    """


def p_func_code_aux(p):
    """
        func_code_aux : action func_code_aux
                        |
    """


def p_action(p):
    """
        action : assign
                | expresion
    """


def p_expresion(p):
    """
        expresion : term term_appear
                    | term term_appear aux_expresion
    """


def p_aux_expresion(p):
    """
        aux_expresion : ADD add_operator expresion
                      | LESS add_operator expresion
    """


def p_term(p):
    """
       term : fact factor_appear
              | fact factor_appear aux_term
    """


def p_aux_term(p):
    """
        aux_term : SPLIT_BY add_operator term
                  | MULT_BY add_operator term
    """


def p_fact(p):
    """
        fact : call_lets
    """


def p_assign(p):
    """
        assign : call_let add_let_target set_appear SET set_value
    """


def p_add_operand(p):
    """
        add_operand :
    """

    compilacion.variables.variables['operands'].append(p[-1])


def p_add_let_target(p):
    """
        add_let_target :
    """
    compilacion.variables.variables['letTargets'].append(p[-1])


def p_add_operator(p):
    """
        add_operator :
    """

    compilacion.variables.variables['operators'].append(p[-1])


def p_set_appear(p):
    """
         set_appear :
    """
    compilacion.variables.variables['currentSign'] = '='
    compilacion.variables.variables['operators'].append('=')


def p_term_appear(p):
    """
        term_appear :
    """
    if len(compilacion.variables.variables['operators']) > 0 and (
            compilacion.variables.variables['operators'][-1] == '+' or compilacion.variables.variables['operators'][-1] == '-'):
        right = compilacion.variables.variables['operands'].pop()
        left = compilacion.variables.variables['operands'].pop()
        sign = compilacion.variables.variables['operators'].pop()
        quad = generateQuad(sign, left, right, 'temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['tempCount'] += 1
        compilacion.variables.variables['quads'].append(quad)
        print(compilacion.variables.variables['quads'])
    else:
        return

def p_factor_appear(p):
    """
        factor_appear :
    """
    if len(compilacion.variables.variables['operators']) > 0 and (
            compilacion.variables.variables['operators'][-1] == '*' or compilacion.variables.variables['operators'][-1] == '/'):
        right = compilacion.variables.variables['operands'].pop()
        left = compilacion.variables.variables['operands'].pop()
        sign = compilacion.variables.variables['operators'].pop()
        quad = generateQuad(sign, left, right, 'temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['tempCount'] += 1
        compilacion.variables.variables['quads'].append(quad)
        print(compilacion.variables.variables['quads'])
    else:
        return


def p_call_let(p):
    """
        call_let : ID check_let_exists
    """

    var = compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'].get(
        p[1])
    if var is None:
        var = compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']][
            'letsTable'].get(p[1])
        # probar si falla sin esto al
        compilacion.variables.variables['currentType'] = \
            compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'][
                p[1]][
                'type']
    else:
        compilacion.variables.variables['currentType'] = \
            compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
                p[1]][
                'type']


def p_call_lets(p):
    """
       call_lets : INI_INT check_global_const_exists
                    | INI_FLOAT check_global_const_exists
    """


def p_check_global_const_exists(p):
    """
        check_global_const_exists : add_operand
    """
    if compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'].get(
            p[-1]) is None:
        compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'][
            p[-1]] = {
            'type': 'pruebaa'}

    p[0] = p[-1]


def p_check_let_exists(p):
    """
        check_let_exists :
    """

    compilacion.variables.variables['currentLet'] = p[-1]

    if compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'].get(
            p[-1]) is None and \
            compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'].get(
                p[-1]) is None:
        print("Error: Variable '%s' does not exist in scope '%s' nor in global" % (
            p[-1], compilacion.variables.variables['currentFunc']))


def p_set_value(p):
    """
        set_value : INI_INT aux_int_check append_operand DOTCOMMA generate_quad
                    | INI_FLOAT aux_float_check append_operand DOTCOMMA generate_quad
    """


def p_append_operand(p):
    """
        append_operand :
    """
    compilacion.variables.variables['operands'].append(p[-2])


def p_generate_quad(p):
    """
        generate_quad :
    """
    if compilacion.variables.variables['currentSign'] != '=':
        quad = generateQuad(compilacion.variables.variables['operators'].pop(),
                            compilacion.variables.variables['operands'].pop(),
                            compilacion.variables.variables['operands'].pop(),
                            compilacion.variables.variables['letTargets'].pop())
    else:
        quad = generateQuad(compilacion.variables.variables['operators'].pop(),
                            compilacion.variables.variables['operands'].pop(),
                            '',
                            compilacion.variables.variables['letTargets'].pop())
    compilacion.variables.variables['quads'].append(quad)
    print(compilacion.variables.variables['quads'])


def p_aux_int_check(p):
    """
        aux_int_check :
    """
    valid = validate_set_type(compilacion.variables.variables['currentSign'],
                              compilacion.variables.variables['currentType'], 'int')
    if valid == 'error':
        print('ERROR')
        p_error(-2)


def p_aux_float_check(p):
    """
        aux_float_check :
    """
    valid = validate_set_type(compilacion.variables.variables['currentSign'],
                              compilacion.variables.variables['currentType'], 'float')
    if valid == 'error':
        print('ERROR')
        p_error(-2)


def p_empty(p):
    """
      empty :
    """


def p_error(p):
    print(p)
    print("Syntax error found!")
