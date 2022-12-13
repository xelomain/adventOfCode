def readInput():
    input = open("puzzleInput.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def dayOne():
    input = readInput()
    elfCalories = []
    summe = 0

    for calories in input:
        if calories == '':
            elfCalories.append(summe)
            summe = 0
        else:
            summe += int(calories)
    elfCalories.append(summe)
    elfCalories.sort()
    #return max(elfCalories)
    return sum(elfCalories[-3:])

ergebnis = dayOne()
print(ergebnis)