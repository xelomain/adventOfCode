import string

def readInput():
    input = open("puzzleInput3.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def dayThree():
    input = readInput()

    prioScore = {}
    letterList = list(string.ascii_letters)
    sumPrio = 0

    for i in range(len(letterList)):
        prioScore[letterList[i]] = i + 1

    #Teil1
    #for rucksack in input:
    #    rucksackSize = len(rucksack)
    #    firstSpace = rucksack[:rucksackSize//2]
    #    secondSpace = rucksack[rucksackSize//2:]
    #
    #    for item in firstSpace:
    #        if item in secondSpace:
    #            sumPrio += prioScore[item]
    #            break 
    
    #Teil2
    i = 0
    while i < len(input):
        firstRucksack = input[i]
        secondRucksack = input[i + 1]
        thirdRucksack = input[i + 2]

        for item in firstRucksack:
            if item in secondRucksack and item in thirdRucksack:
                sumPrio += prioScore[item]
                break
        i += 3

    return sumPrio

ergebnis = dayThree()
print(ergebnis)