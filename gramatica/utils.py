######### Utils for Gramatic ###########
import compilacion.variables


def generateQuad(sign, left, right, letTarget):
    compilacion.variables.variables['quadCount'] += 1
    return [sign, left, right, letTarget]
