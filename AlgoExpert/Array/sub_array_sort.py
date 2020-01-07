


"""
Sub Array sort

time: O(n) - n is length of array
space: O(1)

- find the min and max of the unsorted values


* how to find unsorted numbers in array? - compare each number to it's 2 adjacent values


"""


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


def subarraySort(array):
    minOutOfOrder = float('inf')
    maxOutOfOrder = float('-inf')
    for i, num in enumerate(array):
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if maxOutOfOrder == float('-inf'): # if the entire input array is sorted!
        return [-1, -1]
    subArrayLeftIdx = 0
    while minOutOfOrder >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx, subArrayRightIdx]





"""




"""


def OOO(idx, val, array):
    if idx == 0:
        return val > array[idx + 1]
    elif idx == len(array) - 1:
        return val < array[idx - 1]
    return val > array[idx + 1] or val < array[idx - 1]


def subarraySort(array):
    minValOutOfOrder = float('inf')
    maxValOutOfOrder = float('-inf')
    for i, val in enumerate(array):
        if OOO(i, val, array):
            minValOutOfOrder = min(minValOutOfOrder, val)
            maxValOutOfOrder = max(maxValOutOfOrder, val)

    if maxValOutOfOrder == float('-inf'):
        return [-1, -1]

    subArrayLeftIdx = 0

    while minValOutOfOrder >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array) -1

    while maxValOutOfOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayRightIdx, subArrayRightIdx]
