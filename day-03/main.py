import re

### PART 1 ###

def getNeighbouringPositions(pos):
    row, col = pos
    return [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1)
    ]

posToNum = {}
posToSetOfPositions = {}
symbolPositions = []

with open('input.txt', 'r') as f:
    rowNum = 0
    for line in f:
        rowStr = re.split('\n', line)[0]
        num = 0
        positions = []
        for i in range(len(rowStr)):
            char = rowStr[i]
            try:
                digit = int(char)
                num = num * 10 + digit
                positions.append((rowNum, i))
            except:
                # Non-number reached
                setOfPositions = set(positions)
                for pos in positions:
                    posToNum[pos] = num
                    posToSetOfPositions[pos] = setOfPositions

                # Non-period reached
                if char != '.':
                    symbolPositions.append((rowNum, i))

                num = 0
                positions = []

        # Edge case where number is at the end of the row
        if len(positions):
            for pos in positions:
                posToNum[pos] = num
                posToSetOfPositions[pos] = setOfPositions

        rowNum += 1

sum = 0
for pos in symbolPositions:
    for checkPos in getNeighbouringPositions(pos):
        if checkPos in posToNum:
            sum += posToNum.pop(checkPos)
            removePositions = list(posToSetOfPositions.get(checkPos, set()))
            for removePos in removePositions:
                posToNum.pop(removePos, None)
print(sum)

### PART 2 ###

posToNum = {}
posToSetOfPositions = {}
starPositions = []

with open('input.txt', 'r') as f:
    rowNum = 0
    for line in f:
        rowStr = re.split('\n', line)[0]
        num = 0
        positions = []
        for i in range(len(rowStr)):
            char = rowStr[i]
            try:
                digit = int(char)
                num = num * 10 + digit
                positions.append((rowNum, i))
            except:
                # Non-number reached
                setOfPositions = set(positions)
                for pos in positions:
                    posToNum[pos] = num
                    posToSetOfPositions[pos] = setOfPositions

                # Star reached
                if char == '*':
                    starPositions.append((rowNum, i))

                num = 0
                positions = []

        # Edge case where number is at the end of the row
        if len(positions):
            for pos in positions:
                posToNum[pos] = num
                posToSetOfPositions[pos] = setOfPositions

        rowNum += 1

sum = 0
for pos in starPositions:
    nums = []
    for checkPos in getNeighbouringPositions(pos):
        if checkPos in posToNum:
            nums.append(posToNum.pop(checkPos))
            removePositions = list(posToSetOfPositions.get(checkPos, set()))
            for removePos in removePositions:
                posToNum.pop(removePos, None)

    if len(nums) == 2:
        sum += nums[0] * nums[1]
print(sum)
