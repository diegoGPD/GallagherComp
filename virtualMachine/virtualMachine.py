import compilacion.variables
from compilacion.excecutionMemory import excecutionMemory
from directions.excecutionMemoryAssignation import initVirtualMemory, jumpExcectuionPointer, advanceExcectuionPointer, \
    setVariableValue, updateLocalPointer, advacneLocalPointer, addFuncVirtualMemory, setParamter, finishFunctionRun
from directions.excecutionMemoryGetter import getExectuionMemoryValue


def virutalMachineRun():
    initVirtualMemory()
    quads = compilacion.variables.variables['quads']
    run = True
    while run:
        quad = quads[excecutionMemory['excectuionPointer']]
        if quad[0] == 'GOTO':
            jumpExcectuionPointer(quad[3])

        elif quad[0] == 'GOTOF':
            if getExectuionMemoryValue(quad[1]) == False:
                jumpExcectuionPointer(quad[3])
            else:
                advanceExcectuionPointer()

        elif quad[0] == 'GOTOFUNC':
            excecutionMemory['endFuncPointer'].append(excecutionMemory['excectuionPointer'])
            advacneLocalPointer()
            jumpExcectuionPointer(quad[3])

        elif quad[0] == 'ERA':
            addFuncVirtualMemory(quad[3])


        elif quad[0] == 'PARAMATER':
            setParamter(quad[1], quad[3])

        elif quad[0] == 'ENDFUNC':
            finishFunctionRun()

        elif quad[0] == 'PRINTG':
            a = getExectuionMemoryValue(quad[3])
            print(a)
            advanceExcectuionPointer()

        elif quad[0] == '=':
            setVariableValue(quad[3], getExectuionMemoryValue(quad[1]))

        elif quad[0] == '>':
            expresionValue = getExectuionMemoryValue(quad[1]) > getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '<':
            expresionValue = getExectuionMemoryValue(quad[1]) < getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '<=':
            expresionValue = getExectuionMemoryValue(quad[1]) <= getExectuionMemoryValue(quad[2])
            setVariableValue(quad[3], expresionValue)

        elif quad[0] == '>=':
            expresionValue = getExectuionMemoryValue(quad[1]) >= getExectuionMemoryValue(quad[2])
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

        elif quad[0] == 'ENDALL':
            run = False



