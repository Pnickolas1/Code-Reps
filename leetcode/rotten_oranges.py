from collections import deque


"""
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.




"""

def orangesRotting(grid) -> int:

    q = deque()
    time, fresh = 0, 0

    ROWS, COLS = len(grid), len(grid[0])

    # problem set up
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])
    
    # helper array to handle the directions
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                
                if (row < 0 or row == ROWS or col < 0 or col == COLS):
                    continue

                elif grid[row][col] != 1:
                    continue

                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1

