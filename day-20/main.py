from enum import Enum
from math import lcm
import re

### PART 1 ###

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Module:
    def __init__(self, moduleName) -> None:
        self.moduleName = moduleName
        self.moduleType = None
        self.isOn = False
        self.memory = {}
        self.outputModules = []

    def connectToPrev(self, prevModule):
        self.memory[prevModule] = Pulse.LOW

    def connectToNext(self, nextModule):
        self.outputModules.append(nextModule)

    def process(self, prevModule, inputPulse):
        outputPulse = None
        if self.moduleType == '%':
            if inputPulse == Pulse.LOW:
                self.isOn = not self.isOn
                outputPulse = Pulse.HIGH if self.isOn else Pulse.LOW
        elif self.moduleType == '&':
            self.memory[prevModule] = inputPulse
            outputPulse = Pulse.LOW if all([p == Pulse.HIGH for p in self.memory.values()]) else Pulse.HIGH
        elif self.moduleType == 'broadcaster':
            outputPulse = inputPulse
        return self.outputModules, outputPulse

def getModules():
    with open('input.txt', 'r') as f:
        modules = {}
        for line in f:
            line = re.split(' -> ', line.strip())

            inputModuleName = line[0] if line[0] == 'broadcaster' else line[0][1:]
            inputModule = modules.get(inputModuleName, Module(inputModuleName))
            modules[inputModuleName] = inputModule
            inputModule.moduleType = line[0] if line[0] == 'broadcaster' else line[0][0]

            outputModuleNames = re.split(', ', line[1])
            for outputModuleName in outputModuleNames:
                outputModule = modules.get(outputModuleName, Module(outputModuleName))
                modules[outputModuleName] = outputModule
                inputModule.connectToNext(outputModule)
                outputModule.connectToPrev(inputModule)
    return modules

modules = getModules()
numLow = 0
numHigh = 0
for _ in range(1000):
    broadcastModule = modules['broadcaster']
    numLow += 1
    queue = [(broadcastModule, None, Pulse.LOW)]
    while len(queue):
        newQueue = []
        for inputModule, prevModule, inputPulse in queue:
            outputModules, outputPulse = inputModule.process(prevModule, inputPulse)
            if outputPulse == None:
                continue
            for outputModule in outputModules:
                if outputPulse == Pulse.LOW:
                    numLow += 1
                else:
                    numHigh += 1
                newQueue.append((outputModule, inputModule, outputPulse))
        queue = newQueue
print(numLow * numHigh)

### PART 2 ###


# Get parents of parent of rx
modules = getModules()
parentOfRx = list(modules['rx'].memory.keys())[0].moduleName
grandparentsOfRx = list(modules[parentOfRx].memory.keys())
checkModuleNames = {}
for module in grandparentsOfRx:
    checkModuleNames[module.moduleName] = None

numPresses = 0
numChecked = 0
while True:
    broadcastModule = modules['broadcaster']
    numPresses += 1
    queue = [(broadcastModule, None, Pulse.LOW)]
    while len(queue):
        newQueue = []
        for inputModule, prevModule, inputPulse in queue:
            outputModules, outputPulse = inputModule.process(prevModule, inputPulse)
            if outputPulse == None:
                continue
            for outputModule in outputModules:
                if outputPulse == Pulse.HIGH and inputModule.moduleName in checkModuleNames and checkModuleNames[inputModule.moduleName] is None:
                    checkModuleNames[inputModule.moduleName] = numPresses
                    numChecked += 1
                newQueue.append((outputModule, inputModule, outputPulse))
        queue = newQueue
    if numChecked == len(checkModuleNames):
        break
print(lcm(*checkModuleNames.values()))
