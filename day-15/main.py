import re

### PART 1 ###

def get_val(text):
    val = 0
    for char in text:
        val += ord(char)
        val *= 17
        val %= 256
    return val

res = 0
with open('input.txt', 'r') as f:
    sequence = re.split(',', f.readline().strip())
    for step in sequence:
        res += get_val(step)
print(res)

### PART 2 ###

class LensPtr:
    def __init__(self, label, focalLength):
        self.label = label
        self.focalLength = focalLength
        self.nextLensPtr = None

    def assignNextPtr(self, nextLensPtr):
        self.nextLensPtr = nextLensPtr

    def removeNextPtr(self):
        if self.nextLensPtr is not None:
            self.nextLensPtr = self.nextLensPtr.nextLensPtr

with open('input.txt', 'r') as f:
    sequence = re.split(',', f.readline().strip())
    mapBoxNumToFirstLensPtr = {}

    for step in sequence:
        if '-' in step:
            label = re.split('-', step)[0]
            boxNum = get_val(label)

            if boxNum in mapBoxNumToFirstLensPtr:
                currLensPtr = mapBoxNumToFirstLensPtr[boxNum]
                if currLensPtr.label == label:
                    # Remove first lens pointer
                    nextLensPtr = currLensPtr.nextLensPtr
                    if nextLensPtr is None:
                        # Box has only one lens
                        mapBoxNumToFirstLensPtr.pop(boxNum)
                    else:
                        # Assign next lens pointer as the new first lens pointer
                        mapBoxNumToFirstLensPtr[boxNum] = nextLensPtr
                else:
                    while currLensPtr.nextLensPtr is not None:
                        if currLensPtr.nextLensPtr.label == label:
                            break
                        currLensPtr = currLensPtr.nextLensPtr
                    currLensPtr.removeNextPtr()
        elif '=' in step:
            text = re.split('=', step)
            label = text[0]
            boxNum = get_val(label)
            focalLength = int(text[1])

            if boxNum in mapBoxNumToFirstLensPtr:
                currLensPtr = mapBoxNumToFirstLensPtr[boxNum]
                prevLensPtr = None
                hasAdded = False
                while currLensPtr is not None:
                    if currLensPtr.label == label:
                        currLensPtr.focalLength = focalLength
                        hasAdded = True
                        break
                    prevLensPtr = currLensPtr
                    currLensPtr = currLensPtr.nextLensPtr
                if not hasAdded:
                    prevLensPtr.assignNextPtr(LensPtr(label, focalLength))
            else:
                mapBoxNumToFirstLensPtr[boxNum] = LensPtr(label, focalLength)

    focusingPower = 0
    for boxNum, currLensPtr in mapBoxNumToFirstLensPtr.items():
        currSlotNum = 1
        while currLensPtr is not None:
            focusingPower += (boxNum + 1) * currSlotNum * currLensPtr.focalLength
            currLensPtr = currLensPtr.nextLensPtr
            currSlotNum += 1
    print(focusingPower)
