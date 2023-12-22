import re

### PART 1 ###

bricks = []
with open('input.txt', 'r') as f:
    for line in f:
        nums = re.split('~|,', line.strip())
        bricks.append(((int(nums[0]), int(nums[1]), int(nums[2])), (int(nums[3]), int(nums[4]), int(nums[5]))))
bricks.sort(key=lambda brick: (brick[0][2], brick[1][2]))

class Brick:
    def __init__(self, id):
        self.id = id
        self.lowerBricks = set() # other bricks that are supporting this brick
        self.higherBricks = set() # other bricks that are supported by this brick

brickIdToObjs = {}
finalBricks = []
xyToz = {} # map the highest z position for the (x, y)-coordinate
xyEndzToId = {} # map the (x, y, end z)-coordinate to the brick ID
for id, brick in enumerate(bricks):
    brickIdToObjs[id] = Brick(id)
    start, end = brick
    startX, startY, startZ = start
    endX, endY, endZ = end
    actualStartZ = 0
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            actualStartZ = max(xyToz.get((x, y), 0) + 1, actualStartZ)
    actualEndZ = endZ - (startZ - actualStartZ)
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            xyToz[(x, y)] = actualEndZ
            xyEndzToId[(x, y, actualEndZ)] = id
    finalBricks.append(((startX, startY, actualStartZ), (endX, endY, actualEndZ)))

unsafeBricks = set()
for id, brick in enumerate(finalBricks):
    brickObj = brickIdToObjs[id]
    start, end = brick
    startX, startY, startZ = start
    endX, endY, endZ = end
    if startZ == 1:
        continue
    checkZ = startZ - 1
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if (x, y, checkZ) in xyEndzToId:
                lowerBrickObj = brickIdToObjs[xyEndzToId[(x, y, checkZ)]]
                brickObj.lowerBricks.add(lowerBrickObj)
                lowerBrickObj.higherBricks.add(brickObj)
    if len(brickObj.lowerBricks) == 1:
        unsafeBricks.add(list(brickObj.lowerBricks)[0])

print(len(finalBricks) - len(unsafeBricks))

### PART 2 ###

numFallen = 0
for unsafeBrick in list(unsafeBricks):
    fallenBricks = set()
    fallenBricks.add(unsafeBrick)
    currBricks = list(unsafeBrick.higherBricks)
    while len(currBricks):
        nextBricks = set()
        for currBrick in currBricks:
            isSupportedByNonFallenBrick = False
            for lowerBrick in list(currBrick.lowerBricks):
                if lowerBrick not in fallenBricks:
                    isSupportedByNonFallenBrick = True
                    break
            if not isSupportedByNonFallenBrick:
                fallenBricks.add(currBrick)
                nextBricks.update(list(currBrick.higherBricks))
        currBricks = list(nextBricks)
    numFallen += len(fallenBricks) - 1
print(numFallen)
