import math
import re

### PART 1 ###

graph = {}

with open('input.txt', 'r') as f:
    instructions = f.readline().rstrip()

    f.readline()
    for line in f:
        l = re.split(' = |\(|, |\)\n', line)
        origin = l[0]
        left, right = l[2], l[3]
        graph[origin] = (left, right)

    curr = 'AAA'
    currPtr = 0
    numSteps = 0
    while True:
        numSteps += 1
        if instructions[currPtr] == 'L':
            curr = graph[curr][0]
        else:
            curr = graph[curr][1]

        if curr == 'ZZZ':
            break

        currPtr += 1
        if currPtr == len(instructions):
            currPtr = 0
    print(numSteps)

### PART 2 ###

graph = {}

with open('input.txt', 'r') as f:
    instructions = f.readline().rstrip()

    f.readline()

    origins = []
    for line in f:
        l = re.split(' = |\(|, |\)\n', line)
        origin = l[0]
        if origin.endswith('A'):
            origins.append(origin)
        left, right = l[2], l[3]
        graph[origin] = (left, right)

    numStepsList = []
    for curr in origins:
        currPtr = 0
        numSteps = 0
        visited = {}
        while True:
            numSteps += 1
            if instructions[currPtr] == 'L':
                curr = graph[curr][0]
            else:
                curr = graph[curr][1]

            if curr.endswith('Z'):
                numStepsList.append(numSteps)
                break

            currPtr += 1
            if currPtr == len(instructions):
                currPtr = 0

    lcm = math.lcm(*numStepsList)
    print(lcm)
