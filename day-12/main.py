import re
from functools import lru_cache

### PART 1 ###

@lru_cache(maxsize=None)
def getNumArrangements(conditionPtr, damGroups, nextMustBeOp, nextMustBeDam):
    damGroupsList = [int(i) for i in re.split(',', damGroups) if i]

    if conditionPtr == len(conditions):
        return 1 if len(damGroupsList) == 0 else 0

    if len(damGroupsList) == 0:
        return 0 if '#' in conditions[conditionPtr:] else 1

    if conditions[conditionPtr] == '.':
        if nextMustBeDam:
            return 0
        return getNumArrangements(conditionPtr + 1, damGroups, False, False)
    elif conditions[conditionPtr] == '#':
        if nextMustBeOp:
            return 0
        if damGroupsList[0] == 1:
            newDamGroups = ','.join(str(i) for i in damGroupsList[1:])
            return getNumArrangements(conditionPtr + 1, newDamGroups, True, False)
        else:
            damGroupsList[0] -= 1
            newDamGroups = ','.join(str(i) for i in damGroupsList)
            return getNumArrangements(conditionPtr + 1, newDamGroups, False, True)
    else:
        numArrangementsIfDam = 0
        numArrangementsIfOp = 0
        if not nextMustBeOp:
            conditions[conditionPtr] = '#'
            numArrangementsIfDam = getNumArrangements(conditionPtr, damGroups, False, True)
        if not nextMustBeDam:
            conditions[conditionPtr] = '.'
            numArrangementsIfOp = getNumArrangements(conditionPtr + 1, damGroups, False, False)
        conditions[conditionPtr] = '?'
        return numArrangementsIfDam + numArrangementsIfOp

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        l = re.split(' |\n', line.strip())
        conditions = [char for char in l[0]]
        damGroups = l[1]
        num = getNumArrangements(0, damGroups, False, False)
        getNumArrangements.cache_clear()
        count += num
print(count)

### PART 2 ###

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        l = re.split(' |\n', line.strip())
        conditions = [char for char in '?'.join(l[0] for _ in range(5))]
        damGroups = ','.join(l[1] for _ in range(5))
        num = getNumArrangements(0, damGroups, False, False)
        getNumArrangements.cache_clear()
        count += num
print(count)
