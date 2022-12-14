import re

def readInput():
    input = open("puzzleInput5.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def dayFive():
    input = readInput()

    chest = []
    numStacks = 0
    moves = []

    for line in input:
        if '[' in line:
            chest.append(line)
        elif 'move' in line:
            moves.append(line)
        elif line != '' :
            numStacks = int(line[-2])
    
    layout = {}
    for i in range(numStacks):
        layout[i + 1] = []

    for row in reversed(chest):
        for i in range(numStacks):
            chestPos = (i * 4) + 1
            chestLetter = row[chestPos]
            if chestLetter != ' ':
                layout[i + 1].append(chestLetter)

    for move in moves:
        moveValue = re.findall(r'\d+', move)
        numOfMoves = int(moveValue[0])
        chestFrom = int(moveValue[1])
        chestTo = int(moveValue[2])
        #Teil1
        #chestToMove = reversed(layout[chestFrom][-numOfMoves:])
        chestToMove = layout[chestFrom][-numOfMoves:]
        layout[chestFrom] = layout[chestFrom][:-numOfMoves]
        layout[chestTo] += chestToMove

    topChest = ''
    for values in layout.values():
        topChest += values[-1]
    return topChest 

ergebnis = dayFive()
print(ergebnis)
