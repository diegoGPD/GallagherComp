
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AT BOOL COMMA DO DOTCOMMA ELSE ENDFUNC FLOAT FUNC GOTO GOTOF GOTOT GREATERTN ID IF IGNOREGOTOFUNC INI_BOOL INI_FLOAT INI_INT INI_STRING INT LEFTBRACK LEFTKEY LEFTPARENT LESS LESSTN LET MAIN MULT_BY NOTSAME PRINTG PROG RIGHTBRACK RIGHTKEY RIGHTPARENT SAME SET SPLIT_BY TIMES_BY_SAME TWOPOINTS VOID WHILE\n      compile : PROG ID seen_program DOTCOMMA lets modules\n                |\n    \n        modules : func modules\n                |\n    seen_program :  lets : LET seen_lets type ID seen_ID_let aux_let DOTCOMMA lets\n                | empty\n    seen_lets : \n      type : INT seen_type\n           | FLOAT seen_type\n           | BOOL seen_type\n    seen_type :  seen_ID_let : \n      aux_let : COMMA ID seen_ID_let aux_let\n              |\n    \n        func : FUNC ID seen_func_name params TWOPOINTS return_func_type TWOPOINTS func_code\n    \n        seen_func_name :\n    \n        params : LEFTPARENT param_table_init param_declare RIGHTPARENT\n    \n      param_table_init :\n    \n        param_declare : type ID seen_ID_let param_declare\n                | COMMA param_declare\n                | empty\n    \n      return_func_type : type\n                        | VOID void_detect\n    \n        void_detect :\n    \n        func_code : LEFTKEY lets func_code_aux RIGHTKEY end_func\n    \n        end_func :\n    \n        func_code_aux : action func_code_aux\n                        |\n    \n        action : assign\n                | expresion_line\n                | condition\n                | while\n                | func_call\n                | write\n    \n          write : PRINTG LEFTPARENT write_found RIGHTPARENT DOTCOMMA\n    \n       write_found : write_found_aux\n                    | write_found_aux COMMA write_found\n    \n        write_found_aux : expresion_line print_exp\n                        | INI_STRING string_appear print_exp\n    \n        print_exp :\n    \n        string_appear :\n    \n        func_call : ID func_call_ID LEFTPARENT func_calls_params end_func_call_params RIGHTPARENT end_func_call DOTCOMMA\n                    |\n    \n        end_func_call_params :\n    \n        func_call_ID :\n    \n        end_func_call :\n    \n        func_calls_params : expresion_line parameter_call COMMA add_parameter func_calls_params\n                            | expresion_line parameter_call\n    \n        parameter_call :\n    \n        add_parameter :\n    \n        while : WHILE while_appear LEFTPARENT condition_expresion right_parent_condition RIGHTPARENT condition_code end_cond\n    \n        while_appear :\n    \n        condition : IF LEFTPARENT found_init_parent condition_expresion right_parent_condition RIGHTPARENT  condition_code end_cond condition_end_check\n    \n        condtion_appear :\n    \n        condition_end_check : ELSE condition_code end_condition\n                              | end_condition\n    \n        condition_code : LEFTKEY lets func_code_aux RIGHTKEY\n    \n        end_condition :\n    \n        end_cond :\n    \n        condition_signs : GREATERTN add_operator\n                        | LESSTN add_operator\n                        | SAME add_operator\n                        | NOTSAME add_operator\n                        |\n    \n        condition_expresion : expresion_line condtion_appear\n                    | expresion_line condition_signs expresion_line condtion_appear\n\n    \n        expresion_line : term term_appear\n                    | term term_appear aux_expresion\n    \n        aux_expresion : ADD add_operator expresion_line\n                      | LESS add_operator expresion_line\n    \n       term : fact factor_appear\n              | fact factor_appear aux_term\n    \n        aux_term : SPLIT_BY add_operator term\n                  | MULT_BY add_operator term\n    \n        fact : expo expo_appear\n              | expo expo_appear aux_expo\n    \n        expo :  parent_aux\n               | call_lets\n               | call_let\n    \n        parent_aux : LEFTPARENT found_init_parent expresion_line RIGHTPARENT found_end_parent\n    \n        right_parent_condition :\n    \n        found_init_parent :\n    \n        found_end_parent :\n    \n        aux_expo : TIMES_BY_SAME add_operator fact\n    \n        assign : call_let set_appear SET set_value\n                | call_let set_appear SET expresion_line seen_final_asignacion DOTCOMMA\n    \n       seen_final_asignacion :\n    \n        add_operand :\n    \n        add_operator :\n    \n         set_appear :\n    \n        term_appear :\n    \n        factor_appear :\n    \n        expo_appear :\n    \n        call_let : ID check_let_exists\n    \n       call_lets : INI_INT check_global_const_exists\n                    | INI_FLOAT check_global_const_exists\n    \n        check_global_const_exists : add_operand_const\n    \n        add_operand_const :\n    \n        check_let_exists :\n    \n        set_value : INI_INT aux_int_check append_operand DOTCOMMA\n                    | INI_FLOAT aux_float_check append_operand DOTCOMMA\n    \n        append_operand :\n    \n        aux_int_check :\n    \n        aux_float_check :\n    \n      empty :\n    '
    
_lr_action_items = {'PROG':([0,],[2,]),'$end':([0,1,5,6,8,9,10,13,38,45,47,74,89,],[-2,0,-106,-4,-7,-1,-4,-3,-106,-6,-16,-27,-26,]),'ID':([2,8,11,15,16,17,18,21,22,23,30,35,38,45,48,51,54,55,56,57,58,59,60,61,62,64,66,68,69,70,71,72,73,77,78,79,82,83,84,85,86,87,88,90,91,92,93,94,96,97,98,99,104,105,106,107,108,109,113,114,116,117,122,125,126,127,131,132,135,136,137,138,139,140,144,147,148,149,150,155,156,157,158,161,162,163,164,165,167,169,170,171,172,173,175,177,179,180,181,],[3,-7,14,20,-12,-12,-12,-9,-10,-11,39,43,-106,-6,-106,66,66,-30,-31,-32,-33,-34,-35,-80,-92,-83,-100,-93,-94,-78,-79,-99,-99,-68,-83,97,-95,97,-72,-76,-96,-98,-97,97,-69,-90,-90,97,-80,-100,97,97,-73,-90,-90,-77,-90,-86,97,97,-65,-84,97,97,97,97,-70,-71,97,-90,-90,-90,-90,-81,-36,-74,-75,-85,-87,-61,-62,-63,-64,-51,-101,-102,-60,-106,-60,97,-59,66,-52,-43,-54,-57,-59,-58,-56,]),'DOTCOMMA':([3,4,20,26,29,39,46,50,62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,110,111,112,117,121,128,129,130,131,132,140,147,148,149,151,152,160,168,],[-5,5,-13,-15,38,-13,-15,-14,-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,-88,-99,-99,-84,144,150,-103,-103,-70,-71,-81,-74,-75,-85,162,163,-47,173,]),'LET':([5,38,48,165,],[7,7,7,7,]),'FUNC':([5,6,8,10,38,45,47,74,89,],[-106,11,-7,11,-106,-6,-16,-27,-26,]),'INT':([7,12,25,27,28,36,43,49,],[-8,16,-19,16,16,16,-13,16,]),'FLOAT':([7,12,25,27,28,36,43,49,],[-8,17,-19,17,17,17,-13,17,]),'BOOL':([7,12,25,27,28,36,43,49,],[-8,18,-19,18,18,18,-13,18,]),'IF':([8,38,45,48,51,54,55,56,57,58,59,60,61,62,66,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,109,117,131,132,140,144,147,148,149,150,162,163,164,165,167,170,171,172,173,175,177,179,180,181,],[-7,-106,-6,-106,63,63,-30,-31,-32,-33,-34,-35,-80,-92,-100,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,-86,-84,-70,-71,-81,-36,-74,-75,-85,-87,-101,-102,-60,-106,-60,-59,63,-52,-43,-54,-57,-59,-58,-56,]),'WHILE':([8,38,45,48,51,54,55,56,57,58,59,60,61,62,66,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,109,117,131,132,140,144,147,148,149,150,162,163,164,165,167,170,171,172,173,175,177,179,180,181,],[-7,-106,-6,-106,65,65,-30,-31,-32,-33,-34,-35,-80,-92,-100,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,-86,-84,-70,-71,-81,-36,-74,-75,-85,-87,-101,-102,-60,-106,-60,-59,65,-52,-43,-54,-57,-59,-58,-56,]),'PRINTG':([8,38,45,48,51,54,55,56,57,58,59,60,61,62,66,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,109,117,131,132,140,144,147,148,149,150,162,163,164,165,167,170,171,172,173,175,177,179,180,181,],[-7,-106,-6,-106,67,67,-30,-31,-32,-33,-34,-35,-80,-92,-100,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,-86,-84,-70,-71,-81,-36,-74,-75,-85,-87,-101,-102,-60,-106,-60,-59,67,-52,-43,-54,-57,-59,-58,-56,]),'LEFTPARENT':([8,14,19,38,45,48,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,93,94,96,97,98,99,104,105,106,107,108,109,113,114,116,117,122,125,126,127,131,132,135,136,137,138,139,140,144,147,148,149,150,155,156,157,158,161,162,163,164,165,167,169,170,171,172,173,175,177,179,180,181,],[-7,-17,25,-106,-6,-106,64,64,-30,-31,-32,-33,-34,-35,-80,-92,78,-83,-53,-46,83,-93,-94,-78,-79,-99,-99,-68,-83,64,98,99,-95,64,-72,-76,-96,-98,-97,64,-69,-90,-90,64,-80,-100,64,64,-73,-90,-90,-77,-90,-86,64,64,-65,-84,64,64,64,64,-70,-71,64,-90,-90,-90,-90,-81,-36,-74,-75,-85,-87,-61,-62,-63,-64,-51,-101,-102,-60,-106,-60,64,-59,64,-52,-43,-54,-57,-59,-58,-56,]),'INI_INT':([8,38,45,48,51,54,55,56,57,58,59,60,61,62,64,66,68,69,70,71,72,73,77,78,79,82,83,84,85,86,87,88,90,91,92,93,94,96,97,98,99,104,105,106,107,108,109,113,114,116,117,122,125,126,127,131,132,135,136,137,138,139,140,144,147,148,149,150,155,156,157,158,161,162,163,164,165,167,169,170,171,172,173,175,177,179,180,181,],[-7,-106,-6,-106,72,72,-30,-31,-32,-33,-34,-35,-80,-92,-83,-100,-93,-94,-78,-79,-99,-99,-68,-83,72,-95,72,-72,-76,-96,-98,-97,111,-69,-90,-90,72,-80,-100,72,72,-73,-90,-90,-77,-90,-86,72,72,-65,-84,72,72,72,72,-70,-71,72,-90,-90,-90,-90,-81,-36,-74,-75,-85,-87,-61,-62,-63,-64,-51,-101,-102,-60,-106,-60,72,-59,72,-52,-43,-54,-57,-59,-58,-56,]),'INI_FLOAT':([8,38,45,48,51,54,55,56,57,58,59,60,61,62,64,66,68,69,70,71,72,73,77,78,79,82,83,84,85,86,87,88,90,91,92,93,94,96,97,98,99,104,105,106,107,108,109,113,114,116,117,122,125,126,127,131,132,135,136,137,138,139,140,144,147,148,149,150,155,156,157,158,161,162,163,164,165,167,169,170,171,172,173,175,177,179,180,181,],[-7,-106,-6,-106,73,73,-30,-31,-32,-33,-34,-35,-80,-92,-83,-100,-93,-94,-78,-79,-99,-99,-68,-83,73,-95,73,-72,-76,-96,-98,-97,112,-69,-90,-90,73,-80,-100,73,73,-73,-90,-90,-77,-90,-86,73,73,-65,-84,73,73,73,73,-70,-71,73,-90,-90,-90,-90,-81,-36,-74,-75,-85,-87,-61,-62,-63,-64,-51,-101,-102,-60,-106,-60,73,-59,73,-52,-43,-54,-57,-59,-58,-56,]),'RIGHTKEY':([8,38,45,48,51,53,54,55,56,57,58,59,60,61,62,66,68,69,70,71,72,73,75,77,82,84,85,86,87,88,91,96,97,104,107,109,117,131,132,140,144,147,148,149,150,162,163,164,165,167,170,171,172,173,175,177,178,179,180,181,],[-7,-106,-6,-106,-29,74,-29,-30,-31,-32,-33,-34,-35,-80,-92,-100,-93,-94,-78,-79,-99,-99,-28,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,-86,-84,-70,-71,-81,-36,-74,-75,-85,-87,-101,-102,-60,-106,-60,-59,-29,-52,-43,-54,-57,180,-59,-58,-56,]),'TWOPOINTS':([16,17,18,21,22,23,24,31,32,33,41,42,],[-12,-12,-12,-9,-10,-11,27,40,-23,-25,-24,-18,]),'COMMA':([20,25,26,28,36,39,43,46,49,62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,101,102,103,104,107,117,120,123,124,131,132,140,143,146,147,148,149,],[-13,-19,30,36,36,-13,-13,30,36,-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,122,-41,-42,-73,-77,-84,-50,-39,-41,-70,-71,-81,161,-40,-74,-75,-85,]),'RIGHTPARENT':([25,28,34,36,37,43,44,49,52,62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,95,96,97,100,101,102,103,104,107,115,116,117,118,119,120,123,124,131,132,133,134,140,141,142,143,145,146,147,148,149,154,166,174,],[-19,-106,42,-106,-22,-13,-21,-106,-20,-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,117,-80,-100,121,-37,-41,-42,-73,-77,-82,-55,-84,-82,-45,-50,-39,-41,-70,-71,153,-66,-81,159,160,-49,-38,-40,-74,-75,-85,-55,-67,-48,]),'VOID':([27,],[33,]),'LEFTKEY':([40,153,159,176,],[48,165,165,165,]),'TIMES_BY_SAME':([61,66,69,70,71,72,73,82,85,86,87,88,96,97,111,112,117,140,],[-80,-100,-94,-78,-79,-99,-99,-95,108,-96,-98,-97,-80,-100,-99,-99,-84,-81,]),'SPLIT_BY':([61,66,68,69,70,71,72,73,82,84,85,86,87,88,96,97,107,111,112,117,140,149,],[-80,-100,-93,-94,-78,-79,-99,-99,-95,105,-76,-96,-98,-97,-80,-100,-77,-99,-99,-84,-81,-85,]),'MULT_BY':([61,66,68,69,70,71,72,73,82,84,85,86,87,88,96,97,107,111,112,117,140,149,],[-80,-100,-93,-94,-78,-79,-99,-99,-95,106,-76,-96,-98,-97,-80,-100,-77,-99,-99,-84,-81,-85,]),'ADD':([61,62,66,68,69,70,71,72,73,77,82,84,85,86,87,88,96,97,104,107,111,112,117,140,147,148,149,],[-80,-92,-100,-93,-94,-78,-79,-99,-99,92,-95,-72,-76,-96,-98,-97,-80,-100,-73,-77,-99,-99,-84,-81,-74,-75,-85,]),'LESS':([61,62,66,68,69,70,71,72,73,77,82,84,85,86,87,88,96,97,104,107,111,112,117,140,147,148,149,],[-80,-92,-100,-93,-94,-78,-79,-99,-99,93,-95,-72,-76,-96,-98,-97,-80,-100,-73,-77,-99,-99,-84,-81,-74,-75,-85,]),'SET':([61,66,76,82,],[-91,-100,90,-95,]),'GREATERTN':([62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,116,117,131,132,140,147,148,149,],[-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,136,-84,-70,-71,-81,-74,-75,-85,]),'LESSTN':([62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,116,117,131,132,140,147,148,149,],[-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,137,-84,-70,-71,-81,-74,-75,-85,]),'SAME':([62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,116,117,131,132,140,147,148,149,],[-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,138,-84,-70,-71,-81,-74,-75,-85,]),'NOTSAME':([62,68,69,70,71,72,73,77,82,84,85,86,87,88,91,96,97,104,107,116,117,131,132,140,147,148,149,],[-92,-93,-94,-78,-79,-99,-99,-68,-95,-72,-76,-96,-98,-97,-69,-80,-100,-73,-77,139,-84,-70,-71,-81,-74,-75,-85,]),'INI_STRING':([83,122,],[103,103,]),'ELSE':([164,170,180,],[-60,176,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'compile':([0,],[1,]),'seen_program':([3,],[4,]),'lets':([5,38,48,165,],[6,45,51,171,]),'empty':([5,28,36,38,48,49,165,],[8,37,37,8,8,37,8,]),'modules':([6,10,],[9,13,]),'func':([6,10,],[10,10,]),'seen_lets':([7,],[12,]),'type':([12,27,28,36,49,],[15,32,35,35,35,]),'seen_func_name':([14,],[19,]),'seen_type':([16,17,18,],[21,22,23,]),'params':([19,],[24,]),'seen_ID_let':([20,39,43,],[26,46,49,]),'param_table_init':([25,],[28,]),'aux_let':([26,46,],[29,50,]),'return_func_type':([27,],[31,]),'param_declare':([28,36,49,],[34,44,52,]),'void_detect':([33,],[41,]),'func_code':([40,],[47,]),'func_code_aux':([51,54,171,],[53,75,178,]),'action':([51,54,171,],[54,54,54,]),'assign':([51,54,171,],[55,55,55,]),'expresion_line':([51,54,79,83,90,94,98,99,113,114,122,135,169,171,],[56,56,95,102,110,116,116,120,131,132,102,154,120,56,]),'condition':([51,54,171,],[57,57,57,]),'while':([51,54,171,],[58,58,58,]),'func_call':([51,54,171,],[59,59,59,]),'write':([51,54,171,],[60,60,60,]),'call_let':([51,54,79,83,90,94,98,99,113,114,122,125,126,127,135,169,171,],[61,61,96,96,96,96,96,96,96,96,96,96,96,96,96,96,61,]),'term':([51,54,79,83,90,94,98,99,113,114,122,125,126,135,169,171,],[62,62,62,62,62,62,62,62,62,62,62,147,148,62,62,62,]),'fact':([51,54,79,83,90,94,98,99,113,114,122,125,126,127,135,169,171,],[68,68,68,68,68,68,68,68,68,68,68,68,68,149,68,68,68,]),'expo':([51,54,79,83,90,94,98,99,113,114,122,125,126,127,135,169,171,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'parent_aux':([51,54,79,83,90,94,98,99,113,114,122,125,126,127,135,169,171,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'call_lets':([51,54,79,83,90,94,98,99,113,114,122,125,126,127,135,169,171,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'set_appear':([61,],[76,]),'term_appear':([62,],[77,]),'found_init_parent':([64,78,],[79,94,]),'while_appear':([65,],[80,]),'func_call_ID':([66,],[81,]),'check_let_exists':([66,97,],[82,82,]),'factor_appear':([68,],[84,]),'expo_appear':([69,],[85,]),'check_global_const_exists':([72,73,111,112,],[86,88,86,88,]),'add_operand_const':([72,73,111,112,],[87,87,87,87,]),'end_func':([74,],[89,]),'aux_expresion':([77,],[91,]),'write_found':([83,122,],[100,145,]),'write_found_aux':([83,122,],[101,101,]),'aux_term':([84,],[104,]),'aux_expo':([85,],[107,]),'set_value':([90,],[109,]),'add_operator':([92,93,105,106,108,136,137,138,139,],[113,114,125,126,127,155,156,157,158,]),'condition_expresion':([94,98,],[115,118,]),'func_calls_params':([99,169,],[119,174,]),'print_exp':([102,124,],[123,146,]),'string_appear':([103,],[124,]),'seen_final_asignacion':([110,],[128,]),'aux_int_check':([111,],[129,]),'aux_float_check':([112,],[130,]),'right_parent_condition':([115,118,],[133,141,]),'condtion_appear':([116,154,],[134,166,]),'condition_signs':([116,],[135,]),'found_end_parent':([117,],[140,]),'end_func_call_params':([119,],[142,]),'parameter_call':([120,],[143,]),'append_operand':([129,130,],[151,152,]),'condition_code':([153,159,176,],[164,167,179,]),'end_func_call':([160,],[168,]),'add_parameter':([161,],[169,]),'end_cond':([164,167,],[170,172,]),'condition_end_check':([170,],[175,]),'end_condition':([170,179,],[177,181,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> compile","S'",1,None,None,None),
  ('compile -> PROG ID seen_program DOTCOMMA lets modules','compile',6,'p_compile','reglas.py',15),
  ('compile -> <empty>','compile',0,'p_compile','reglas.py',16),
  ('modules -> func modules','modules',2,'p_modules','reglas.py',22),
  ('modules -> <empty>','modules',0,'p_modules','reglas.py',23),
  ('seen_program -> <empty>','seen_program',0,'p_seen_program','reglas.py',28),
  ('lets -> LET seen_lets type ID seen_ID_let aux_let DOTCOMMA lets','lets',8,'p_lets','reglas.py',36),
  ('lets -> empty','lets',1,'p_lets','reglas.py',37),
  ('seen_lets -> <empty>','seen_lets',0,'p_seen_lets','reglas.py',42),
  ('type -> INT seen_type','type',2,'p_type','reglas.py',50),
  ('type -> FLOAT seen_type','type',2,'p_type','reglas.py',51),
  ('type -> BOOL seen_type','type',2,'p_type','reglas.py',52),
  ('seen_type -> <empty>','seen_type',0,'p_seen_type','reglas.py',57),
  ('seen_ID_let -> <empty>','seen_ID_let',0,'p_seen_ID_let','reglas.py',62),
  ('aux_let -> COMMA ID seen_ID_let aux_let','aux_let',4,'p_aux_let','reglas.py',83),
  ('aux_let -> <empty>','aux_let',0,'p_aux_let','reglas.py',84),
  ('func -> FUNC ID seen_func_name params TWOPOINTS return_func_type TWOPOINTS func_code','func',8,'p_func','reglas.py',90),
  ('seen_func_name -> <empty>','seen_func_name',0,'p_seen_func_name','reglas.py',96),
  ('params -> LEFTPARENT param_table_init param_declare RIGHTPARENT','params',4,'p_params','reglas.py',109),
  ('param_table_init -> <empty>','param_table_init',0,'p_param_table_init','reglas.py',115),
  ('param_declare -> type ID seen_ID_let param_declare','param_declare',4,'p_param_declare','reglas.py',124),
  ('param_declare -> COMMA param_declare','param_declare',2,'p_param_declare','reglas.py',125),
  ('param_declare -> empty','param_declare',1,'p_param_declare','reglas.py',126),
  ('return_func_type -> type','return_func_type',1,'p_return_func_type','reglas.py',132),
  ('return_func_type -> VOID void_detect','return_func_type',2,'p_return_func_type','reglas.py',133),
  ('void_detect -> <empty>','void_detect',0,'p_void_detect','reglas.py',142),
  ('func_code -> LEFTKEY lets func_code_aux RIGHTKEY end_func','func_code',5,'p_func_code','reglas.py',150),
  ('end_func -> <empty>','end_func',0,'p_end_func','reglas.py',155),
  ('func_code_aux -> action func_code_aux','func_code_aux',2,'p_func_code_aux','reglas.py',162),
  ('func_code_aux -> <empty>','func_code_aux',0,'p_func_code_aux','reglas.py',163),
  ('action -> assign','action',1,'p_action','reglas.py',169),
  ('action -> expresion_line','action',1,'p_action','reglas.py',170),
  ('action -> condition','action',1,'p_action','reglas.py',171),
  ('action -> while','action',1,'p_action','reglas.py',172),
  ('action -> func_call','action',1,'p_action','reglas.py',173),
  ('action -> write','action',1,'p_action','reglas.py',174),
  ('write -> PRINTG LEFTPARENT write_found RIGHTPARENT DOTCOMMA','write',5,'p_write','reglas.py',179),
  ('write_found -> write_found_aux','write_found',1,'p_write_found','reglas.py',184),
  ('write_found -> write_found_aux COMMA write_found','write_found',3,'p_write_found','reglas.py',185),
  ('write_found_aux -> expresion_line print_exp','write_found_aux',2,'p_write_found_aux','reglas.py',190),
  ('write_found_aux -> INI_STRING string_appear print_exp','write_found_aux',3,'p_write_found_aux','reglas.py',191),
  ('print_exp -> <empty>','print_exp',0,'p_print_exp','reglas.py',196),
  ('string_appear -> <empty>','string_appear',0,'p_string_appear','reglas.py',203),
  ('func_call -> ID func_call_ID LEFTPARENT func_calls_params end_func_call_params RIGHTPARENT end_func_call DOTCOMMA','func_call',8,'p_func_call','reglas.py',210),
  ('func_call -> <empty>','func_call',0,'p_func_call','reglas.py',211),
  ('end_func_call_params -> <empty>','end_func_call_params',0,'p_end_func_call_params','reglas.py',216),
  ('func_call_ID -> <empty>','func_call_ID',0,'p_func_call_ID','reglas.py',224),
  ('end_func_call -> <empty>','end_func_call',0,'p_end_func_call','reglas.py',231),
  ('func_calls_params -> expresion_line parameter_call COMMA add_parameter func_calls_params','func_calls_params',5,'p_func_calls_params','reglas.py',238),
  ('func_calls_params -> expresion_line parameter_call','func_calls_params',2,'p_func_calls_params','reglas.py',239),
  ('parameter_call -> <empty>','parameter_call',0,'p_parameter_call','reglas.py',244),
  ('add_parameter -> <empty>','add_parameter',0,'p_add_parameter','reglas.py',251),
  ('while -> WHILE while_appear LEFTPARENT condition_expresion right_parent_condition RIGHTPARENT condition_code end_cond','while',8,'p_while','reglas.py',259),
  ('while_appear -> <empty>','while_appear',0,'p_while_appear','reglas.py',264),
  ('condition -> IF LEFTPARENT found_init_parent condition_expresion right_parent_condition RIGHTPARENT condition_code end_cond condition_end_check','condition',9,'p_condition','reglas.py',272),
  ('condtion_appear -> <empty>','condtion_appear',0,'p_condtion_appear','reglas.py',278),
  ('condition_end_check -> ELSE condition_code end_condition','condition_end_check',3,'p_condition_end_check','reglas.py',286),
  ('condition_end_check -> end_condition','condition_end_check',1,'p_condition_end_check','reglas.py',287),
  ('condition_code -> LEFTKEY lets func_code_aux RIGHTKEY','condition_code',4,'p_condition_code','reglas.py',292),
  ('end_condition -> <empty>','end_condition',0,'p_end_condition','reglas.py',297),
  ('end_cond -> <empty>','end_cond',0,'p_end_cond','reglas.py',304),
  ('condition_signs -> GREATERTN add_operator','condition_signs',2,'p_condition_signs','reglas.py',313),
  ('condition_signs -> LESSTN add_operator','condition_signs',2,'p_condition_signs','reglas.py',314),
  ('condition_signs -> SAME add_operator','condition_signs',2,'p_condition_signs','reglas.py',315),
  ('condition_signs -> NOTSAME add_operator','condition_signs',2,'p_condition_signs','reglas.py',316),
  ('condition_signs -> <empty>','condition_signs',0,'p_condition_signs','reglas.py',317),
  ('condition_expresion -> expresion_line condtion_appear','condition_expresion',2,'p_condition_expresion','reglas.py',322),
  ('condition_expresion -> expresion_line condition_signs expresion_line condtion_appear','condition_expresion',4,'p_condition_expresion','reglas.py',323),
  ('expresion_line -> term term_appear','expresion_line',2,'p_expresion_line','reglas.py',330),
  ('expresion_line -> term term_appear aux_expresion','expresion_line',3,'p_expresion_line','reglas.py',331),
  ('aux_expresion -> ADD add_operator expresion_line','aux_expresion',3,'p_aux_expresion','reglas.py',337),
  ('aux_expresion -> LESS add_operator expresion_line','aux_expresion',3,'p_aux_expresion','reglas.py',338),
  ('term -> fact factor_appear','term',2,'p_term','reglas.py',344),
  ('term -> fact factor_appear aux_term','term',3,'p_term','reglas.py',345),
  ('aux_term -> SPLIT_BY add_operator term','aux_term',3,'p_aux_term','reglas.py',351),
  ('aux_term -> MULT_BY add_operator term','aux_term',3,'p_aux_term','reglas.py',352),
  ('fact -> expo expo_appear','fact',2,'p_fact','reglas.py',358),
  ('fact -> expo expo_appear aux_expo','fact',3,'p_fact','reglas.py',359),
  ('expo -> parent_aux','expo',1,'p_expo','reglas.py',365),
  ('expo -> call_lets','expo',1,'p_expo','reglas.py',366),
  ('expo -> call_let','expo',1,'p_expo','reglas.py',367),
  ('parent_aux -> LEFTPARENT found_init_parent expresion_line RIGHTPARENT found_end_parent','parent_aux',5,'p_parenth_aux','reglas.py',373),
  ('right_parent_condition -> <empty>','right_parent_condition',0,'p_right_parent_condition','reglas.py',379),
  ('found_init_parent -> <empty>','found_init_parent',0,'p_found_init_parent','reglas.py',386),
  ('found_end_parent -> <empty>','found_end_parent',0,'p_found_end_parent','reglas.py',394),
  ('aux_expo -> TIMES_BY_SAME add_operator fact','aux_expo',3,'p_aux_expo','reglas.py',406),
  ('assign -> call_let set_appear SET set_value','assign',4,'p_assign','reglas.py',412),
  ('assign -> call_let set_appear SET expresion_line seen_final_asignacion DOTCOMMA','assign',6,'p_assign','reglas.py',413),
  ('seen_final_asignacion -> <empty>','seen_final_asignacion',0,'p_seen_final_asignacion','reglas.py',419),
  ('add_operand -> <empty>','add_operand',0,'p_add_operand','reglas.py',426),
  ('add_operator -> <empty>','add_operator',0,'p_add_operator','reglas.py',437),
  ('set_appear -> <empty>','set_appear',0,'p_set_appear','reglas.py',445),
  ('term_appear -> <empty>','term_appear',0,'p_term_appear','reglas.py',453),
  ('factor_appear -> <empty>','factor_appear',0,'p_factor_appear','reglas.py',465),
  ('expo_appear -> <empty>','expo_appear',0,'p_expo_appear','reglas.py',477),
  ('call_let -> ID check_let_exists','call_let',2,'p_call_let','reglas.py',488),
  ('call_lets -> INI_INT check_global_const_exists','call_lets',2,'p_call_lets','reglas.py',517),
  ('call_lets -> INI_FLOAT check_global_const_exists','call_lets',2,'p_call_lets','reglas.py',518),
  ('check_global_const_exists -> add_operand_const','check_global_const_exists',1,'p_check_global_const_exists','reglas.py',524),
  ('add_operand_const -> <empty>','add_operand_const',0,'p_add_operan_const','reglas.py',536),
  ('check_let_exists -> <empty>','check_let_exists',0,'p_check_let_exists','reglas.py',544),
  ('set_value -> INI_INT aux_int_check append_operand DOTCOMMA','set_value',4,'p_set_value','reglas.py',559),
  ('set_value -> INI_FLOAT aux_float_check append_operand DOTCOMMA','set_value',4,'p_set_value','reglas.py',560),
  ('append_operand -> <empty>','append_operand',0,'p_append_operand','reglas.py',567),
  ('aux_int_check -> <empty>','aux_int_check',0,'p_aux_int_check','reglas.py',574),
  ('aux_float_check -> <empty>','aux_float_check',0,'p_aux_float_check','reglas.py',586),
  ('empty -> <empty>','empty',0,'p_empty','reglas.py',599),
]
