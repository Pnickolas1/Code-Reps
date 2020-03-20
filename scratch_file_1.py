
import pprint
import sys

x = [8, 12, 2, 3, 15, 5, 7]
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),+
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
z = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
sampleInput = [[1, 3, 4, 10],
               [2, 5, 9, 11],
               [6, 8, 12, 15],
               [7, 13, 14, 16]]
wordbank = ['this', 'that', 'apple', 'is', 'apology']

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def getNewPattern(pattern):
    newPattern = list(pattern)
    if newPattern[0] == "x":
        return newPattern
    else:
        return list(map(lambda char: "x" if char == "y" else "y", newPattern))


def getCounts(newPattern, counts):
    yIdx = None
    for i, char in enumerate(newPattern):
        counts[char] += 1
        if char == "y" and yIdx is None:
            yIdx = i
    return yIdx

def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []

    newPattern = getNewPattern(pattern)
    counts = {"x": 0, "y": 0}
    didSwitch = pattern[0] != newPattern[0]
    firstYIdx = getCounts(newPattern, counts)

    if counts["y"] != 0:
        for lenOfx in range(1, len(string)):
            lenOfy = (len(string) - lenOfx * counts['x']) / counts['y']
            if lenOfy <= 0 or lenOfy % 1 != 0:
                continue
            lenOfy = int(lenOfy)
            yIdx = firstYIdx * lenOfx
            x = string[:lenOfx]
            y = string[yIdx: yIdx + lenOfy]
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else:
        lenOfx = len(string) / counts['x']
        if lenOfx % 1 == 0:
            lenOfx = int(lenOfx)
            x = string[:lenOfx]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ''] if not didSwitch else ['', x]
    return []

