"""

# tree traversal of a binary search tree

same space and time complexity for all three!
time: O(n)
space: O(n) where n is the length of the longest branch



inorder:
returns a sorted list


"""

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

# in order: [1, 2, 5, 5, 10, 15, 22]
# pre order: [10, 5, 2, 1, 5, 15, 22]
# post order: [1, 2, 5, 5, 22, 15, 10]
