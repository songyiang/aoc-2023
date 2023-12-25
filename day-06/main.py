import re

### PART 1 ###

with open('input.txt', 'r') as f:
    times = [int(i) for i in re.split('\D+', re.split('Time:|\n', f.readline())[1]) if i]
    distances = [int(i) for i in re.split('\D+', re.split('Distance:|\n', f.readline())[1]) if i]

    numWaysList = []
    for time, distance in zip(times, distances):
        numWays = 0
        for i in range(1, time + 1):
            if i * (time - i) > distance:
                numWays += 1
        numWaysList.append(numWays)

    total = 1
    for numWays in numWaysList:
        total *= numWays
    print(total)

### PART 2 ###

with open('input.txt', 'r') as f:
    time = int(''.join(re.split('\D+', re.split('Time:|\n', f.readline())[1])))
    distance = int(''.join(re.split('\D+', re.split('Distance:|\n', f.readline())[1])))

    # Get first occurrence of beating the record
    start = 1
    end = time
    while start != end:
        mid = start + (end - start) // 2
        checkDistance = mid * (time - mid)
        if checkDistance <= distance:
            start = mid + 1
        else:
            end = mid
    first = start

    # Get last occurrence of beating the record
    start = 1
    end = time
    while start != end:
        mid = start + (end - start) // 2
        checkDistance = mid * (time - mid)
        if checkDistance > distance:
            start = mid + 1
        else:
            end = mid
    last = start - 1

    print(last - first + 1)
