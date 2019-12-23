"""
breadth first search : medium

traversing a graph, where the graph is going to be like a tree like structure

nodes, each node has a name
bread first search works, traverse level by level

use a queue! FIFO

time: O(V + E) - in a graph you have vertices and edges
space: O(V)
 - worst case the queue could hold all nodes in the queue, if all nodes
 were direct childs of the root node passed into the func


"""


class Node:

    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


"""
graph theory on two dimensional arrays (grid)

"""
def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    q = [(0, 0, 1)]
    for i, j, d in q:
        if i == n-1 and j == n-1: return d
        for x, y in ((i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)):
            if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                grid[x][y] = 1
                q.append((x, y, d+1))
    return -1
import collections
def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))










