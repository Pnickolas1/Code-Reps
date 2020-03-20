"""
Heap Sort: HARD


divide your array into two subarrays, 1 subarray will be sorted and
the other subarray will be unsorted.

will not be created two subarray!

the root node or value of a heap if you're dealing with a max heap, is the greatest value
within the heap (can be a min heap as well)

Time: O(n log(n))
Space: O(1)

"""


def buildMaxHeap(array):
    firstParentIdx = (len(array) -1) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)

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

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array
        
        
