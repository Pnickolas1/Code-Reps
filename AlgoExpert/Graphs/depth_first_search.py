
import unittest


""""
# easy
depth first search

algorithm, very important, must know
exploring, or traversing a graph

deep rather than wide, go down all the way on one branch
 before you explore the next branch

vertices and edges
time = O(V + E)
    - why is v +e, at one point we traverse every node

space = O (V)
    - storing an array of all of vertices3

"""

class Node:

    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array




test1 = Node("a")

test1.addChild("b")
test1.addChild("c")
test1.addChild("d")
test1.addChild("e")
print(test1)
x = test1.depthFirstSearch([])
print(x)