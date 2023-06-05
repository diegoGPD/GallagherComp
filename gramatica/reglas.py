####### REGLAS GRAMATICALES ############
import compilacion.variables
from directions.virtualMemoryAssignation import setLetIDToVirtualMemory, setConstantIDToVirtualMemory, \
    resetLocalVirtualMemory
from gramatica.utils import generateQuad, generateAssignQuad, generateOperationQuad, generateFalseJumpQuad, \
    completeJumpQuadruple, callFuncQuadruple, paramaterQuad, restartFuncCalled, generateEndFuncQuad, generateWriteQuad, \
    generateReturnQuad, generateElseJumpQuad, generationWhileEndJumpQuad, endArrayDec, calculateArrayR, \
    foundArrayAccess, arrayExpresionHelper, endArrayAccess
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
              | LET seen_lets type ID seen_ID_let LEFTBRACK left_bracket_array add_dimension RIGHTBRACK end_array_init DOTCOMMA lets
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
        'type': compilacion.variables.variables['currentType']
    }
    if (compilacion.variables.variables['currentFunc'] != compilacion.variables.variables['progName']):
        setLetIDToVirtualMemory(p[-1], compilacion.variables.variables['currentType'], 'local', compilacion.variables.variables['currentFunc'])
    else:
        setLetIDToVirtualMemory(p[-1], compilacion.variables.variables['currentType'], 'global', compilacion.variables.variables['currentFunc'])


def p_access_array(p):
    """
        access_array : ID  LEFTBRACK access_array_found array_expresion RIGHTBRACK end_array_access
    """

def p_access_array_found(p):
    """
        access_array_found :
    """
    foundArrayAccess(p[-2])

def p_end_array_access(p):
    """
        end_array_access :
    """

    endArrayAccess()

def p_array_expresion(p):
    """
        array_expresion : expresion_line array_expresion_helper
                         | expresion_line array_expresion_helper COMMA array_comma_access array_expresion
    """



def p_array_expresion_helper(p):
    """
        array_expresion_helper :
    """
    arrayExpresionHelper()

def p_array_comma_access(p):
    """
        array_comma_access :
    """
    compilacion.variables.variables['dimensionStacks'][-1]['dimension'] += 1

def p_aux_let(p):
    """
      aux_let : COMMA ID seen_ID_let aux_let
              |
    """


def p_func(p):
    """
        func : FUNC ID seen_func_name params TWOPOINTS return_func_type TWOPOINTS func_code
    """


def p_seen_func_name(p):
    """
        seen_func_name :
    """
    compilacion.variables.variables['currentFunc'] = p[-1]
    compilacion.variables.variables['funciones'][p[-1]] = {'type': '', 'quadStart': compilacion.variables.variables['quadCount'] + 1}
    if not ('letsTable' in compilacion.variables.variables['funciones'][
            compilacion.variables.variables['currentFunc']]):
            compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']][
                'letsTable'] = {}
            setLetIDToVirtualMemory(p[-1], compilacion.variables.variables['currentType'], 'global', compilacion.variables.variables['progName'])
            compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'][compilacion.variables.variables['currentFunc']] = {
                'type': 'test',
                'value': None
            }
    if p[-1] == 'main':
        completeJumpQuadruple(1)



def p_params(p):
    '''
        params : LEFTPARENT param_table_init param_declare RIGHTPARENT
    '''


def p_param_table_init(p):
    '''
      param_table_init :
    '''
    if not ('paramsTable' in compilacion.variables.variables['funciones'][
        compilacion.variables.variables['currentFunc']]):
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['paramsTable'] = {}


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
        func_code : LEFTKEY func_code_start lets func_code_aux RIGHTKEY end_func
    """

def p_end_func(p):
    """
        end_func :
    """
    resetLocalVirtualMemory()
    generateEndFuncQuad()

def p_func_code_aux(p):
    """
        func_code_aux : action func_code_aux
                        |
    """


def p_action(p):
    """
        action : assign
                | expresion_line
                | condition
                | while
                | func_call DOTCOMMA
                | write
                | return
    """

def p_return(p):
    """
        return : RETURN expresion_line return_aux DOTCOMMA
                |
    """

def p_return_aux(p):
    """
        return_aux :
    """
    generateReturnQuad()


def p_write(p):
    """
          write : PRINTG LEFTPARENT write_found RIGHTPARENT DOTCOMMA
    """

def p_write_found(p):
    """
       write_found : write_found_aux
                    | write_found_aux COMMA write_found
    """

def p_write_found_aux(p):
    """
        write_found_aux : expresion_line print_exp
                        | INI_STRING string_appear print_exp
    """

def p_print_exp(p):
    """
        print_exp :
    """

    generateWriteQuad()

def p_string_appear(p):
    """
        string_appear :
    """
    setLetIDToVirtualMemory(p[-1], compilacion.variables.variables['currentType'], 'local', compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['operands'].append(p[-1])

def p_func_call(p):
    """
        func_call : AT ID func_call_ID LEFTPARENT func_calls_params end_func_call_params RIGHTPARENT end_func_call
                    |
    """

def p_end_func_call_params(p):
    """
        end_func_call_params :
    """

    if len(compilacion.variables.variables['funciones'][compilacion.variables.variables['functionCalled']]['paramsTable']) != compilacion.variables.variables['paramCounter'] :
        'Muchos o poquitos params bro'

def p_func_call_ID(p):
    """
        func_call_ID :
    """

    callFuncQuadruple(p[-1])

def p_end_func_call(p):
    """
        end_func_call :
    """
    restartFuncCalled()


def p_func_calls_params(p):
    """
        func_calls_params : expresion_line parameter_call COMMA add_parameter func_calls_params
                            | expresion_line parameter_call
    """

def p_parameter_call(p):
    """
        parameter_call :
    """

    paramaterQuad()

def p_add_parameter(p):
    """
        add_parameter :
    """

    compilacion.variables.variables['paramCounter'] += 1


def p_while(p):
    """
        while : WHILE while_appear LEFTPARENT condition_expresion RIGHTPARENT right_parent_condition condition_code while_end
    """

def p_while_end(p):
    """
        while_end :
    """
    generationWhileEndJumpQuad()

def p_while_appear(p):
    """
        while_appear :
    """

    compilacion.variables.variables['jumps'].append(compilacion.variables.variables['quadCount']);


def p_condition(p):
    """
        condition : IF LEFTPARENT found_init_parent condition_expresion right_parent_condition RIGHTPARENT  condition_code condition_end_check
    """


def p_condtion_appear(p):
    """
        condtion_appear :
    """

    if len(compilacion.variables.variables['operators']) and (compilacion.variables.variables['operators'][-1] == '>' or compilacion.variables.variables['operators'][-1] == '<' or compilacion.variables.variables['operators'][-1] == '==' or compilacion.variables.variables['operators'][-1] == '!=' or compilacion.variables.variables['operators'][-1] == '<=' or compilacion.variables.variables['operators'][-1] == '>='):
        generateOperationQuad(True)

def p_condition_end_check(p):
    """
        condition_end_check : ELSE else_appear condition_code end_condition
                              | end_condition
    """

def p_else_appear(p):
    """
        else_appear :
    """
    generateElseJumpQuad()

def p_condition_code(p):
    """
        condition_code : LEFTKEY lets func_code_aux RIGHTKEY
    """

def p_func_code_start(p):
    """
        func_code_start :
    """

    compilacion.variables.variables["currentFuncQuadStart"] = compilacion.variables.variables['quadCount'] + 1
def p_end_condition(p):
    """
        end_condition :
    """
    completeJumpQuadruple(compilacion.variables.variables['jumps'].pop())



def p_condition_signs(p):
    """
        condition_signs : GREATERTN add_operator
                        | LESSTN add_operator
                        | SAME add_operator
                        | NOTSAME add_operator
                        | LESSSAME add_operator
                        | MORESAME add_operator
    """

def p_condition_expresion(p):
    """
        condition_expresion :  expresion_line condition_signs expresion_line condtion_appear
                    | expresion_line condtion_appear

    """


def p_expresion_line(p):
    """
        expresion_line : term term_appear
                    | term term_appear aux_expresion
    """


def p_aux_expresion(p):
    """
        aux_expresion : ADD add_operator expresion_line
                      | LESS add_operator expresion_line
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
        fact : expo expo_appear
              | expo expo_appear aux_expo
    """


def p_expo(p):
    """
        expo :  parent_aux
               | call_lets
               | call_let
               | func_call
               | access_array
    """


def p_parenth_aux(p):
    """
        parent_aux : LEFTPARENT found_init_parent expresion_line RIGHTPARENT found_end_parent
    """


def p_right_parent_condition(p):
    """
        right_parent_condition :
    """
    generateFalseJumpQuad()

def p_found_init_parent(p):
    """
        found_init_parent :
    """

    compilacion.variables.variables['operators'].append('(')


def p_found_end_parent(p):
    """
        found_end_parent :
    """

    if len(compilacion.variables.variables['operators']) > 0 and compilacion.variables.variables['operators'][
        -1] == '(':
        compilacion.variables.variables['operators'].pop()
    else:
        print('Alto ahi vaquero no tienes omp')


def p_aux_expo(p):
    """
        aux_expo : TIMES_BY_SAME add_operator fact
    """


def p_assign(p):
    """
        assign : call_let set_appear SET set_value
                | call_let set_appear SET expresion_line seen_final_asignacion DOTCOMMA
                | access_array set_appear SET expresion_line seen_final_asignacion DOTCOMMA
    """


def p_seen_final_asignacion(p):
    """
       seen_final_asignacion :
    """

    generateAssignQuad()

def p_add_operand(p):
    """
        add_operand :
    """
    if (compilacion.variables.variables['currentFunc'] != compilacion.variables.variables['progName']):
        setLetIDToVirtualMemory(p[-1], compilacion.variables.variables['currentType'], 'local', compilacion.variables.variables['currentFunc'])
    else:
        setLetIDToVirtualMemory(p[-1], compilacion.variables.variables['currentType'], 'global', compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['operands'].append(p[-1])


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
            compilacion.variables.variables['operators'][-1] == '+' or compilacion.variables.variables['operators'][
        -1] == '-'):

        generateOperationQuad()
    else:
        return


def p_factor_appear(p):
    """
        factor_appear :
    """
    if len(compilacion.variables.variables['operators']) > 0 and (
            compilacion.variables.variables['operators'][-1] == '*' or compilacion.variables.variables['operators'][
        -1] == '/'):
        generateOperationQuad()
    else:
        return


def p_expo_appear(p):
    """
        expo_appear :
    """
    if len(compilacion.variables.variables['operators']) > 0 and compilacion.variables.variables['operators'][
        -1] == '^':
        generateOperationQuad()
    else:
        return

def p_bracket_array(p):
    """
        left_bracket_array :
    """
    compilacion.variables.variables['currentLet'] = p[-3]
    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][compilacion.variables.variables['currentLet']]['dimensionsNodes'] = [{}]
    compilacion.variables.variables['arrayDeclaration'] = True

def p_extra_dimension_found(p):
    """
        extra_dimension_found :
    """
    compilacion.variables.variables['dimensions'] += 1
    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][compilacion.variables.variables['currentLet']]['dimensionsNodes'].append({})


def p_add_dimension(p):
    """
        add_dimension : INI_INT array_start INI_INT array_end
                      | INI_INT array_start INI_INT array_end COMMA extra_dimension_found add_dimension
    """

def p_array_start(p):
    """
        array_start :
    """
    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][compilacion.variables.variables['currentLet']]['dimensionsNodes'][compilacion.variables.variables['dimensions'] - 1]['arrayStart'] = p[-1]

def p_array_end(p):
    """
        array_end :
    """
    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][compilacion.variables.variables['currentLet']]['dimensionsNodes'][compilacion.variables.variables['dimensions'] - 1]['arrayEnd'] = p[-1]

    calculateArrayR()


def p_end_array_init(p):
    """
        end_array_init :
    """
    endArrayDec()

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
            compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'][p[1]]['type']
    else:
        compilacion.variables.variables['currentType'] = \
            compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][p[1]]['type']

    if (compilacion.variables.variables['currentFunc'] != compilacion.variables.variables['progName']):
        setLetIDToVirtualMemory(p[1], compilacion.variables.variables['currentType'], 'local', compilacion.variables.variables['currentFunc'])
    else:
        setLetIDToVirtualMemory(p[1], compilacion.variables.variables['currentType'], 'global', compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['operands'].append(p[1])


def p_call_lets(p):
    """
       call_lets : INI_INT check_global_const_exists
                    | INI_FLOAT check_global_const_exists
    """



def p_check_global_const_exists(p):
    """
        check_global_const_exists : add_operand_const
    """
    if compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'].get(
            p[-1]) is None:
        compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'][
            p[-1]] = {
            'type': 'pruebaa'}
    setConstantIDToVirtualMemory(p[-1])
    p[0] = p[-1]

def p_add_operan_const(p):
    """
        add_operand_const :
    """

    compilacion.variables.variables['operands'].append(p[-1])


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
        set_value : INI_INT aux_int_check append_operand DOTCOMMA
                    | INI_FLOAT aux_float_check append_operand DOTCOMMA
    """

    generateAssignQuad()

def p_append_operand(p):
    """
        append_operand :
    """

    compilacion.variables.variables['operands'].append(p[-2])

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

    setConstantIDToVirtualMemory(p[-1])
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
