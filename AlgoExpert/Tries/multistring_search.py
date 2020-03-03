"""

multistring search








"""


def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1
    while leftBigIdx <= rightBigIdx:
        if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]:
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    return True


def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False


def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]