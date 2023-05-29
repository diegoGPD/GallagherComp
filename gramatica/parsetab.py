
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD BOOL COMMA DO DOTCOMMA ELSE FLOAT FUNC GREATERTN ID IF IGNORE INI_FLOAT INI_INT INI_STRING INT LEFTBRACK LEFTKEY LEFTPARENT LESS LESSTN LET MAIN MULT_BY NOTSAME PRINTV PROG RIGHTBRACK RIGHTKEY RIGHTPARENT SAME SET SPLIT_BY TWOPOINTS WHILE\n      compile : PROG ID seen_program DOTCOMMA lets\n    seen_program :  lets : LET seen_lets type ID seen_ID_let aux_let DOTCOMMA lets\n                | empty\n    seen_lets : \n      type : INT seen_type\n           | FLOAT seen_type\n           | BOOL seen_type\n    seen_type :  seen_ID_let : \n      aux_let : COMMA ID seen_ID_let aux_let\n              |\n    \n      empty :\n    '
    
_lr_action_items = {'PROG':([0,],[2,]),'$end':([1,5,6,8,21,23,],[0,-13,-1,-4,-13,-3,]),'ID':([2,10,11,12,13,15,16,17,20,],[3,14,-9,-9,-9,-6,-7,-8,22,]),'DOTCOMMA':([3,4,14,18,19,22,24,25,],[-2,5,-10,-12,21,-10,-12,-11,]),'LET':([5,21,],[7,7,]),'INT':([7,9,],[-5,11,]),'FLOAT':([7,9,],[-5,12,]),'BOOL':([7,9,],[-5,13,]),'COMMA':([14,18,22,24,],[-10,20,-10,20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'compile':([0,],[1,]),'seen_program':([3,],[4,]),'lets':([5,21,],[6,23,]),'empty':([5,21,],[8,8,]),'seen_lets':([7,],[9,]),'type':([9,],[10,]),'seen_type':([11,12,13,],[15,16,17,]),'seen_ID_let':([14,22,],[18,24,]),'aux_let':([18,24,],[19,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> compile","S'",1,None,None,None),
  ('compile -> PROG ID seen_program DOTCOMMA lets','compile',5,'p_compile','reglas.py',9),
  ('seen_program -> <empty>','seen_program',0,'p_seen_program','reglas.py',13),
  ('lets -> LET seen_lets type ID seen_ID_let aux_let DOTCOMMA lets','lets',8,'p_lets','reglas.py',19),
  ('lets -> empty','lets',1,'p_lets','reglas.py',20),
  ('seen_lets -> <empty>','seen_lets',0,'p_seen_lets','reglas.py',24),
  ('type -> INT seen_type','type',2,'p_type','reglas.py',33),
  ('type -> FLOAT seen_type','type',2,'p_type','reglas.py',34),
  ('type -> BOOL seen_type','type',2,'p_type','reglas.py',35),
  ('seen_type -> <empty>','seen_type',0,'p_seen_type','reglas.py',40),
  ('seen_ID_let -> <empty>','seen_ID_let',0,'p_seen_ID_let','reglas.py',46),
  ('aux_let -> COMMA ID seen_ID_let aux_let','aux_let',4,'p_aux_let','reglas.py',59),
  ('aux_let -> <empty>','aux_let',0,'p_aux_let','reglas.py',60),
  ('empty -> <empty>','empty',0,'p_empty','reglas.py',65),
]