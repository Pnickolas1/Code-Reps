


"""
find the closest value in a binary search tree

time: O(log n)
space:  O(1)

gives you a bst and a target value
"""


def findClosestValueInBst(tree, target):
    return findClosestValueinBSThelper(tree, target, float('inf'))

def findClosestValueinBSThelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break

    return closest





