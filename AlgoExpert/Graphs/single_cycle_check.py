"""
single cycle check: medium

time: O(n)
space: O(1)



sample input: [2, 3, 1, -4, -4, 2]
sample output: true
"""


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx == 0


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
