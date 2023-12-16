### PART 1 ###

def hasReflection(pattern, firstPtr, lastPtr):
    while firstPtr < lastPtr:
        if not all(x == y for x, y in zip(pattern[firstPtr], pattern[lastPtr])):
            return False
        firstPtr += 1
        lastPtr -= 1
    return True

def getPatternNote(pattern):
    for i in range(len(pattern) - 1):
        sideLength = min(i + 1, len(pattern) - i - 1)
        firstPtr = i - sideLength + 1
        lastPtr = i + sideLength
        if hasReflection(pattern, firstPtr, lastPtr):
            return i + 1
    return 0

def solve():
    num = 0
    with open('input.txt', 'r') as f:
        patternRows = []
        patternCols = []
        for line in f:
            line = line.strip()
            if line == '':
                num += getPatternNote(patternRows) * 100
                num += getPatternNote(patternCols)
                patternRows = []
                patternCols = []
                continue

            if len(patternCols) == 0:
                patternCols = [[] for _ in range(len(line))]

            patternRows.append([char for char in line])
            for i in range(len(line)):
                patternCols[i].append(line[i])

        if len(patternRows):
            num += getPatternNote(patternRows) * 100
            num += getPatternNote(patternCols)
    print(num)

solve()

### PART 2 ###

def hasReflection(pattern, firstPtr, lastPtr):
    diff = 0
    while firstPtr < lastPtr and diff <= 1:
        for x, y in zip(pattern[firstPtr], pattern[lastPtr]):
            if x != y:
                diff += 1
        firstPtr += 1
        lastPtr -= 1
    return diff == 1

solve()
