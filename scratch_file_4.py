



def getNeighbors(r, c, matrix, visited):
    newNeighbors = []
    if r > 0 and not visited[r -1][c]:
        newNeighbors.append([r -1, c])
    if r < len(matrix) - 1 and not visited[r + 1][c]:
        newNeighbors.append([r + 1, c])
    if c < len(matrix[0]) - 1 and not visited[r][c + 1]:
        newNeighbors.append([r, c + 1])
    if c > 0 and not visited[r][c - 1]:
        newNeighbors.append([r, c - 1])
    return newNeighbors

def traverseNode(r, c, matrix, visited, sizes):
    currentSize = 0
    neighbors = [[r, c]]
    while len(neighbors):
        current = neighbors.pop()
        nr, nc = current

        if visited[nr][nc]:
            continue

        visited[nr][nc] = True
        if matrix[nr][nc] == 0:
            continue

        currentSize += 1
        unvisitedNeighbors = getNeighbors(nr, nc, matrix, visited)
        for item in unvisitedNeighbors:
            neighbors.append(item)

    if currentSize > 0:
        sizes.append(currentSize)



def riverSizes(matrix):
    sizes = []
    visited = [[False for _ in row] for row in matrix]
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if visited[r][c]:
                continue
            traverseNode(r, c, matrix, visited, sizes)
    return sizes
