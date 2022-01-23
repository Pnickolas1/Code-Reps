from collections import Counter, namedtuple
from heapq import heapify, heappop, heappush
from itertools import zip_longest
import math
import re

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

Rectangle = namedtuple('Rectangle', ('x', 'y', 'width', 'height'))





def TwoSumIv(root, target):

    def inOrderTravesal(root, arr):
        
        if root is None:
            return

        inOrderTravesal(root.left, arr)
        arr.append(root.val)
        inOrderTravesal(root.right, arr)

    arr = []
    inOrderTravesal(root, arr)

    l = 0
    r = len(arr) - 1


    while l < r:

        value = arr[l] + arr[r]
        if value == target:
            return True
        elif value < target:
            l =+ 1
        elif value > target:
            r -= 1
    
    return False