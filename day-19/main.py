import re

### PART 1 ###

acceptedSum = 0
with open('input.txt', 'r') as f:
    workflows = {}
    parts = []
    hasReachedParts = False
    for line in f:
        line = line.strip()
        if line == '':
            hasReachedParts = True
            continue

        if not hasReachedParts:
            l = re.split('{|}', line)
            name = l[0]
            stepStrs = re.split(',', l[1])
            steps = []
            for stepStr in stepStrs:
                if ':' in stepStr:
                    condition, workflowName = re.split(':', stepStr)
                    category = condition[0]
                    comparison = condition[1]
                    num = int(condition[2:])
                    steps.append((category, comparison, num, workflowName))
                else:
                    steps.append(stepStr)
            workflows[name] = steps
        else:
            xmas = re.split('{x=|,m=|,a=|,s=|}', line)
            x, m, a, s = int(xmas[1]), int(xmas[2]), int(xmas[3]), int(xmas[4])
            currWorkflowName = 'in'
            while True:
                if currWorkflowName == 'A':
                    acceptedSum += x + m + a + s
                    break
                elif currWorkflowName == 'R':
                    break

                for step in workflows[currWorkflowName]:
                    if type(step) == str:
                        currWorkflowName = step
                        break
                    else:
                        category, comparison, num, nextWorkflowName = step
                        if category == 'x':
                            val = x
                        elif category == 'm':
                            val = m
                        elif category == 'a':
                            val = a
                        elif category == 's':
                            val = s
                        hasFulfilled = val < num if comparison == '<' else val > num
                        if hasFulfilled:
                            currWorkflowName = nextWorkflowName
                            break
print(acceptedSum)

### PART 2 ###

class Node:
    def __init__(self, category=None, val=None, isAccepted=False):
        self.category = category
        self.val = val
        self.isAccepted = isAccepted
        self.left = None
        self.right = None

def assignChildren(node, steps):
    if len(steps) == 1:
        step = steps[0]
        assert type(step) == str
        if step == 'A':
            node.isAccepted = True
        elif step != 'R':
            node = assignChildren(node, workflows[step])
    else:
        # Assign node for true condition
        category, comparison, num, nextWorkflowName = steps[0]
        isTrueConditionOnLeftChild = comparison == '<'
        node.category = category
        node.val = num if isTrueConditionOnLeftChild else num + 1
        trueNode = Node()
        if nextWorkflowName == 'A':
            trueNode.isAccepted = True
        elif nextWorkflowName != 'R':
            trueNode = assignChildren(trueNode, workflows[nextWorkflowName])
        if isTrueConditionOnLeftChild:
            node.left = trueNode
        else:
            node.right = trueNode

        # Assign node for false condition
        falseNode = Node()
        if isTrueConditionOnLeftChild:
            node.right = assignChildren(falseNode, steps[1:])
        else:
            node.left = assignChildren(falseNode, steps[1:])

    return node

numAccepted = 0
rootNode = assignChildren(Node(), workflows['in'])
queue = [(rootNode, (1, 4000), (1, 4000), (1, 4000), (1, 4000))] # list of (node, x range, m range, a range, s range)
while len(queue):
    newQueue = []
    for node, xRange, mRange, aRange, sRange in queue:
        if node.isAccepted:
            size = (xRange[1] - xRange[0] + 1) * (mRange[1] - mRange[0] + 1) * (aRange[1] - aRange[0] + 1) * (sRange[1] - sRange[0] + 1)
            numAccepted += size
        elif node.category is not None:
            leftXRange, leftMRange, leftARange, leftSRange = xRange, mRange, aRange, sRange
            rightXRange, rightMRange, rightARange, rightSRange = xRange, mRange, aRange, sRange
            if node.category == 'x':
                leftXRange, rightXRange = (xRange[0], node.val - 1), (node.val, xRange[1])
            elif node.category == 'm':
                leftMRange, rightMRange = (mRange[0], node.val - 1), (node.val, mRange[1])
            elif node.category == 'a':
                leftARange, rightARange = (aRange[0], node.val - 1), (node.val, aRange[1])
            elif node.category == 's':
                leftSRange, rightSRange = (sRange[0], node.val - 1), (node.val, sRange[1])
            newQueue.append((node.left, leftXRange, leftMRange, leftARange, leftSRange))
            newQueue.append((node.right, rightXRange, rightMRange, rightARange, rightSRange))
    queue = newQueue
print(numAccepted)
