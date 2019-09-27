def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, value):
        self.children.append(Node(value))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.value)
            for child in current.children:
                queue.append(child)
        return array


    def depthFirstSearch(self, array):

