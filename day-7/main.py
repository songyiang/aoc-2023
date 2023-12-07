from collections import Counter
import re

### PART 1 ###

five = []
four = []
full = []
three = []
two = []
one = []
high = []

mapCharToRank = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

def sortHands(t):
    handRank = 0
    for char in t[0]:
        handRank = handRank * 100 + mapCharToRank[char]
    return handRank

with open('input.txt', 'r') as f:
    for line in f:
        l = re.split(' |\n', line)
        hand, bid = l[0], int(l[1])

        chars = Counter(hand)
        size = len(chars.keys())
        if size == 1:
            five.append((hand, bid))
        elif size == 2:
            if chars.most_common(1)[0][1] == 4:
                four.append((hand, bid))
            else:
                full.append((hand, bid))
        elif size == 3:
            if chars.most_common(1)[0][1] == 3:
                three.append((hand, bid))
            else:
                two.append((hand, bid))
        elif size == 4:
            one.append((hand, bid))
        elif size == 5:
            high.append((hand, bid))

    final = []
    final.extend(sorted(high, key=sortHands))
    final.extend(sorted(one, key=sortHands))
    final.extend(sorted(two, key=sortHands))
    final.extend(sorted(three, key=sortHands))
    final.extend(sorted(full, key=sortHands))
    final.extend(sorted(four, key=sortHands))
    final.extend(sorted(five, key=sortHands))

    rank = 0
    score = 0
    for _, bid in final:
        rank += 1
        score += rank * bid
    print(score)

### PART 2 ###

five = []
four = []
full = []
three = []
two = []
one = []
high = []

mapCharToRank = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

with open('input.txt', 'r') as f:
    for line in f:
        l = re.split(' |\n', line)
        hand, bid = l[0], int(l[1])

        chars = Counter(hand)
        hasJoker = 'J' in chars
        size = len(chars.keys())
        if size == 1:
            five.append((hand, bid))
        elif size == 2:
            if hasJoker:
                five.append((hand, bid))
            else:
                if chars.most_common(1)[0][1] == 4:
                    four.append((hand, bid))
                else:
                    full.append((hand, bid))
        elif size == 3:
            if hasJoker:
                topTwo = chars.most_common(2)
                if topTwo[0][0] != 'J' and topTwo[1][0] != 'J' and topTwo[0][1] == 2 and topTwo[1][1] == 2:
                    # J AA KK -> full
                    full.append((hand, bid))
                else:
                    # J AAA K -> four
                    # JJ AA K -> four
                    # JJJ A K -> four
                    four.append((hand, bid))
            else:
                if chars.most_common(1)[0][1] == 3:
                    three.append((hand, bid))
                else:
                    two.append((hand, bid))
        elif size == 4:
            if hasJoker:
                three.append((hand, bid))
            else:
                one.append((hand, bid))
        elif size == 5:
            if hasJoker:
                one.append((hand, bid))
            else:
                high.append((hand, bid))

    final = []
    final.extend(sorted(high, key=sortHands))
    final.extend(sorted(one, key=sortHands))
    final.extend(sorted(two, key=sortHands))
    final.extend(sorted(three, key=sortHands))
    final.extend(sorted(full, key=sortHands))
    final.extend(sorted(four, key=sortHands))
    final.extend(sorted(five, key=sortHands))

    rank = 0
    score = 0
    for _, bid in final:
        rank += 1
        score += rank * bid
    print(score)
