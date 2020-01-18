


def getUnvisitedNeighbors(r, c, matrix, visited):
    unvisited = []
    if r > 0 and not visited[r - 1][c]:
        unvisited.append([r - 1, c])
    if r < len(matrix) - 1 and not visited[r + 1][c]:
        unvisited.append([r + 1, c])
    if c < len(matrix[r]) - 1 and not visited[r][c + 1]:
        unvisited.append([r, c + 1])
    if c > 0 and not visited[r][c - 1]:
        unvisited.append([r, c - 1])
    return unvisited


def traverseNodes(r, c, matrix, visited, riverSizes):
    currentRiverSize = 0
    nodesToExplore = [[r, c]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        nr, nc = currentNode
        if visited[nr][nc] or visited[nr][nc] == 0:
            continue

        visited[nr][nc] = True
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(nr, nc, matrix, visited)
        for neibor in unvisitedNeighbors:
            nodesToExplore.append(neibor)

    if currentRiverSize > 0:
        riverSizes.append(currentRiverSize)


def riverSize(matrix):
    riverSizes = []
    visited = [[False for value in row] for row in matrix]

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if visited[r][c]:
                continue
            traverseNodes(r, c, matrix, visited, riverSizes)
    return riverSizes