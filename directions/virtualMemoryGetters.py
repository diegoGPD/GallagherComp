from compilacion.virtualMemory import virtualMemory
from directions.virtualMemoryAssignation import setConstantIDToVirtualMemory


def getVirtualMemoryAddressValue(let_ID, scope, func = ''):
    if str(let_ID).startswith('*'):
        return let_ID
    if (let_ID in virtualMemory['constant']):
        return virtualMemory['constant'][let_ID]
    if (scope != 'global'):
        keys = virtualMemory['local'][func]
        if let_ID in keys:
            return virtualMemory['local'][func][let_ID]
        else:
            return setConstantIDToVirtualMemory(let_ID)
    else:
        return virtualMemory[scope][let_ID]
