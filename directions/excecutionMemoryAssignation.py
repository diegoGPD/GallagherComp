from compilacion.excecutionMemory import excecutionMemory
from compilacion.virtualMemory import virtualMemory
from directions.excecutionMemoryGetter import getExectuionMemoryValue


def initVirtualMemory():
    mainObject = {}
    for globalVarial in virtualMemory['global']:
        excecutionMemory['global'][virtualMemory['global'][globalVarial]] = None
    for mainVarial in virtualMemory['local']['main']:
        if (mainVarial):
            mainObject[virtualMemory['local']['main'][mainVarial]] = None
    excecutionMemory['local'].append(mainObject)
    constVarialKeys = list(virtualMemory['constant'].keys())
    constVarialKeysCounter = 0
    for constVarial in list(virtualMemory['constant'].values()):
        excecutionMemory['constant'][constVarial] = constVarialKeys[constVarialKeysCounter]
        constVarialKeysCounter += 1


def addFuncVirtualMemory(funcName):
    funcObject = {}
    for funcVarial in virtualMemory['local'][funcName]:
        funcObject[virtualMemory['local'][funcName][funcVarial]] = None
    excecutionMemory['local'].append(funcObject)
    advanceExcectuionPointer()


def setParamter(value, parameterNumber):
    parameters = list((excecutionMemory['local'][-1].keys()))
    excecutionMemory['local'][-1][parameters[parameterNumber]] = getExectuionMemoryValue(value)
    advanceExcectuionPointer()

def setGlobalVariableValue(letAddress, letVal):
    excecutionMemory['global'][letAddress] = letVal


def setFunctionVariableValue(letAddress, letVal):
    excecutionMemory['local'][excecutionMemory['localPointer']][letAddress] = letVal



def setVariableValue(letAddress, letVal):
    if str(letAddress).startswith('*'):
        letAddress = int(str(letAddress)[1:])
        if not letVal in excecutionMemory['local'][excecutionMemory['localPointer']]:
            excecutionMemory['local'][excecutionMemory['localPointer']][letVal] = None
        setFunctionVariableValue(getExectuionMemoryValue(letAddress), letVal)
    if letAddress in excecutionMemory['local'][excecutionMemory['localPointer']]:
        setFunctionVariableValue(letAddress, letVal)
    else:
        excecutionMemory['global'][letAddress] = letVal
        setGlobalVariableValue(letAddress, letVal)
    advanceExcectuionPointer()


def finishFunctionRun():
    excecutionMemory['local'].pop()
    excecutionMemory['localPointer'] -= 1
    jumptTo = excecutionMemory['endFuncPointer'].pop() + 1
    jumpExcectuionPointer(jumptTo)

def jumpExcectuionPointer(quadNumber):
    excecutionMemory['excectuionPointer'] = quadNumber


def updateLocalPointer(localToUse):
    excecutionMemory['localPointer'] = localToUse


def advacneLocalPointer():
    excecutionMemory['localPointer'] = len(excecutionMemory['local']) - 1


def advanceExcectuionPointer():
    excecutionMemory['excectuionPointer'] += 1
