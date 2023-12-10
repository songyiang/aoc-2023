### PART 1 ###

maze = []
with open('input.txt', 'r') as f:
    for r, line in enumerate(f):
        row = []
        for c, char in enumerate(line[:-1]):
            if char == 'S':
                start = (r, c)
            row.append(char)
        maze.append(row)
    numRows, numCols = len(maze), len(maze[0])

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

def addPairs(a, b):
    return (a[0] + b[0], a[1] + b[1])

def canMove(next, direction):
    if direction == UP: # from DOWN
        return next == '|' or next == '7' or next == 'F'
    elif direction == RIGHT: # from LEFT
        return next == '-' or next == 'J' or next == '7'
    elif direction == DOWN: # from UP
        return next == '|' or next == 'L' or next == 'J'
    elif direction == LEFT: # from RIGHT
        return next == '-' or next == 'L' or next == 'F'
    else:
        return False

def getNeighbours(pos):
    directions = []
    curr = maze[pos[0]][pos[1]]
    if curr == '|':
        directions = [UP, DOWN]
    elif curr == '-':
        directions = [RIGHT, LEFT]
    elif curr == 'L':
        directions = [UP, RIGHT]
    elif curr == 'J':
        directions = [UP, LEFT]
    elif curr == '7':
        directions = [DOWN, LEFT]
    elif curr == 'F':
        directions = [RIGHT, DOWN]
    elif curr == 'S':
        directions = [UP, RIGHT, DOWN, LEFT]

    neighbours = []
    for direction in directions:
        r, c = addPairs(pos, direction)
        if r >= 0 and r < numRows and c >= 0 and c < numCols and canMove(maze[r][c], direction):
            neighbours.append((r, c))
    return neighbours

# BFS
isAtStart = True
curr = [start]
visited = set()
visited.add(start)
numSteps = 0
while isAtStart or len(curr) != 1:
    isAtStart = False
    nextCurr = []
    numSteps += 1
    for pos in curr:
        for neighbour in getNeighbours(pos):
            if neighbour not in visited:
                nextCurr.append(neighbour)
                visited.add(neighbour)
    curr = nextCurr
print(numSteps)

### PART 2 ###

def getNextPosMovement(pos):
    directions = []
    curr = maze[pos[0]][pos[1]]
    if curr == '|':
        directions = [UP, DOWN]
    elif curr == '-':
        directions = [RIGHT, LEFT]
    elif curr == 'L':
        directions = [UP, RIGHT]
    elif curr == 'J':
        directions = [UP, LEFT]
    elif curr == '7':
        directions = [DOWN, LEFT]
    elif curr == 'F':
        directions = [RIGHT, DOWN]
    elif curr == 'S':
        directions = [UP, RIGHT, DOWN, LEFT]

    for direction in directions:
        r, c = addPairs(pos, direction)
        if r >= 0 and r < numRows and c >= 0 and c < numCols and canMove(maze[r][c], direction):
            if (r, c) not in traced: # prevent dfs from non-termination
                return (r, c), direction

def getDirectionStr(direction):
    if direction == UP:
        return 'U'
    elif direction == RIGHT:
        return 'R'
    elif direction == DOWN:
        return 'D'
    elif direction == LEFT:
        return 'L'

# DFS
curr = start
traced = set()
traced.add(start)
directionalMaze = [[' ' for _ in range(numCols)] for _ in range(numRows)]
while True:
    next = getNextPosMovement(curr)
    if next is None: # reached starting position
        break
    nextPos, direction = next
    traced.add(nextPos)
    directionalMaze[curr[0]][curr[1]] = getDirectionStr(direction)
    curr = nextPos

# Ray casting algorithm
insidePoints = set()
for r in range(numRows):
    isInside = False
    prev = None
    consecutivePoints = []
    for c in range(numCols):
        if (r, c) in traced:
            consecutivePoints = []
            curr = directionalMaze[r][c]
            if curr == 'U' or curr == 'D':
                isInside = prev == None or prev == curr
                prev = curr
        elif isInside:
            insidePoints.add((r, c))
            consecutivePoints.append((r, c))
    if isInside:
        for point in consecutivePoints:
            insidePoints.remove(point)
print(len(insidePoints))

# Visualise directional maze
for point in insidePoints:
    directionalMaze[point[0]][point[1]] = 'X'
for row in directionalMaze:
    print(row)
