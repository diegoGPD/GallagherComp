from compilacion.excecutionMemory import excecutionMemory


def getExectuionMemoryValue(letAddress):
    toAssign = letAddress
    if str(letAddress).startswith('*'):
        toAssign = getExectuionMemoryValue(int(str(letAddress)[1:]))
        if toAssign in excecutionMemory['local'][excecutionMemory['localPointer']]:
            return excecutionMemory['local'][excecutionMemory['localPointer']][toAssign]
        elif toAssign in excecutionMemory['global']:
            return excecutionMemory['global'][toAssign]
        elif toAssign in excecutionMemory['constant']:
            return excecutionMemory['constant'][toAssign]
        return toAssign
    if toAssign in excecutionMemory['local'][excecutionMemory['localPointer']]:
        return excecutionMemory['local'][excecutionMemory['localPointer']][toAssign]
    elif toAssign in excecutionMemory['global']:
        return excecutionMemory['global'][toAssign]
    else:
        return excecutionMemory['constant'][toAssign]
