def readInput():
    input = open("puzzleInput6.txt", "r")
    readFile = input.read()
    return readFile

def daySix():
    input = readInput()
    
    #Teil1
    #charPros = 4
    #buffer = 4

    #Teil2
    charPros = 14
    buffer = 14

    for i in range(len(input)):
        curBuffer = input[i: i+buffer]

        if(len(set(curBuffer)) == buffer):
            return charPros
        charPros += 1 
    return charPros
    

ergebnis = daySix()
print(ergebnis)