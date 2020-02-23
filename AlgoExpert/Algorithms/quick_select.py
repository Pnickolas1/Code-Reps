

"""
quick select

on average linear time



"""

def quickselect(arr, k):
    position = k - 1
    return quickSelectHelper(arr, 0, len(arr) - 1, position)

def quickSelectHelper(arr, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("this should never happen")
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if arr[leftIdx] > arr[pivotIdx] and arr[rightIdx] < arr[pivotIdx]:
                swap(leftIdx, rightIdx, arr)
            if arr[leftIdx] <= arr[pivotIdx]:
                leftIdx += 1
            if arr[rightIdx] >= arr[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, arr)
        if rightIdx == position:
            return arr[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1

def swap(one, two, arr):
    arr[one], arr[two] = arr[two], arr[one]