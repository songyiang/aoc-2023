### PART 1 ###

with open('input.txt', 'r') as f:
    maze = []
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

foundLoop = False
for startDirection in [UP, RIGHT, DOWN, LEFT]:
    loop = [(start, startDirection)]
    curr = start
    currDirection = startDirection
    while True:
        r, c = curr[0] + currDirection[0], curr[1] + currDirection[1]
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

        curr = (r, c)
        currDirection = nextDirection
        loop.append((curr, currDirection))
    if foundLoop:
        break

print(len(loop) // 2)
