import re

### PART 1 ###

def extrapolate(nums):
    if all(i == 0 for i in nums):
        return 0
    newNums = []
    prevNum = nums[0]
    for i in range(1, len(nums)):
        newNums.append(nums[i] - prevNum)
        prevNum = nums[i]
    return nums[-1] + extrapolate(newNums)

sumValues = 0
with open('input.txt', 'r') as f:
    for line in f:
        nums = [int(i) for i in re.split('\s+', line) if i]
        sumValues += extrapolate(nums)
print(sumValues)

### PART 2 ###

sumValues = 0
with open('input.txt', 'r') as f:
    for line in f:
        nums = [int(i) for i in re.split('\s+', line) if i]
        sumValues += extrapolate(list(reversed(nums)))
print(sumValues)
