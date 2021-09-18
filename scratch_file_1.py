
from AlgoExpert.Stacks.sort_stack import insertInSortedOrder
import math
import random
import pprint
from scratch_file_3 import word_count_engine
import sys

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


def findMedianSortedArray(nums1, nums2):

    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)

    left = 0
    right =  n - 1

    while True:

        partition1 = left + (right - left) // 2
        partition2 = (n + m) // 2 - partition1 - 2

        left1 = nums1[partition1] if partition1 in range(n) else -math.inf
        left2 = nums2[partition2] if partition2 in range(m) else -math.inf
        right1 = nums1[partition1 + 1] if partition1 + 1 in range(n) else math.inf
        right2 = nums2[partition2 + 1] if partition2 + 1 in range(m) else math.inf

        if left1 <= right2 and left2 <= right1:
            if (n + m) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                min(right1, right2)
        elif left1 > right2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    

def runLengthEncoding(string):

    encodedChars = []
    currentRunLength = 1

    for i in range(1, len(string)):

        currentChar = string[i]
        prevChar = string[i -1 ]

        if currentChar != prevChar or currentRunLength == 9:
            encodedChars.append(str(currentRunLength))
            encodedChars.append(prevChar)
            currentRunLength = 0
        currentRunLength += 1
    
    encodedChars.append(str(currentRunLength))
    encodedChars.append(string[len(string)- 1])
    return "".join(encodedChars)

print(runLengthEncoding('aaaaabbcccccc'))
