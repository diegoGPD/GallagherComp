import compilacion.variables
from compilacion.excecutionMemory import excecutionMemory
from compilacion.virtualMemory import virtualMemory


def printAllResults():
    print('\n')
    print('\n')
    print('\n')
    print('##################################################################################')
    print('INFORMACION DE COMPILACION')
    print('CUADRUPLOS')
    print('SIGN |  LEFT  | RIGHT |  RESULT')
    print(compilacion.variables.variables['quads'])

    print('Virtual Memory')
    for key, value in virtualMemory.items():
        print(key, '--')
        # Again iterate over the nested dictionary
        for subject, score in value.items():
            print(subject, ' : ', score)

    print('Execution Memory')
    print(excecutionMemory)
    print(compilacion.variables.variables)
    print('##################################################################################')
