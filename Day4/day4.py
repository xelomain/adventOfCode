def readInput():
    input = open("puzzleInput4.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def dayFor():
    input = readInput()
    overlapPairs = 0

    for pairs in input:
        pairs = pairs.split(',')

        firstElf = pairs[0]
        secElf = pairs[1]
        firstElf = firstElf.split('-')
        secElf =secElf.split('-')

        firstSection = [section for section in range(int(firstElf[0]), int(firstElf[1]) + 1)]
        secSection = [section for section in range(int(secElf[0]), int(secElf[1]) + 1)]

        checkFirstToSec = all(section in firstSection for section in secSection)
        checkSecToFrist = all(section in secSection for section in firstSection)

        if checkFirstToSec or checkSecToFrist:
            overlapPairs += 1
        
    return overlapPairs


ergebnis = dayFor()
print(ergebnis)