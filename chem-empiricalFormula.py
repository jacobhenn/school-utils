from periodictable import carbon
from periodictable import hydrogen
from periodictable import oxygen
from periodictable import nitrogen

weightList = [carbon.mass, hydrogen.mass, oxygen.mass, nitrogen.mass]

class Repl:
    # Take user input
    def read():
        return(input('i: '))

    # Turn input into output
    def evaluate(userInput):
        if userInput == 'x':
            exit()
        inputList = userInput.split('+')
        inputList = [float(item) / weightList[inputList.index(item)] for item in inputList]
        inputList_min = min(inputList)
        if inputList_min == 0:
            inputList_sansZero = [item for item in inputList if item != 0]
            inputList_min = min(inputList_sansZero)
        inputList = [item / inputList_min for item in inputList]
        return(inputList)

    # Print output
    def printout(formulaOutput):
        print('o: ' + '\n'.join([str(item) for item in formulaOutput]))

while True:
    Repl.printout(Repl.evaluate(Repl.read()))
    
