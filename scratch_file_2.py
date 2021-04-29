from itertools import zip_longest
import math
import re
import collections

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))



x = {'z', 'c', 't'}
y = {'yike', 'greg', 'gun'}

def productSum(arr):
    sum = 1
    for item in arr:
        sum = sum * item
    return sum


def aproductExceptSelf(arr):
    totals = [0 for x in arr]
    for i in range(len(arr)):
        arrExceptSelf = arr[:i] + arr[i + 1:]
        totals[i] = productSum(arrExceptSelf)
    return totals


print(productExceptSelf([1, 2, 3, 4]))