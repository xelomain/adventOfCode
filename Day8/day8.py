def readInput():
    input = open("puzzleInput8.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def dayEight():

    input = readInput()

    rows = len(input)
    columns = len(input[0])

    edges = (rows*2) + ((columns-2)*2)
    total = edges

    for row in range(1, rows-1):
        for col in range(1, columns-1):
            tree = input[row][col]

            left  = [input[row][col-i] for i in range(1, col+1)]
            right = [input[row][col+i] for i in range(1, columns-col)]
            up =  [input[row-i][col] for i in range(1, row+1)]
            down = [input[row+i][col] for i in range(1, rows-row)]

            if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
                total += 1

    return total
    
ergebnis = dayEight()
print(ergebnis)