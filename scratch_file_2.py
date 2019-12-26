from itertools import zip_longest
import math
import re
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


def minmum_difference_in_array(n, nums):
    minValue = float('inf')
    arr = [int(x) for x in nums.split(' ')]
    print(arr)
    for i in range(n):
        for j in range(i + 1, n):
            minValue = min(abs(arr[i] - arr[j]), minValue)
    return minValue


def this_is_fucking_stupic(arr):
    diffs = []
    arr.sort()
    for i in range(len(arr)-1):
        diffs.append(abs(arr[i]-arr[i+1]))
    return min(diffs)

def get_hour_glass(matrix):

    # [row][col]
    maxNum = float('-inf')
    for i in range(4):
        for j in range(4):
            value = sum([matrix[i][j], matrix[i][j + 1], matrix[i][j + 2], matrix[i + 1][j + 1], matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]])
            #value = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col + 1] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
            maxNum = max(value, maxNum)
    return maxNum

x = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
 ]

def hourglassSum(matrix):
    # [row][col]
    maxNum = float('-inf')
    for row in range(4):
        for col in range(4):
            value = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col + 1] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
            maxNum = max(value, maxNum)
    return maxNum


def left_rotation(arr, d):

    arrLength = len(arr)
    calcRotations = d % arrLength
    print(calcRotations)
    counter = 0

    while counter < calcRotations:
        val = arr.pop(0)
        print(arr)
        arr.append(val)
        print(arr)
        counter += 1
    return arr



def ransom_note(magazine, ransom):
    d = {}  # dict of word: count of that word in the note
    for word in magazine:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    for word in ransom:
        if word not in d:
            return False
        if d[word] == 0:
            return False
        d[word] -= 1
    return True


m = ['ive', 'got', 'some', 'coconuts']
n = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']

# true
mag = ['two', 'times', 'two', 'is', 'four']
note = ['two', 'times', 'three', 'is', 'not', 'four']

print(ransom_note(mag, note))



from collections import deque



def binary_search_in_matrix(grid, sr, sc, tr, tc):

    queue = deque()
    seen = set()
    queue.append((sr, sc, 0))
    seen.add((sr, sc))

    while queue:
        r, c, moves = queue.popleft()
        if r == tr and c == tc:
            return moves
        for (nr, nc) in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in seen:
                queue.append((nr, nc, moves + 1))
                seen.add((nr, nc))
    return -1






















