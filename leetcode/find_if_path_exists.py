

"""
find if path exists:

easy


"""


from readline import add_history


def makeGraph(edges):

    graph = {}

    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        
        if edge[1] not in graph:
            graph[edge[1]] = []
        
        graph[edge[1]].append(edge[0])
        graph[edge[0]].append(edge[1])
    return graph


def validPath(n, edges, source, destination):
    graph = makeGraph(edges)
    queue = [source]
    visited = set()

    while len(queue) > 0:
        current = queue.pop()

        if current in visited:
            continue

        if current == destination:
            return True

        for item in graph[current]:
            queue.insert(0, item)
        visited.add(current)
    return False





