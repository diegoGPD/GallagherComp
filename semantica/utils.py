############### ERROR MESSAGES ##########
from semantica.objectos import cuboSemantico


def validate_set_type(op, letType, assignType):
    return cuboSemantico[op][letType][assignType]
