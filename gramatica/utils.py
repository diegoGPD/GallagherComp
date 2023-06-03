######### Utils for Gramatic ###########
import compilacion.variables
from directions.virtualMemoryAssignation import setLetIDToVirtualMemory
from directions.virtualMemoryGetters import getVirtualMemoryAddressValue


def generateQuad(sign, left, right, letTarget):
    compilacion.variables.variables['quadCount'] += 1
    return [sign, left, right, letTarget]


def generateAssignQuad():
    rightOperand = compilacion.variables.variables['operands'].pop()
    leftOperand = compilacion.variables.variables['operands'].pop()
    rightAddress = getVirtualMemoryAddressValue(rightOperand, 'local', compilacion.variables.variables['currentFunc'])
    leftAddress = getVirtualMemoryAddressValue(leftOperand, 'local', compilacion.variables.variables['currentFunc'])
    equalSign = compilacion.variables.variables['operators'].pop()
    quad = generateQuad(equalSign, rightAddress, '', leftAddress)
    compilacion.variables.variables['quads'].append(quad)



def generateOperationQuad(conditional = False):
    rightOperand = compilacion.variables.variables['operands'].pop()
    leftOperand = compilacion.variables.variables['operands'].pop()
    rightAddress = getVirtualMemoryAddressValue(rightOperand, 'local', compilacion.variables.variables['currentFunc'])
    leftAddress = getVirtualMemoryAddressValue(leftOperand, 'local', compilacion.variables.variables['currentFunc'])
    sign = compilacion.variables.variables['operators'].pop()
    tempAddress = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                          compilacion.variables.variables['currentType'], 'temporal',
                                          compilacion.variables.variables['currentFunc'])
    quad = generateQuad(sign, leftAddress, rightAddress, tempAddress)
    if (conditional):
        setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                compilacion.variables.variables['currentType'], 'temporal',
                                compilacion.variables.variables['currentFunc'])
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    else:
        setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                compilacion.variables.variables['currentType'], 'temporal',
                                compilacion.variables.variables['currentFunc'])
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    compilacion.variables.variables['tempCount'] += 1
    compilacion.variables.variables['quads'].append(quad)



def generateJumpQuad(jumpType):
    if (jumpType == 'GOTO'):
        setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                compilacion.variables.variables['currentType'], 'temporal',
                                compilacion.variables.variables['currentFunc'])
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['tempCount'] += 1
    result = compilacion.variables.variables['operands'].pop()

    quad = generateQuad(jumpType, result, '', '')
    compilacion.variables.variables['quads'].append(quad)
    compilacion.variables.variables['jumps'].append(compilacion.variables.variables['quadCount'])



def completeJumpQuadruple():
    quadToJump = compilacion.variables.variables['quadCount']
    quadToComplete = compilacion.variables.variables['jumps'].pop()
    compilacion.variables.variables['quads'][quadToComplete][2] = quadToJump


def callFuncQuadruple(funcName):
    if (funcName) in compilacion.variables.variables['funciones']:
        compilacion.variables.variables['funcCalls'].append(funcName)
        quad = generateQuad('ERA', '', '', funcName)
        compilacion.variables.variables['quads'].append(quad)



def paramaterQuad():
    operand = compilacion.variables.variables['operands'].pop()
    compilacion.variables.variables['functionCalled'] = compilacion.variables.variables['funcCalls'][-1]
    if not len(compilacion.variables.variables['funciones'][compilacion.variables.variables['functionCalled']]['paramsTable']) <= compilacion.variables.variables['paramCounter']:
        print('ERROR TOO MANY PARAMETERS')
    quad = generateQuad('PARAMATER', operand, '', 'param' + str(compilacion.variables.variables['paramCounter']))
    compilacion.variables.variables['quads'].append(quad)

def restartFuncCalled():
    compilacion.variables.variables['paramCounter'] = 0
    functionCalled = compilacion.variables.variables['funcCalls'].pop()
    quad = generateQuad('GOTOFUNC', functionCalled, '', '')
    compilacion.variables.variables['quads'].append(quad)


def generateEndFuncQuad():
    compilacion.variables.variables['tempCount'] = 1
    quad = generateQuad('ENDFUNC', '', '', '')
    compilacion.variables.variables['quads'].append(quad)

def generateWriteQuad():
    valueToPrint = compilacion.variables.variables['operands'].pop()
    quad = generateQuad('PRINTG', '', '', valueToPrint)
    compilacion.variables.variables['quads'].append(quad)

def generateReturnQuad():
    result = compilacion.variables.variables['operands'].pop()
    resultAddress = getVirtualMemoryAddressValue(compilacion.variables.variables['currentFunc'], 'global')
    quad = generateQuad('=', result, '', resultAddress)
    compilacion.variables.variables['quads'].append(quad)


