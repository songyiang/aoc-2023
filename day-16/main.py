### PART 1 ###

def getEnergizedTiles(startR, startC):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    mapForwardSlash = {
        UP: RIGHT,
        DOWN: LEFT,
        LEFT: DOWN,
        RIGHT: UP
    }
    mapBackwardSlash = {
        UP: LEFT,
        DOWN: RIGHT,
        LEFT: UP,
        RIGHT: DOWN
    }

    energizedTiles = set()
    visited = set()
    curr = []

    startTile = (startR, startC)
    if startR == 0:
        curr.append((startTile, DOWN))
    elif startR == numRows - 1:
        curr.append((startTile, UP))
    if startC == 0:
        curr.append((startTile, RIGHT))
    elif startC == numCols - 1:
        curr.append((startTile, LEFT))


    def add(tileWithDirection):
        if tileWithDirection not in visited:
            next.append(tileWithDirection)
            visited.add(tileWithDirection)

    isStart = True
    while len(curr):
        next = []
        for tile, direction in curr:
            r = tile[0] + direction[0] if not isStart else tile[0]
            c = tile[1] + direction[1] if not isStart else tile[1]
            newTile = (r, c)
            new = (newTile, direction)

            if r < 0 or r == numRows or c < 0 or c == numCols:
                continue

            energizedTiles.add(newTile)
            if contraption[r][c] == '/':
                add((newTile, mapForwardSlash[direction]))
            elif contraption[r][c] == '\\':
                add((newTile, mapBackwardSlash[direction]))
            elif contraption[r][c] == '|':
                if direction == LEFT or direction == RIGHT:
                    add((newTile, UP))
                    add((newTile, DOWN))
                else:
                    add(new)
            elif contraption[r][c] == '-':
                if direction == UP or direction == DOWN:
                    add((newTile, LEFT))
                    add((newTile, RIGHT))
                else:
                    add(new)
            else:
                add(new)
        isStart = False
        curr = next

    return energizedTiles

with open('input.txt', 'r') as f:
    contraption = []
    for line in f:
        contraption.append([char for char in line.strip()])
    numRows = len(contraption)
    numCols = len(contraption[0])

print(len(getEnergizedTiles(0, 0)))

### PART 2 ###

maxNumEnergized = 0
for r in range(numRows):
    maxNumEnergized = max(len(getEnergizedTiles(r, 0)), maxNumEnergized)
    maxNumEnergized = max(len(getEnergizedTiles(r, numCols - 1)), maxNumEnergized)
for c in range(numCols):
    maxNumEnergized = max(len(getEnergizedTiles(0, c)), maxNumEnergized)
    maxNumEnergized = max(len(getEnergizedTiles(numRows - 1, c)), maxNumEnergized)
print(maxNumEnergized)
