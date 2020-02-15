
import pprint
import sys
x = [8, 12, 2, 3, 15, 5, 7]
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
z = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
sampleInput = [[1,3,4,10],
               [2,5,9,11],
               [6,8,12,15],
               [7,13,14,16]
               ]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereq = []
        self.visited = False
        self.visiting = False

class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

    def addPrereq(self, job, dep):
        node = self.getNode(job)
        prereq = self.getNode(dep)
        node.prereqs.append(prereq)



def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for pre, job in deps:
        graph.addPrereq(job, pre)
    return graph


def dfs(node, orderedNodes):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereq in node.prereqs:
        containsCycle = dfs(prereq, orderedNodes)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedNodes.append(node.job)

def createSortedOrder(graph):
    orderedNodes = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = dfs(node, orderedNodes)
        if containsCycle:
            return []
    return orderedNodes



def topologicalSort(jobs, deps):
    graph = createJobGraph(jobs, deps)
    return createSortedOrder(graph)
