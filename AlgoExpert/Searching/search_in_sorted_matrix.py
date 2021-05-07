"""
search in sorted matrix: medium

search for a number in a two-dimensional array  or otherwise known as a matrix

start at top right corner, and just eliminate or search

space: O(1)
time: O(N + M) , N is length of rows, M is length of colums

"""

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]