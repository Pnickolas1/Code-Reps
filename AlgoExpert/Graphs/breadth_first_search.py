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