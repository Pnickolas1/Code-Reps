
import pprint
import sys

x = [8, 12, 2, 3, 15, 5, 7]
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
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

def qsHelper(arr, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    pivot = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while leftIdx <= rightIdx:
        if arr[leftIdx] >= arr[pivot] and arr[rightIdx] <= arr[pivot]:
            swap(leftIdx, rightIdx, arr)
        if arr[leftIdx] < arr[pivot]:
            leftIdx += 1
        if arr[rightIdx] > arr[pivot]:
            rightIdx -= 1
    swap(rightIdx, pivot, arr)
    leftIsSmaller = rightIdx - startIdx - 1 < endIdx - rightIdx + 1
    if leftIsSmaller:
        qsHelper(arr, startIdx, rightIdx - 1)
        qsHelper(arr, rightIdx + 1, endIdx)
    else:
        qsHelper(arr, rightIdx + 1, endIdx)
        qsHelper(arr, startIdx, rightIdx - 1)

def quickSort(arr):
    qsHelper(arr, 0, len(arr) - 1)
    return arrpoy