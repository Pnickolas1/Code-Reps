def isToeplitz(matrix):
    col = len(matrix[0]) - 1

    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            if matrix[r][c] != matrix[r + 1][c + 1]:
                return False
    return True

x = [[1, 2, 3, 4], [5, 1, 9, 3], [6, 5, 1, 2]]
print(isToeplitz(x))
# false

y = [[1,2,3,4], [5,1,2,3], [6,5,1,2]]


"""
[[1,2,3,4],
[5,1,2,3],
[6,5,1,2]]
"""

print(isToeplitz(y))



