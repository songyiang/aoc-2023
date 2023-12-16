import re

### PART 1 ###

def tiltHorizontally(dy):
    assert dy == -1 or dy == 1

    if dy == -1:
        platform.reverse()

    numRows = len(platform)
    numCols = len(platform[0])
    for c in range(numCols):
        nextAvailableR = 0
        for r in range(numRows):
            if platform[r][c] == 'O':
                platform[r][c] = '.'
                platform[nextAvailableR][c] = 'O'
                nextAvailableR += 1
            elif platform[r][c] == '#':
                nextAvailableR = r + 1

    if dy == -1:
        platform.reverse()

    return platform

def calculateLoadOnNorth():
    totalLoad = 0
    currLoad = len(platform)
    for row in platform:
        for value in row:
            if value == 'O':
                totalLoad += currLoad
        currLoad -= 1
    return totalLoad

with open('input.txt', 'r') as f:
    platform = []
    for line in f:
        platform.append([char for char in line.strip()])

    tiltHorizontally(1)
    print(calculateLoadOnNorth())

### PART 2 ###

def tiltVertically(dx):
    assert dx == -1 or dx == 1

    for row in platform:
        if dx == 1:
            row.reverse()

        nextAvailableC = 0
        for c, value in enumerate(row):
            if value == 'O':
                row[c] = '.'
                row[nextAvailableC] = 'O'
                nextAvailableC += 1
            elif value == '#':
                nextAvailableC = c + 1

        if dx == 1:
            row = row.reverse()

    return platform

def spin():
    tiltHorizontally(1)
    tiltVertically(-1)
    tiltHorizontally(-1)
    tiltVertically(1)

with open('input.txt', 'r') as f:
    platform = []
    for line in f:
        platform.append([char for char in line.strip()])

    mapPlatformStrToSpinNum = {}
    mapSpinNumToPlatformStr = {}
    for currSpinNum in range(1, 1000000000 + 1):
        spin()
        platformStr = ','.join([''.join(row) for row in platform])
        if platformStr in mapPlatformStrToSpinNum:
            firstSpinNum = mapPlatformStrToSpinNum[platformStr]
            sameSpinNum = firstSpinNum + (1000000000 - firstSpinNum) % (currSpinNum - firstSpinNum)
            samePlatformStr = mapSpinNumToPlatformStr[sameSpinNum]
            platform = [[char for char in row] for row in re.split(',', samePlatformStr)]
            break
        else:
            mapPlatformStrToSpinNum[platformStr] = currSpinNum
            mapSpinNumToPlatformStr[currSpinNum] = platformStr

    print(calculateLoadOnNorth())