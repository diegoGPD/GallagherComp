from compilacion.excecutionMemory import excecutionMemory


def getExectuionMemoryValue(letAddress):
    if letAddress in excecutionMemory['local'][excecutionMemory['localPointer']]:
        return excecutionMemory['local'][excecutionMemory['localPointer']][letAddress]
    elif letAddress in excecutionMemory['global']:
        return excecutionMemory['global'][letAddress]
    else:
        return excecutionMemory['constant'][letAddress]
