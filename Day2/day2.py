def readInput():
    input = open("puzzleInput2.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def dayTwo():
    input = readInput()

    #X=Lose,Y=Unentschieden, Z=Win
    #Teil1
    #moves = {
    #    'A' : {
    #        'X': 4,
    #        'Y': 8,
    #        'Z': 3, 
    #    },
    #    'B' : {
    #        'X': 1,
    #        'Y': 5,
    #        'Z': 9,
    #    },
    #    'C' : {
    #        'X': 7,
    #        'Y': 2,
    #        'Z': 6,
    #    }
    #}

    moves = {
        'A' : {
            'X': 3,
            'Y': 4,
            'Z': 8, 
        },
        'B' : {
            'X': 1,
            'Y': 5,
            'Z': 9,
        },
        'C' : {
            'X': 2,
            'Y': 6,
            'Z': 7,
        }
    }
    
    score = 0

    for round in input:
        move = round[0]
        yourMove = round[2]
        score += moves[move][yourMove]
    return score

ergebnis = dayTwo()
print(ergebnis)