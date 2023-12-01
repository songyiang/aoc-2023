### PART 1 ###

def getNumber(line):
    firstPtr, lastPtr = 0, len(line)
    firstDigit, lastDigit = 0, 0

    # Get first digit
    while True:
        try:
            firstDigit = int(line[firstPtr])
        except:
            firstPtr += 1
            continue
        break

    # Get last digit
    while True:
        try:
            lastDigit = int(line[lastPtr])
        except:
            lastPtr -= 1
            continue
        break

    # Combine digits
    return firstDigit * 10 + lastDigit

sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        sum += getNumber(line)
print(sum)

### PART 2 ###

validDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
validSpellings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Create a trie
END_KEY = '_END'
root = dict()
for digit, spelling in zip(validDigits, validSpellings):
    currPtr = root
    for letter in spelling:
        currPtr = currPtr.setdefault(letter, {})
    currPtr[END_KEY] = digit

# Convert any valid spelling in text to valid digit
def convert(text):
    newText = []
    validPtrs = []
    for letter in text:
        nextPtrs = []
        nextChar = None
        if letter in root:
            nextPtrs.append(root[letter])
        for ptr in validPtrs:
            if letter in ptr:
                nextPtr =  ptr[letter]
                if END_KEY in nextPtr: # valid spelling found
                    nextChar = nextPtr[END_KEY] # get the digit corresponding to the spelling
                    break
                else:
                    nextPtrs.append(nextPtr)
        validPtrs = nextPtrs
        newText.append(letter if nextChar is None else nextChar)
    return ''.join(newText)

sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        newLine = convert(line)
        sum += getNumber(newLine)
print(sum)
