def readInput():
    input = open("puzzleInput25.txt", "r")
    readFile = input.read()
    return readFile   

def daytwentyfive():

    input = readInput()

    fuels = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
    decimals = dict(map(reversed, fuels.items()))

    numbers = []

    def toDecimal(number):
        result = sum([(5 ** ii) * fuels[c] for ii, c in enumerate(reversed(number))])
        return result

    def toFuel(number):
        value = []

        while number > 0:
            tempNum = number % 5
            if tempNum > 2:
                number += tempNum
                value.append(decimals[tempNum - 5])
            else: 
                value.append(str(tempNum))

            number //= 5

        return ''.join(reversed(value))

    for line in input.splitlines():
        numbers.append(toDecimal(line))

    snafu = toFuel(sum(numbers))
    return snafu

ergebnis = daytwentyfive()
print(ergebnis)
