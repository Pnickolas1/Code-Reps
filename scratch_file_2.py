from itertools import zip_longest
import math
import collections

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

#intersect
r3 = Rectangle(1, 2, 3, 4)
r4 = Rectangle(1, 2, 3, 4)

# does not intersect
r1 = Rectangle(1, 2, 3, 4)
r2 = Rectangle(5, 3, 2, 4)




def moveElementToEnd(arr, target):

    def swap(i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    leftIdx = 0
    rightIdx = len(arr) - 1
    while leftIdx < rightIdx:
        while leftIdx < rightIdx and arr[rightIdx] == target:
            rightIdx -= 1
        if arr[leftIdx] == target:
            swap(leftIdx, rightIdx, arr)
        leftIdx += 1
    return arr



print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))



