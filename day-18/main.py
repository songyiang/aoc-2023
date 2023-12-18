import re

### PART 1 ###

def getPointsAndPerimeter():
    with open('input.txt', 'r') as f:
        minX, minY = 0, 0
        currPoint = (0, 0)
        points = [currPoint]
        perimeter = 0
        for line in f:
            directionStr, numMetres, _ = re.split(' ', line.strip())
            numMetres = int(numMetres)
            perimeter += numMetres
            if directionStr == 'U':
                nextPoint = (currPoint[0], currPoint[1] + numMetres)
            elif directionStr == 'D':
                nextPoint = (currPoint[0], currPoint[1] - numMetres)
            elif directionStr == 'L':
                nextPoint = (currPoint[0] - numMetres, currPoint[1])
            elif directionStr == 'R':
                nextPoint = (currPoint[0] + numMetres, currPoint[1])
            points.append(nextPoint)
            minX = min(nextPoint[0], minX)
            minY = min(nextPoint[1], minY)
            currPoint = nextPoint

        # Adjust for negative coordinates
        if minX < 0 or minY < 0:
            dx, dy = abs(minX), abs(minY)
            for i, point in enumerate(points):
                x, y = point
                points[i] = (x + dx, y + dy)

        return points, perimeter

def pick_theorem(points, perimeter):
    # Shoelace formula
    det = 0
    numPoints = len(points)
    points.append(points[0])
    for i in range(numPoints):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        det += x1 * y2 - y1 * x2

    # Pick's theorem
    return abs(det) // 2 + perimeter // 2 + 1

points, perimeter = getPointsAndPerimeter()
area = pick_theorem(points, perimeter)
print(area)

### PART 2 ###

def getPointsAndPerimeter():
    with open('input.txt', 'r') as f:
        minX, minY = 0, 0
        currPoint = (0, 0)
        points = [currPoint]
        perimeter = 0
        for line in f:
            instruction = re.split(' ', line.strip())[2][2:-1]
            numMetres = int(instruction[:-1], 16)
            perimeter += numMetres
            directionStr = instruction[-1]
            if directionStr == '0':
                nextPoint = (currPoint[0] + numMetres, currPoint[1])
            elif directionStr == '1':
                nextPoint = (currPoint[0], currPoint[1] - numMetres)
            elif directionStr == '2':
                nextPoint = (currPoint[0] - numMetres, currPoint[1])
            elif directionStr == '3':
                nextPoint = (currPoint[0], currPoint[1] + numMetres)
            points.append(nextPoint)
            minX = min(nextPoint[0], minX)
            minY = min(nextPoint[1], minY)
            currPoint = nextPoint

        # Adjust for negative coordinates
        if minX < 0 or minY < 0:
            dx, dy = abs(minX), abs(minY)
            for i, point in enumerate(points):
                x, y = point
                points[i] = (x + dx, y + dy)

        return points, perimeter

points, perimeter = getPointsAndPerimeter()
area = pick_theorem(points, perimeter)
print(area)
