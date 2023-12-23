import sys

### PART 1 ###

map = []
with open('input.txt', 'r') as f:
    for line in f:
        map.append([char for char in line.strip()])
numRows = len(map)
numCols = len(map[0])
sys.setrecursionlimit(numRows * numCols)

for c, tile in enumerate(map[0]):
    if tile == '.':
        start = (0, c)
for c, tile in enumerate(map[-1]):
    if tile == '.':
        end = (len(map) - 1, c)

d = {
    '^': [(-1, 0)],
    '>': [(0, 1)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '.': [(-1, 0), (0, 1), (1, 0), (0, -1)]
}

def getNeighbours(pos):
    neighbours = []
    r, c = pos
    for dr, dc in d[map[r][c]]:
        newR, newC = r + dr, c + dc
        if 0 <= newR < numRows and 0 <= newC < numCols and map[newR][newC] != '#':
            neighbours.append((newR, newC))
    return neighbours

def dfs(curr, tilesAlongPath):
    global pathLength
    if curr == end:
        pathLength = max(len(tilesAlongPath), pathLength)
    for r, c in getNeighbours(curr):
        if (r, c) not in tilesAlongPath:
            tilesAlongPath.append((r, c))
            dfs((r, c), tilesAlongPath)
            tilesAlongPath.pop()

pathLength = 0
dfs(start, [start])
print(pathLength - 1) # exclude start

### PART 2 ###

def getNeighbours(pos):
    neighbours = []
    r, c = pos
    for dr, dc in d['.']:
        newR, newC = r + dr, c + dc
        if 0 <= newR < numRows and 0 <= newC < numCols and map[newR][newC] != '#':
            neighbours.append((newR, newC))
    return neighbours

# Find intersections
intersections = set()
intersections.add(start)
for r in range(numRows):
    for c in range(numCols):
        if map[r][c] != '#' and len(getNeighbours((r, c))) > 2:
            intersections.add((r, c))
intersections.add(end)

# Find lengths between each pair of intersections
intersectionLengths = {}
for intersection in list(intersections):
    visited = set()
    visited.add(intersection)
    queue = [intersection]
    length = 0
    while len(queue):
        newQueue = []
        length += 1
        for pos in queue:
            for neighbourPos in getNeighbours(pos):
                if neighbourPos not in visited:
                    if neighbourPos in intersections:
                        l = intersectionLengths.get(intersection, [])
                        l.append((neighbourPos, length))
                        intersectionLengths[intersection] = l
                    else:
                        newQueue.append(neighbourPos)
                    visited.add(neighbourPos)
        queue = newQueue

def dfs(curr, tilesAlongPath, length):
    global pathLength
    if curr == end:
        pathLength = max(length, pathLength)
    for pos, intersectionLength in intersectionLengths[curr]:
        r, c = pos
        if (r, c) not in tilesAlongPath:
            tilesAlongPath.append((r, c))
            dfs((r, c), tilesAlongPath, length + intersectionLength)
            tilesAlongPath.pop()

pathLength = 0
dfs(start, [start], 0)
print(pathLength)
