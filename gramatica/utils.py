######### Utils for Gramatic ###########
import compilacion.variables


def generateQuad(sign, left, right, letTarget):
    compilacion.variables.variables['quadCount'] += 1
    return [sign, left, right, letTarget]


def generateAssignQuad():
    rightOperand = compilacion.variables.variables['operands'].pop()
    leftOperand = compilacion.variables.variables['operands'].pop()
    equalSign = compilacion.variables.variables['operators'].pop()
    quad = generateQuad(equalSign, rightOperand, '', leftOperand)
    compilacion.variables.variables['quads'].append(quad)
    print(compilacion.variables.variables['quads'])


def generateOperationQuad(conditional = False):
    rightOperand = compilacion.variables.variables['operands'].pop()
    if (conditional): leftOperand = compilacion.variables.variables['operands'].pop()
    else: leftOperand = compilacion.variables.variables['operands'].pop()
    sign = compilacion.variables.variables['operators'].pop()
    quad = generateQuad(sign, leftOperand, rightOperand, 'temp' + str(compilacion.variables.variables['tempCount']))
    if (conditional): compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    else: compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    compilacion.variables.variables['tempCount'] += 1
    compilacion.variables.variables['quads'].append(quad)
    print(compilacion.variables.variables['quads'])


def generateJumpQuad(jumpType):
    if (jumpType == 'GOTO'):
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['tempCount'] += 1
    result = compilacion.variables.variables['operands'].pop()
    quad = generateQuad(jumpType, result, '', '')
    compilacion.variables.variables['quads'].append(quad)
    compilacion.variables.variables['jumps'].append(compilacion.variables.variables['quadCount'])
    print(compilacion.variables.variables['quads'])


def completeJumpQuadruple():
    quadToJump = compilacion.variables.variables['quadCount']
    quadToComplete = compilacion.variables.variables['jumps'].pop()
    compilacion.variables.variables['quads'][quadToComplete][2] = quadToJump
    print(len(compilacion.variables.variables['quads']))
    print(compilacion.variables.variables['quads'])
