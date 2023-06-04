from compilacion.virtualMemory import virtualMemory


def getVirtualMemoryAddressValue(let_ID, scope, func = ''):
    print(virtualMemory)
    if (let_ID in virtualMemory['constant']):
        return virtualMemory['constant'][let_ID]
    if (scope != 'global'):
        keys = virtualMemory['local'][func]
        if let_ID in keys:
            return virtualMemory['local'][func][let_ID]
        else:
            return virtualMemory['temporal'][func][let_ID]
    else:
        return virtualMemory[scope][let_ID]
