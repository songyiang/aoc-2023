import re

### PART 1 ###

def getNumsFromText(text):
    return [int(i) for i in re.split('\D+', text) if i != '']

def getCardInfo(line):
    split = re.split(': | \| |\n', line)
    winningText, myText = split[1], split[2]
    winningNums, myNums = set(getNumsFromText(winningText)), getNumsFromText(myText)
    return winningNums, myNums

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        cardInfo = getCardInfo(line)
        winningNums, myNums = cardInfo[0], cardInfo[1]
        numMatches = 0
        for myNum in myNums:
            if myNum in winningNums:
                numMatches += 1
        points = pow(2, numMatches - 1) if numMatches > 0 else 0
        total += points
print(total)

### PART 2 ###

numCardInstancesList = [] # each index is the number of instances of corresponding card
ptr = 0
with open('input.txt', 'r') as f:
    for line in f:
        # Add original card instance of current card
        try:
            numCardInstancesList[ptr] += 1
        except:
            numCardInstancesList.append(1)

        numCurrCardInstances = numCardInstancesList[ptr]

        cardInfo = getCardInfo(line)
        winningNums, myNums =  cardInfo[0], cardInfo[1]

        numMatches = 0
        for myNum in myNums:
            if myNum in winningNums:
                numMatches += 1

        for i in range(1, numMatches + 1):
            try:
                numCardInstancesList[ptr + i] += numCurrCardInstances
            except:
                numCardInstancesList.append(numCurrCardInstances)

        ptr += 1
print(sum(numCardInstancesList))
