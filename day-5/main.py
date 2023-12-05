import re

### PART 1 ###

def getDest(text, nums):
    sourceRanges, destRanges = [], []
    for i in re.split('\n', text):
        if not i:
            continue

        l = [int(j) for j in re.split(' ', i)]
        source, dest, step = l[1], l[0], l[2]
        sourceRanges.append((source, source + step - 1))
        destRanges.append((dest, dest + step - 1))

    newNums = []
    for num in nums:
        newNum = None
        for i, sourceRange in enumerate(sourceRanges):
            if num >= sourceRange[0] and num <= sourceRange[1]:
                newNum = (destRanges[i][0] + num - sourceRange[0])
                break
        if newNum is None:
            newNum = num
        newNums.append(newNum)
    return sorted(list(set(newNums)))

with open('input.txt', 'r') as f:
    lines = f.read()
    l = re.split('seeds: |\nseed-to-soil map:\n|\nsoil-to-fertilizer map:\n|\nfertilizer-to-water map:\n|\nwater-to-light map:\n|\nlight-to-temperature map:\n|\ntemperature-to-humidity map:\n|\nhumidity-to-location map:\n', lines)
    l = list(filter(None, l))

    seeds = [int(i) for i in re.split(' |\n', l[0]) if i]

    soil = getDest(l[1], seeds)
    fertilizer = getDest(l[2], soil)
    water = getDest(l[3], fertilizer)
    light = getDest(l[4], water)
    temperature = getDest(l[5], light)
    humidity = getDest(l[6], temperature)
    location = getDest(l[7], humidity)

    print(min(location))

### PART 2 ###

def getSortedMappings(text, maxEnd):
    # Get ranges sorted by source
    ranges = []
    currMax = maxEnd
    for i in re.split('\n', text):
        if not i:
            continue

        l = [int(j) for j in re.split(' ', i)]
        source, dest, step = l[1], l[0], l[2]
        ranges.append(((source, source + step - 1), (dest, dest + step - 1)))
        currMax = max(currMax, dest + step - 1)
    ranges = sorted(ranges, key=lambda t: t[0][0])

    # Pad ranges with missing source-to-dest range
    newRanges = []
    curr = 0
    for range in ranges:
        start, end = range[0]
        if curr < start:
            newRanges.append(((curr, start - 1), (curr, start - 1)))
        newRanges.append(range)
        currMax = max(currMax, start - 1)
        curr = end + 1

    # Pad ranges with max end
    if curr < currMax:
        newRanges.append(((curr, currMax), (curr, currMax)))

    return newRanges, currMax

def combineRanges(ranges):
    newRanges = []
    currStart = None
    for i in range(len(ranges) - 1):
        currStart = currStart if currStart else ranges[i][0]
        currEnd = ranges[i][1]
        nextStart = ranges[i + 1][0]
        if currEnd < nextStart - 1:
            newRanges.append((currStart, currEnd))
            currStart = None
    currStart = currStart if currStart else ranges[-1][0]
    currEnd = ranges[-1][1]
    newRanges.append((currStart, currEnd))
    return newRanges

def getDestRangesFromSourceRanges(sourceRanges, mappings):
    destRanges = []
    for sourceRange in sourceRanges:
        sourceStart, sourceEnd = sourceRange
        for i in range(len(mappings)):
            sourceMapStart, sourceMapEnd = mappings[i][0]
            if sourceStart >= sourceMapStart and sourceEnd <= sourceMapEnd:
                destMapStart, _ = mappings[i][1]
                destRanges.append((destMapStart + sourceStart - sourceMapStart, destMapStart + sourceEnd - sourceMapStart))
                break
            elif sourceStart >= sourceMapStart and sourceEnd > sourceMapEnd:
                destMapStart, destMapEnd = mappings[i][1]
                destRanges.append((destMapStart + sourceStart - sourceMapStart, destMapEnd))
                sourceStart = sourceMapEnd + 1
    return combineRanges(sorted(destRanges, key=lambda t: t[0]))

with open('input.txt', 'r') as f:
    lines = f.read()
    l = re.split('seeds: |\nseed-to-soil map:\n|\nsoil-to-fertilizer map:\n|\nfertilizer-to-water map:\n|\nwater-to-light map:\n|\nlight-to-temperature map:\n|\ntemperature-to-humidity map:\n|\nhumidity-to-location map:\n', lines)
    l = list(filter(None, l))

    seeds = [int(i) for i in re.split(' |\n', l[0]) if i]
    seedRanges = []
    for i in range(len(seeds) // 2):
        seedRanges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
    seedRanges = combineRanges(sorted(seedRanges, key=lambda t: t[0]))

    maxEnd = seedRanges[-1][1]
    seedToSoil, maxEnd = getSortedMappings(l[1], maxEnd)
    soilToFertilizer, maxEnd = getSortedMappings(l[2], maxEnd)
    fertilizerToWater, maxEnd = getSortedMappings(l[3], maxEnd)
    waterToLight, maxEnd = getSortedMappings(l[4], maxEnd)
    lightToTemperature, maxEnd = getSortedMappings(l[5], maxEnd)
    temperatureToHumidity, maxEnd = getSortedMappings(l[6], maxEnd)
    humidityToLocation, _ = getSortedMappings(l[7], maxEnd)

    soilRanges = getDestRangesFromSourceRanges(seedRanges, seedToSoil)
    fertilizerRanges = getDestRangesFromSourceRanges(soilRanges, soilToFertilizer)
    waterRanges = getDestRangesFromSourceRanges(fertilizerRanges, fertilizerToWater)
    lightRanges = getDestRangesFromSourceRanges(waterRanges, waterToLight)
    temperatureRanges = getDestRangesFromSourceRanges(lightRanges, lightToTemperature)
    humidityRanges = getDestRangesFromSourceRanges(temperatureRanges, temperatureToHumidity)
    locationRanges = getDestRangesFromSourceRanges(humidityRanges, humidityToLocation)
    print(locationRanges)
