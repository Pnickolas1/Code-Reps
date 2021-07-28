
import math
import random
import pprint
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


def delete_dups(arr):

    if not arr:
        return 0

    write_idx = 1

    for i in range(1, len(arr)):
        if arr[write_idx - 1] != arr[i]:
            arr[write_idx] = arr[i]
            write_idx += 1
    print(arr)
    print(arr[:write_idx])
    return arr[:write_idx]


print(delete_dups(x))