

"""
given an adjacency list representing a graph, determine if there is a cycle in the graph
dfs*

"""


def cycleInGraph(edges):
    numberOfNodes = len(edges)

    visited = [False for x in range(numberOfNodes)]
    currentlyInStack = [False for x in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue

        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            return True
    return False

def isNodeInCycle(node, edges, visited, currentInStack):

    visited[node] = True
    currentInStack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(neighbor, edges, visited, currentInStack)
            if containsCycle:
                return True
        elif currentInStack[neighbor]:
            return True
    currentInStack[node] = False
    return False


