from compilacion.excecutionMemory import excecutionMemory
from compilacion.virtualMemory import virtualMemory


def initVirtualMemory():
    mainObject = {}
    for globalVarial in virtualMemory['global']:
        excecutionMemory['global'][virtualMemory['global'][globalVarial]] = None
    for mainVarial in virtualMemory['local']['main']:
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

def setGlobalVariableValue(letAddress, letVal):
    excecutionMemory['global'][letAddress] = letVal

def setFunctionVariableValue(letAddress, letVal):
    print('goku')
    excecutionMemory['local'][excecutionMemory['localPointer']][letAddress] = letVal

def setVariableValue(letAddress, letVal):
    print(letAddress, excecutionMemory['local'][excecutionMemory['localPointer']], virtualMemory)
    if letAddress in excecutionMemory['local'][excecutionMemory['localPointer']]:
        setFunctionVariableValue(letAddress, letVal)
    else:
        excecutionMemory['global'][letAddress] = letVal
        setGlobalVariableValue(letAddress, letVal)

def finishFunctionRun():
    excecutionMemory['localPointer'] -= 1
    excecutionMemory['local'].pop()

def jumpExcectuionPointer(quadNumber):
    excecutionMemory['excectuionPointer'] = quadNumber

def updateLocalPointer(localToUse):
    excecutionMemory['localPointer'] = localToUse

def advanceExcectuionPointer():
    excecutionMemory['excectuionPointer'] += 1





