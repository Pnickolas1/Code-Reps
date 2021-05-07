

"""
detect a cycle in a graph


"""


def isInCycle(node, visited, inCallStack, edges):
    visited[node] = True
    inCallStack[node] =  True

    neighbors = edges[node]
    for neibor in neighbors:
        if not visited[neibor]:
            containsCycle = isInCycle(neibor, visited, inCallStack, edges)
            if containsCycle:
                return True
        elif inCallStack[neibor]:
            return True
    inCallStack[node] = False
    return False


def cycleInGraph(edges):
    numberOfNodes= len(edges)

    visited = [False for x in range(numberOfNodes)]
    inCallStack = [False for x in range(numberOfNodes)]

    for node in range(numberOfNodes):

        if visited[node]:
            continue

        containsCycle = isInCycle(node, visited, inCallStack, edges)
        if containsCycle:
            return True
    return False