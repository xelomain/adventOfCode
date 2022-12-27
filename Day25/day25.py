def readInput():
    input = open("puzzleInput25.txt", "r")
    readFile = input.read()
    return readFile   

def daytwentyfive():

    input = readInput()

    fuels = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
    decimals = dict(map(reversed, fuels.items()))

    numbers = []

    def to_decimal(number):
        result = sum([(5 ** ii) * fuels[c] for ii, c in enumerate(reversed(number))])
        return result

    def to_fuel(number):
        value = []

        while number > 0:
            remainder = number % 5
            if remainder > 2:
                number += remainder
                value.append(decimals[remainder - 5])
            else: 
                value.append(str(remainder))

            number //= 5

        return ''.join(reversed(value))

    for line in input.splitlines():
        numbers.append(to_decimal(line))

    snafu = to_fuel(sum(numbers))
    return snafu

ergebnis = daytwentyfive()
print(ergebnis)
