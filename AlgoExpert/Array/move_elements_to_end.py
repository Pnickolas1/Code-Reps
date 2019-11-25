"""

Move element to end ->
given an array of integers, and a target number, move all instances of target to the end
of the array

function signature:
def moveToEnd(arr : array, toMove: integer):
    pass

caveats: must be done in place

Time: O(n)
Space: O(1)

given = [2, 1, 2, 2, 2, 3, 4, 2]
return [1, 3, 4, 2, 2, 2, 2, 2,]



"""


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def moveElementToEnd(arr, toMove):
    leftIdx = 0
    rightIdx = len(arr) - 1

    while leftIdx < rightIdx:
        while leftIdx < rightIdx and arr[rightIdx] == toMove:
            rightIdx -= 1
        if arr[leftIdx] == toMove:
            swap(leftIdx, rightIdx, arr)
        leftIdx += 1
    return arr



