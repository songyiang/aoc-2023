### PART 1 ###

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

LEFT = {
    NORTH: WEST,
    EAST: NORTH,
    SOUTH: EAST,
    WEST: SOUTH
}
RIGHT = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

class BlockNode:
    def __init__(self, x, y, directionFrom):
        self.x = x
        self.y = y
        self.directionFrom = directionFrom

class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def createPath(self, fromNode, toNode, pathCost):
        if fromNode in self.adjacencyList:
            self.adjacencyList[fromNode].append((toNode, pathCost))
        else:
            self.adjacencyList[fromNode] = [(toNode, pathCost)]

    def getNeighbours(self, node):
        return self.adjacencyList.get(node, [])

class BlockQueue:
    def __init__(self):
        self.queue = []

    def add(self, node):
        self.queue.append(node)

    def get(self):
        self.queue.sort(key=lambda node: nodeToCost[node], reverse=True)
        return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

    def has(self, node):
        return node in self.queue

def getNodeObj(x, y, directionFrom):
    if (x, y, directionFrom) in nodeObjs:
        return nodeObjs[(x, y, directionFrom)]

    node = BlockNode(x, y, directionFrom)
    nodeObjs[(x, y, directionFrom)] = node
    return node

def assignNeighbours(r, c):
    for directionFrom in [NORTH, EAST, SOUTH, WEST]:
        fromNode = getNodeObj(r, c, directionFrom)
        for newDirectionFrom in [LEFT[directionFrom], RIGHT[directionFrom]]:
            x, y = r, c
            pathCost = 0
            for _ in range(3):
                x += newDirectionFrom[0]
                y += newDirectionFrom[1]
                if x < 0 or x >= numRows or y < 0 or y >= numCols:
                    break

                toNode = getNodeObj(x, y, newDirectionFrom)
                pathCost += map[x][y]
                graph.createPath(fromNode, toNode, pathCost)

with open('input.txt', 'r') as f:
    map = []
    for line in f:
        map.append([int(char) for char in line.strip()])
    numRows = len(map)
    numCols = len(map[0])

# Construct graph
nodeObjs = {}
startFromNorthNode = getNodeObj(0, 0, NORTH)
startFromEastNode = getNodeObj(0, 0, EAST)
startFromSouthNode = getNodeObj(0, 0, SOUTH)
startFromWestNode = getNodeObj(0, 0, WEST)
startNodes = [startFromNorthNode, startFromEastNode, startFromSouthNode, startFromWestNode]
graph = Graph()
for r in range(numRows):
    for c in range(numCols):
        assignNeighbours(r, c)

# Uniform cost search
minHeatLoss = sum([sum(row) for row in map])
for startNode in startNodes:
    visited = set()
    nodeToCost = {}
    nodeToCost[startNode] = 0
    frontier = BlockQueue()
    frontier.add(startNode)
    while not frontier.isEmpty():
        node = frontier.get()
        currCost = nodeToCost[node]
        visited.add(node)

        if node.x == numRows - 1 and node.y == numCols - 1:
            minHeatLoss = min(currCost, minHeatLoss)
            break

        for neighbour, pathCost in graph.getNeighbours(node):
            if neighbour in visited:
                continue

            if frontier.has(neighbour):
                nodeToCost[neighbour] = min(currCost + pathCost, nodeToCost[neighbour])
            else:
                nodeToCost[neighbour] = currCost + pathCost
                frontier.add(neighbour)
print(minHeatLoss)

### PART 2 ###

def assignNeighbours(r, c):
    for directionFrom in [NORTH, EAST, SOUTH, WEST]:
        fromNode = getNodeObj(r, c, directionFrom)
        for newDirectionFrom in [LEFT[directionFrom], RIGHT[directionFrom]]:
            x, y = r, c
            pathCost = 0
            for i in range(10):
                x += newDirectionFrom[0]
                y += newDirectionFrom[1]
                if x < 0 or x >= numRows or y < 0 or y >= numCols:
                    break

                pathCost += map[x][y]
                if i >= 3:
                    toNode = getNodeObj(x, y, newDirectionFrom)
                    graph.createPath(fromNode, toNode, pathCost)

# Construct graph
nodeObjs = {}
startFromNorthNode = getNodeObj(0, 0, NORTH)
startFromEastNode = getNodeObj(0, 0, EAST)
startFromSouthNode = getNodeObj(0, 0, SOUTH)
startFromWestNode = getNodeObj(0, 0, WEST)
startNodes = [startFromNorthNode, startFromEastNode, startFromSouthNode, startFromWestNode]
graph = Graph()
for r in range(numRows):
    for c in range(numCols):
        assignNeighbours(r, c)

# Uniform cost search
minHeatLoss = sum([sum(row) for row in map])
for startNode in startNodes:
    visited = set()
    nodeToCost = {}
    nodeToCost[startNode] = 0
    frontier = BlockQueue()
    frontier.add(startNode)
    while not frontier.isEmpty():
        node = frontier.get()
        currCost = nodeToCost[node]
        visited.add(node)

        if node.x == numRows - 1 and node.y == numCols - 1:
            minHeatLoss = min(currCost, minHeatLoss)
            break

        for neighbour, pathCost in graph.getNeighbours(node):
            if neighbour in visited:
                continue

            if frontier.has(neighbour):
                nodeToCost[neighbour] = min(currCost + pathCost, nodeToCost[neighbour])
            else:
                nodeToCost[neighbour] = currCost + pathCost
                frontier.add(neighbour)
print(minHeatLoss)
