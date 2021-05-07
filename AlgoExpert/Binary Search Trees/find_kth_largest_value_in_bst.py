

"""
find kth largest value in bst


"""

class BST:
    def __init__(self, value, left=None, right=None):
        self.value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    sortedValues = []
    inOrderTraverse(tree, sortedValues)
    return sortedValues[len(sortedValues) - k]

def inOrderTraverse(node, sortedNodeValues):
    if node is None:
        return

    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)

