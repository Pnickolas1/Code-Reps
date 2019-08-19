

"""
Quicksort - HARD

sort list of values
pick a pivot, sort every value with respect of the pivot

you must use quicksort recursively, which will require putting frames on the callstack
- read up on tail recursion

time:
    worst: O(n^2)
    best: O(n log(n))
    avg: O(N log(N))
space:
    worst: O(log(n))

"""

def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def quickSortHelper(array, startIdx, endIdx):
    """
    :param array:
    :param startIdx:
    :param endIdx:
    :return:
    """
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)



