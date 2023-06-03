import compilacion.variables
from compilacion.virtualMemory import virtualMemory


def printAllResults():
    print('CUADRUPLOS')
    print('SIGN |  LEFT  | RIGHT |  RESULT')
    for qu in compilacion.variables.variables['quads']:
        print(qu[0], ' |', qu[1], ' |', qu[2], ' |', qu[3])

    print('Virtual Memory')
    for key, value in virtualMemory.items():
        print(key, '--')
        # Again iterate over the nested dictionary
        for subject, score in value.items():
            print(subject, ' : ', score)
