######### Utils for Gramatic ###########
import compilacion.variables
from compilacion.virtualMemory import virtualMemory
from directions.virtualMemoryAssignation import setLetIDToVirtualMemory, setNewMatch, setArrayDirectsToVirtualMemory, \
    setConstantIDToVirtualMemory
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


def generateOperationQuad(conditional=False):
    rightOperand = compilacion.variables.variables['operands'].pop()
    leftOperand = compilacion.variables.variables['operands'].pop()
    rightAddress = getVirtualMemoryAddressValue(rightOperand, 'local', compilacion.variables.variables['currentFunc'])
    leftAddress = getVirtualMemoryAddressValue(leftOperand, 'local', compilacion.variables.variables['currentFunc'])
    sign = compilacion.variables.variables['operators'].pop()
    tempAddress = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                          compilacion.variables.variables['currentType'], 'temporal',
                                          compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    quad = generateQuad(sign, leftAddress, rightAddress, tempAddress)
    compilacion.variables.variables['tempCount'] += 1
    compilacion.variables.variables['quads'].append(quad)


def generateFalseJumpQuad():
    conditionVariable = compilacion.variables.variables['operands'].pop()
    quad = generateQuad('GOTOF', getVirtualMemoryAddressValue(conditionVariable, 'local',
                                                              compilacion.variables.variables['currentFunc']), '', '')
    compilacion.variables.variables['quads'].append(quad)
    compilacion.variables.variables['jumps'].append(compilacion.variables.variables['quadCount'])


def generateElseJumpQuad():
    falseJump = compilacion.variables.variables['jumps'].pop()
    quad = generateQuad('GOTO', '', '', '')
    compilacion.variables.variables['quads'].append(quad)
    compilacion.variables.variables['jumps'].append(compilacion.variables.variables['quadCount'])
    completeJumpQuadruple(falseJump)


def generationWhileEndJumpQuad():
    endJump = compilacion.variables.variables['jumps'].pop()
    returnJump = compilacion.variables.variables['jumps'].pop()
    quad = generateQuad('GOTO', '', '', returnJump)
    compilacion.variables.variables['quads'].append(quad)
    completeJumpQuadruple(endJump)


def completeJumpQuadruple(toFill):
    compilacion.variables.variables['quads'][toFill][3] = compilacion.variables.variables['quadCount'] + 1


def callFuncQuadruple(funcName):
    if (funcName) in compilacion.variables.variables['funciones']:
        compilacion.variables.variables['funcCalls'].append(funcName)
        quad = generateQuad('ERA', '', '', funcName)
        compilacion.variables.variables['quads'].append(quad)
        compilacion.variables.variables['operators'].append('(')


def paramaterQuad():
    operand = compilacion.variables.variables['operands'].pop()
    compilacion.variables.variables['functionCalled'] = compilacion.variables.variables['funcCalls'][-1]
    paramAddress = getVirtualMemoryAddressValue(operand, 'local', compilacion.variables.variables['currentFunc'])
    if not len(compilacion.variables.variables['funciones'][compilacion.variables.variables['functionCalled']][
                   'paramsTable']) <= compilacion.variables.variables['paramCounter']:
        print('ERROR TOO MANY PARAMETERS')
    quad = generateQuad('PARAMATER', paramAddress, '', compilacion.variables.variables['paramCounter'])
    compilacion.variables.variables['quads'].append(quad)


def restartFuncCalled():
    functionCalled = compilacion.variables.variables['funcCalls'].pop()
    quad = generateQuad('GOTOFUNC', functionCalled, '',
                        compilacion.variables.variables["funciones"][functionCalled]['quadStart'])
    compilacion.variables.variables['quads'].append(quad)
    tempAddress = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                          compilacion.variables.variables['currentType'], 'temporal',
                                          compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    compilacion.variables.variables['tempCount'] += 1
    quad = generateQuad('=', getVirtualMemoryAddressValue(functionCalled, 'global'), '', tempAddress)
    compilacion.variables.variables['quads'].append(quad)

    if compilacion.variables.variables['operators'][-1] == '(':
        compilacion.variables.variables['operators'].pop()

    compilacion.variables.variables['paramCounter'] = 0


def generateEndFuncQuad():
    if (compilacion.variables.variables['currentFunc'] == 'main'):
        quad = generateQuad('ENDALL', '', '', '')
        compilacion.variables.variables['quads'].append(quad)
        return
    compilacion.variables.variables['tempCount'] = 1
    quad = generateQuad('ENDFUNC', '', '', '')
    compilacion.variables.variables['quads'].append(quad)


def generateWriteQuad():
    valueToPrint = compilacion.variables.variables['operands'].pop()
    quad = generateQuad('PRINTG', '', '', getVirtualMemoryAddressValue(valueToPrint, 'local',
                                                                       compilacion.variables.variables['currentFunc']))
    compilacion.variables.variables['quads'].append(quad)


def generateReturnQuad():
    result = compilacion.variables.variables['operands'].pop()
    resultAddress = getVirtualMemoryAddressValue(compilacion.variables.variables['currentFunc'], 'global')
    quad = generateQuad('=',
                        getVirtualMemoryAddressValue(result, 'local', compilacion.variables.variables['currentFunc']),
                        '', resultAddress)
    compilacion.variables.variables['quads'].append(quad)


def calculateArrayR():
    arrayStart = \
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
            compilacion.variables.variables['currentLet']]['dimensionsNodes'][
            compilacion.variables.variables['dimensions'] - 1]['arrayStart'] or 0
    arrayEnd = \
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
            compilacion.variables.variables['currentLet']]['dimensionsNodes'][
            compilacion.variables.variables['dimensions'] - 1]['arrayEnd']

    compilacion.variables.variables['arrayR'] = (arrayEnd - arrayStart + 1) * compilacion.variables.variables['arrayR']


def endArrayDec():
    compilacion.variables.variables['dimensions'] = 1
    offset = 0
    arrayTotalSize = compilacion.variables.variables['arrayR']
    arrayDimensions = \
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
            compilacion.variables.variables['currentLet']]['dimensionsNodes']

    for dimension in arrayDimensions:
        arrayStart = dimension['arrayStart'] or 0
        arrayEnd = dimension['arrayEnd']
        m = compilacion.variables.variables['arrayR'] / (arrayEnd - arrayStart + 1)
        compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
            compilacion.variables.variables['currentLet']]['dimensionsNodes'][
            compilacion.variables.variables['dimensions'] - 1]['m'] = m
        compilacion.variables.variables['arrayR'] = m
        offset += arrayStart * m
        compilacion.variables.variables['dimensions'] -= 1

    compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][compilacion.variables.variables['currentLet']]['dimensionsNodes'][-1]['k'] = offset
    allArrayAddress(arrayTotalSize)


def allArrayAddress(size, type='int'):
    addresses = []
    for a in range(size - 1):
        if compilacion.variables.variables['currentFunc'] != compilacion.variables.variables['progName']:
            addresses.append(setNewMatch('local', type))
        else:
            addresses.append(setNewMatch('global', type))
    setArrayDirectsToVirtualMemory(compilacion.variables.variables['currentLet'],
                                   compilacion.variables.variables['currentFunc'], addresses)


def foundArrayAccess(letId):
    if letId not in compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'] and letId not in \
            compilacion.variables.variables['progName']['letsTable']:
        print('NOT POSSIBLE TO ACCESS THIS ARRAY')
    compilacion.variables.variables['dimensions'] = 1
    compilacion.variables.variables['dimensionStacks'].append(
        {'letId': letId, 'dimension': compilacion.variables.variables['dimensions']})
    compilacion.variables.variables['operators'].append('(')


def arrayExpresionHelper():
    currentDim = compilacion.variables.variables['dimensionStacks'][-1]['dimension']
    currentArrayLet = compilacion.variables.variables['dimensionStacks'][-1]['letId']
    currentDimention = getArrayDimention(currentArrayLet, currentDim)
    arrayStart = currentDimention['arrayStart'] or 0
    arrayStartDir = getVirtualMemoryAddressValue(arrayStart, 'local', compilacion.variables.variables['currentFunc'])
    arrayEnd = currentDimention['arrayEnd']
    arrayEndDir = getVirtualMemoryAddressValue(arrayEnd, 'local', compilacion.variables.variables['currentFunc'])
    m = currentDimention['m']
    constOrLetAddress = getVirtualMemoryAddressValue(compilacion.variables.variables['operands'][-1], 'local')
    quad = generateQuad('VERIFY', constOrLetAddress, arrayStartDir, arrayEndDir)
    compilacion.variables.variables['quads'].append(quad)
    currentDimentionkeys = list(currentDimention.keys())
    if 'end' not in currentDimentionkeys:
        aux = compilacion.variables.variables['operands'].pop()
        tempAddress = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                              compilacion.variables.variables['currentType'], 'temporal',
                                              compilacion.variables.variables['currentFunc'])
        quad = generateQuad('*', getVirtualMemoryAddressValue(aux, 'local'), setConstantIDToVirtualMemory(int(m)), tempAddress)
        compilacion.variables.variables['quads'].append(quad)
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['tempCount'] += 1
    else:
        aux1 = compilacion.variables.variables["operands"].pop()
        aux2 = compilacion.variables.variables["operands"].pop()
        temp = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                              compilacion.variables.variables['currentType'], 'temporal',
                                              compilacion.variables.variables['currentFunc'])
        quad = generateQuad('+', getVirtualMemoryAddressValue(aux1, 'local', compilacion.variables.variables['currentFunc']), getVirtualMemoryAddressValue(aux2, 'local', compilacion.variables.variables['currentFunc']), temp)
        compilacion.variables.variables['quads'].append(quad)
        compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
        compilacion.variables.variables['tempCount'] += 1

def endArrayAccess():
    currentArrayLet = compilacion.variables.variables['dimensionStacks'][-1]['letId']
    K = compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][
            compilacion.variables.variables['currentLet']]['dimensionsNodes'][-1]['k']
    pastTemp = compilacion.variables.variables['operands'].pop()
    temp1 = tempResult = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                              compilacion.variables.variables['currentType'], 'temporal',
                                              compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['operands'].append('temp' + str(compilacion.variables.variables['tempCount']))
    compilacion.variables.variables['tempCount'] += 1

    quad = generateQuad('+', getVirtualMemoryAddressValue(pastTemp,'local', compilacion.variables.variables['currentFunc']), getVirtualMemoryAddressValue(int(K), 'local', compilacion.variables.variables['currentFunc']), temp1)
    compilacion.variables.variables['quads'].append(quad)

    temp2 = tempResult = setLetIDToVirtualMemory('temp' + str(compilacion.variables.variables['tempCount']),
                                              compilacion.variables.variables['currentType'], 'temporal',
                                              compilacion.variables.variables['currentFunc'])
    compilacion.variables.variables['tempCount'] += 1
    arrayInitalAddress = getInitialArrayAddress(currentArrayLet)
    quad = generateQuad('+', temp1, getVirtualMemoryAddressValue(arrayInitalAddress,'local', compilacion.variables.variables['currentFunc']), temp2)
    compilacion.variables.variables['quads'].append(quad)
    compilacion.variables.variables['operands'].append('*'+str(temp2))
    if compilacion.variables.variables['operators'][-1] == "(":
        compilacion.variables.variables['operators'].pop()
    compilacion.variables.variables['dimensionStacks'].pop()
    compilacion.variables.variables['dimensionStacks']


def getArrayDimention(letId, dimention):
    dimention -= 1
    if letId in compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']][
        'letsTable']:
        arrayDimention = \
            compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][letId]['dimensionsNodes'][dimention]
        if len(compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable'][letId]['dimensionsNodes']) <= dimention + 1:
            arrayDimention['end'] = True
    else:
        arrayDimention = \
            compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable'][
                letId]['dimensionsNodes'][dimention]
        if len(compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']][
                   'letsTable'][letId]['dimensionsNodes']) <= dimention + 1:
            arrayDimention['end'] = True

    return arrayDimention

def getInitialArrayAddress(letId):
    if letId in compilacion.variables.variables['funciones'][compilacion.variables.variables['currentFunc']]['letsTable']:
        return getVirtualMemoryAddressValue(letId, 'local', compilacion.variables.variables['currentFunc'] )
    elif letId in compilacion.variables.variables['funciones'][compilacion.variables.variables['progName']]['letsTable']:
        return getVirtualMemoryAddressValue(letId, 'global' )

