"""
heap sort

best:
    time: O(n log(n))
    space: O(1)

average:
    time: O(n log(n))
    space: O(1)

worst:
    time: O(n log(n))
    space: O(1)



"""

def buildMaxHeap(arr):
    firstParentIdx = (len(arr) - 1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(arr) - 1, arr)

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def siftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return

def heapSort(arr):
    buildMaxHeap(arr)
    for endIdx in reversed(range(1, len(arr))):
        swap(0, endIdx, arr)
        siftDown(0, endIdx - 1, arr)
    return arr


