### PART 1 ###

with open('input.txt', 'r') as f:
    maze = []
    for r, line in enumerate(f):
        row = []
        for c, char in enumerate(line[:-1]):
            if char == 'S':
                startPoint = (r, c)
            row.append(char)
        maze.append(row)
    numRows, numCols = len(maze), len(maze[0])

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

foundLoop = False
for startDirection in [UP, RIGHT, DOWN, LEFT]:
    loop = [(startPoint, startDirection)]
    currPoint = startPoint
    currDirection = startDirection
    while True:
        r, c = currPoint[0] + currDirection[0], currPoint[1] + currDirection[1]
        if r < 0 or r == numRows or c < 0 or c == numCols:
            break

        nextDirection = None
        if maze[r][c] == '|':
            if currDirection == UP:
                nextDirection = UP
            elif currDirection == DOWN:
                nextDirection = DOWN
        elif maze[r][c] == '-':
            if currDirection == RIGHT:
                nextDirection = RIGHT
            elif currDirection == LEFT:
                nextDirection = LEFT
        elif maze[r][c] == 'L':
            if currDirection == DOWN:
                nextDirection = RIGHT
            elif currDirection == LEFT:
                nextDirection = UP
        elif maze[r][c] == 'J':
            if currDirection == RIGHT:
                nextDirection = UP
            elif currDirection == DOWN:
                nextDirection = LEFT
        elif maze[r][c] == '7':
            if currDirection == UP:
                nextDirection = LEFT
            elif currDirection == RIGHT:
                nextDirection = DOWN
        elif maze[r][c] == 'F':
            if currDirection == UP:
                nextDirection = RIGHT
            elif currDirection == LEFT:
                nextDirection = DOWN
        elif maze[r][c] == 'S':
            foundLoop = True
            break
        if nextDirection is None:
            break

        currPoint = (r, c)
        currDirection = nextDirection
        loop.append((currPoint, currDirection))
    if foundLoop:
        break

print(len(loop) // 2)

### PART 2 ###

# Get vertices in loop
vertices = []
currDirection = None
for point, direction in loop:
    if direction != currDirection:
        vertices.append(point)
        currDirection = direction

# Shoelace formula
det = 0
numVertices = len(vertices)
vertices.append(vertices[0])
for i in range(numVertices):
    x1, y1 = vertices[i]
    x2, y2 = vertices[i + 1]
    det += x1 * y2 - y1 * x2
print(abs(det) // 2 - len(loop) // 2 + 1)
