

"""

- dfs and you can change the value in the matrix so you wouldn't visit the same node twice
-




"""


def markIsland(matrix):
    if not matrix:
        return 0

    count = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                dfs(matrix, r, c)
                count += 1
    return count


def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
        return
    grid[r][c] = 0
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)



binaryMatrix = [[0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 1, 0, 1]]

print(markIsland(binaryMatrix))