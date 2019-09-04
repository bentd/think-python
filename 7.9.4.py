from math import *
print

def run():
    while True:
        inputa=raw_input('What do you wish to evaluate? \n\n')
        if inputa == 'done':
            return
        print '\n', eval(inputa), '\n'
    return

run()
