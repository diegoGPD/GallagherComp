from compilacion.excecutionMemory import excecutionMemory


def getExectuionMemoryValue(letAddress):
    if letAddress in excecutionMemory['local'][excecutionMemory['localPointer']]:
        return excecutionMemory['local'][excecutionMemory['localPointer']][letAddress]
    elif letAddress in excecutionMemory['global']:
        excecutionMemory['global'][letAddress]
    else:
        excecutionMemory['constant'][letAddress]
