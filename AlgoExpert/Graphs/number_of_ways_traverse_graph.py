

""""
number of ways to traverse a graph

"""

def numberOfWaysToTraverseGraph(width, height):

    numberOfWays = [[0 for x in range(width + 1)] for y in range(height + 1)]

    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberOfWays[heightIdx][widthIdx - 1]
                waysUp = numberOfWays[heightIdx - 1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysUp + waysLeft
    return numberOfWays[height][width]