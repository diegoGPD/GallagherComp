from compilacion.excecutionMemory import excecutionMemory


def getExectuionMemoryValue(letAddress):
    if letAddress in excecutionMemory['local'][excecutionMemory['excectuionPointer']]:
        return excecutionMemory['local'][excecutionMemory['excectuionPointer']][letAddress]
    elif letAddress in excecutionMemory['global']:
        excecutionMemory['global'][letAddress]
    else:
        excecutionMemory['constant'][letAddress]
