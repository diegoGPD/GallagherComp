from compilacion.excecutionMemory import excecutionMemory
from directions.excecutionMemoryAssignation import initVirtualMemory, jumpExcectuionPointer, advanceExcectuionPointer, \
    setVariableValue
from directions.excecutionMemoryGetter import getExectuionMemoryValue, isAddress


def virutalMachineRun(quads):
    initVirtualMemory()
    for quad in quads:
        if quad[0] == 'GOTO':
            jumpExcectuionPointer(quad[3])

        elif quad[0] == 'GOTOF':
            if (quad[1] == False):
                jumpExcectuionPointer(quad[3])
            else:
                advanceExcectuionPointer()

        elif quad[0] == 'PRINTG':
            print(getExectuionMemoryValue(quad[4]))

        elif quad[0] == '=':
            setVariableValue(quad[3], getExectuionMemoryValue(quad[1]))

        elif quad[0] == '>':
            expresionValue = getExectuionMemoryValue(quad[1]) > getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '<':
            expresionValue = getExectuionMemoryValue(quad[1]) < getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '!=':
            expresionValue = getExectuionMemoryValue(quad[1]) != getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '==':
            expresionValue = getExectuionMemoryValue(quad[1]) == getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '+':
            expresionValue = getExectuionMemoryValue(quad[1]) + getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '-':
            expresionValue = getExectuionMemoryValue(quad[1]) - getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '/':
            expresionValue = getExectuionMemoryValue(quad[1]) / getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '*':
            expresionValue = getExectuionMemoryValue(quad[1]) * getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '^':
            expresionValue = getExectuionMemoryValue(quad[1]) ** getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)


