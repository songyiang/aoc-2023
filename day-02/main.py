import re

### PART 1 ###

def isValidGame(line, colors):
    texts = re.split(', |; ', line)
    for text in texts:
        res = re.split(' ', text)
        num, color = int(res[0]), res[1]
        if num > colors[color]:
            return False
    return True

colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        res = re.split(': |\n', line)
        gameLine, otherLine = res[0], res[1]
        if isValidGame(otherLine, colors):
            gameId = int(re.split(' ', gameLine)[1])
            sum += gameId
print(sum)

### PART 2 ###

def calcSetPower(line):
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    texts = re.split(', |; ', line)
    for text in texts:
        res = re.split(' ', text)
        num, color = int(res[0]), res[1]
        colors[color] = max(colors[color], num)
    prod = 1
    for val in colors.values():
        prod = prod * val
    return prod

sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        res = re.split(': |\n', line)
        sum += calcSetPower(res[1])
print(sum)
