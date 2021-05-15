 """
Quick Sort

write a function that takes in sort

[8, 5, 2, 9, 5, 6, 3]
best:
    time: O(n log(n))
    space: O( log(n))

avg:
    time: O(n log(n))
    space: O(log(n))

worst:
    time: O(n^2)
    space: O(log(n))
"""

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def quickSortHelper(arr, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if arr[leftIdx] > arr[pivotIdx] and arr[rightIdx] < arr[pivotIdx]:
            swap(leftIdx, rightIdx, arr)
        if arr[leftIdx] <= arr[pivotIdx]:
            leftIdx += 1
        if arr[rightIdx] >= arr[pivotIdx]:
            rightIdx -= 1
    swap(rightIdx, pivotIdx, arr)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(arr, startIdx, rightIdx - 1)
        quickSortHelper(arr, rightIdx + 1, endIdx)
    else:
        quickSortHelper(arr, rightIdx + 1, endIdx)
        quickSortHelper(arr, startIdx, rightIdx - 1)
