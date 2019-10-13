

def swap(i, k, arr):
    arr[i], arr[k] = arr[k], arr[i]


def selectionSort(arr):
    currentIdx = 0
    while currentIdx < len(arr) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(arr)):
            if arr[smallestIdx] > arr[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, arr)
        currentIdx += 1
    return arr

