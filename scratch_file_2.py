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



def leve


