### PART 1 ###

img = []
with open('input.txt', 'r') as f:
    for line in f:
        row = []
        for char in line[:-1]:
            row.append(char)
        img.append(row)

numRows = len(img)
numCols = len(img[0])

def solve(additionalDist):
    galaxies = []

    # Row/Column with no galaxy: additionalDist
    # Row/Column with galaxy: 0
    rowGalaxyStatus = [additionalDist for _ in range(numRows)]
    columnGalaxyStatus = [additionalDist for _ in range(numCols)]
    for r in range(numRows):
        for c in range(numCols):
            if img[r][c] == '#':
                galaxies.append((r, c))
                rowGalaxyStatus[r] = 0
                columnGalaxyStatus[c] = 0

    rowsTravelledToAddDist = {}
    columnsTravelledToAddDist = {}
    for i in range(numRows):
        for j in range(i, numRows):
            rowsTravelledToAddDist[(i, j)] = sum(rowGalaxyStatus[i:j + 1]) if i != j else 0
    for i in range(numCols):
        for j in range(i, numCols):
            columnsTravelledToAddDist[(i, j)] = sum(columnGalaxyStatus[i:j + 1]) if i != j else 0

    sumLengths = 0
    for i in range(len(galaxies)):
        firstR, firstC = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            secondR, secondC = galaxies[j]
            sumLengths += abs(secondR - firstR) + abs(secondC - firstC)
            rowTravelled = (min(firstR, secondR), max(firstR, secondR))
            columnTravelled = (min(firstC, secondC), max(firstC, secondC))
            sumLengths += rowsTravelledToAddDist[rowTravelled]
            sumLengths += columnsTravelledToAddDist[columnTravelled]
    print(sumLengths)

solve(1)

### PART 2 ###

solve(999999)
