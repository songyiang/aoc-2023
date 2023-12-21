### PART 1 ###

map = []
startTile = None
with open('input.txt', 'r') as f:
    for r, line in enumerate(f):
        row = []
        for c, char in enumerate(line.strip()):
            if char == 'S':
                startTile = (r, c)
            row.append(char)
        map.append(row)
numRows = len(map)
numCols = len(map[0])

numSteps = 0
queue = [startTile]
visitedOddStepsTiles = set()
visitedEvenStepsTiles = set()
while numSteps != 64:
    numSteps += 1
    newQueue = []
    isOddStep = numSteps % 2
    for r, c in queue:
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newR, newC = r + dr, c + dc
            if newR >= 0 and newR < numRows and newC >= 0 and newC < numCols:
                # Check parity of current step as reachable tiles oscillate between odd and even step while spreading outwards with new reachable tiles
                if (isOddStep and (newR, newC) not in visitedOddStepsTiles) or (not isOddStep and (newR, newC) not in visitedEvenStepsTiles):
                    if map[newR][newC] != '#':
                        newQueue.append((newR, newC))
                        if isOddStep:
                            visitedOddStepsTiles.add((newR, newC))
                        else:
                            visitedEvenStepsTiles.add((newR, newC))
    queue = newQueue
print(len(visitedEvenStepsTiles))

### PART 2 ###

# Boundary of the finite map is made of garden plots.
# numRows == numCols == 131
# 26501365 == 131 * 202300 + 65
# Let N = 131.
# A quadratic seuquence is formed: f(65), f(N+65), f(2N+65), ...

def getNumReachable(numSteps):
    count = 0
    queue = [startTile]
    visitedOddStepsTiles = set()
    visitedEvenStepsTiles = set()
    while count != numSteps:
        count += 1
        newQueue = []
        isOddStep = count % 2
        for r, c in queue:
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newR, newC = r + dr, c + dc
                checkR, checkC = newR % numRows, newC % numCols # since map is repeated infinitely
                if (isOddStep and (newR, newC) not in visitedOddStepsTiles) or (not isOddStep and (newR, newC) not in visitedEvenStepsTiles):
                    if map[checkR][checkC] != '#':
                        newQueue.append((newR, newC))
                        if isOddStep:
                            visitedOddStepsTiles.add((newR, newC))
                        else:
                            visitedEvenStepsTiles.add((newR, newC))
        queue = newQueue
    return len(visitedOddStepsTiles) if numSteps % 2 else len(visitedEvenStepsTiles)

# Get quadratic equation from quadratic sequence
first = getNumReachable(65) # f(65)
second = getNumReachable(131 + 65) # f(N + 65)
third = getNumReachable(131 + 131 + 65) # f(2N + 65)
a = ((third - second) - (second - first)) // 2
b = (second - first) - 3 * a
c = first - a - b

# Find f(202300 * N + 65)
n = 202300 + 1
print(a * n * n + b * n + c)
