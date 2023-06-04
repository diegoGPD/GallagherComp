from compilacion.directionCounters import virtualMemoryCounter
from compilacion.virtualMemory import virtualMemory
from compilacion.virtualMemorySize import memorySizes


def setNewMatch(scope, type=''):
    if scope == "global":
        if type == 'int':
            address = memorySizes['GLOBAL_LET_INT_START'] + virtualMemoryCounter['global_let_int_counter']
            virtualMemoryCounter['global_let_int_counter'] += 1
            return address
        elif type == 'float':
            address = memorySizes['GLOBAL_LET_FLOAT_START'] + virtualMemoryCounter['global_let_float_counter']
            virtualMemoryCounter['global_let_float_counter'] += 1
            return address
        elif type == 'bool':
            address = memorySizes['GLOBAL_LET_BOOL_START'] + virtualMemoryCounter['global_let_bool_counter']
            virtualMemoryCounter['global_let_bool_counter'] += 1
            return address
        elif type == 'string':
            address = memorySizes['GLOBAL_LET_STRING_START'] + virtualMemoryCounter['global_let_string_counter']
            virtualMemoryCounter['global_let_string_counter'] += 1
            return address
    elif scope == "local":
        if type == 'int':
            address = memorySizes['LOCAL_LET_INT_START'] + virtualMemoryCounter['local_let_int_counter']
            virtualMemoryCounter['local_let_int_counter'] += 1
            return address
        elif type == 'float':
            address = memorySizes['LOCAL_LET_FLOAT_START'] + virtualMemoryCounter['local_let_float_counter']
            virtualMemoryCounter['local_let_float_counter'] += 1
            return address
        elif type == 'bool':
            address = memorySizes['LOCAL_LET_BOOL_START'] + virtualMemoryCounter['local_let_bool_counter']
            virtualMemoryCounter['local_let_bool_counter'] += 1
            return address
        elif type == 'string':
            address = memorySizes['LOCAL_LET_STRING_START'] + virtualMemoryCounter['local_let_string_counter']
            virtualMemoryCounter['local_let_string_counter'] += 1
            return address

    elif scope == "temporal":
        if type == 'int':
            address = memorySizes['TEMPORAL_LET_INT_START'] + virtualMemoryCounter['temporal_let_int_counter']
            virtualMemoryCounter['temporal_let_int_counter'] += 1
            return address
        elif type == 'float':
            address = memorySizes['TEMPORAL_LET_FLOAT_START'] + virtualMemoryCounter['temporal_let_float_counter']
            virtualMemoryCounter['temporal_let_float_counter'] += 1
            return address
        elif type == 'bool':
            address = memorySizes['TEMPORAL_LET_BOOL_START'] + virtualMemoryCounter['temporal_let_bool_counter']
            virtualMemoryCounter['temporal_let_bool_counter'] += 1
            return address
        elif type == 'string':
            address = memorySizes['TEMPORAL_LET_STRING_START'] + virtualMemoryCounter['temporal_let_string_counter']
            virtualMemoryCounter['temporal_let_string_counter'] += 1
            return address

    elif scope == "constant":
        address = memorySizes['CONSTANT_START'] + virtualMemoryCounter['constant_counter']
        virtualMemoryCounter['constant_counter'] += 1
        return address


def resetLocalVirtualMemory():
    virtualMemoryCounter['local_let_int_counter'] = 0
    virtualMemoryCounter['local_let_float_counter'] = 0
    virtualMemoryCounter['local_let_bool_counter'] = 0
    virtualMemoryCounter['local_let_string_counter'] = 0

    virtualMemoryCounter['temporal_let_int_counter'] = 0
    virtualMemoryCounter['temporal_let_float_counter'] = 0
    virtualMemoryCounter['temporal_let_bool_counter'] = 0
    virtualMemoryCounter['temporal_let_string_counter'] = 0


def setConstantIDToVirtualMemory(let_constant_ID):
    if let_constant_ID in list(virtualMemory["constant"].keys()):
        return virtualMemory["constant"][let_constant_ID]
    assignedAddress = setNewMatch("constant")
    virtualMemory["constant"][let_constant_ID] = assignedAddress
    return assignedAddress


def setLetIDToVirtualMemory(let_ID, type, scope, func):
    if let_ID in virtualMemory['constant']:
        return
    assignedAddress = setNewMatch(scope, type)
    if scope != 'global':
        if func in virtualMemory['local'] and let_ID not in virtualMemory['local'][func]:
            virtualMemory['local'][func][let_ID] = assignedAddress
        elif func not in virtualMemory['local']:
            virtualMemory['local'][func] = {let_ID: None}
            virtualMemory['local'][func][let_ID] = assignedAddress
    else:
        virtualMemory['global'][let_ID] = assignedAddress
    return assignedAddress
