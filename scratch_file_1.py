from collections import Counter, OrderedDict
from heapq import heapify, heappop, heappush, heapreplace
from os import scandir
import random
import math

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

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
x = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

def swap(l, r, arr):
    arr[l], arr[r] = arr[r], arr[l]

def swapTree(tree):
    tree.left. tree.right = tree.right, 

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j -1]:
        unvisitedNeighbors.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors

x = [1, 2, 3, 5, 5, 5, 5, 8, 10, 12, 12, 12, 15, 19, 20, 21, 21]


def median(nums1, nums2):

    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)

    left = 0
    right = n - 1

    while True:

        pointer1 = left + (right - left) // 2
        pointer2 = (m + n) // 2 - pointer1 - 2

        left1 = nums1[pointer1] if pointer1 in range(n) else -math.inf
        left2 = nums2[pointer2] if pointer2 in range(m) else -math.inf
        right1 = nums1[pointer1 + 1] if pointer1 + 1 in range(n) else math.inf
        right2 = nums2[pointer2 + 1] if pointer2 + 1 in range(m) else math.inf


        if left1 <= right2 and left2 <= right1:
            if (n + m) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return min(right1, right2)
        else:
            if left1 > right2:
                right = pointer1 - 1
            else:
                left = pointer1 + 1



    
