

"""
invert a binary tree: medium

itertive:
time: O(n)
space: O(n)

recursvie:
time: O(n)
space: O(d) - depth of tree

takes in a root node of a binary tree

"""
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

def invertBinaryTree_iterative(tree):
    queue= [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)


### RECURSIVE SOLUTION
def invertBinaryTree_recursive(tree):
    """
    time: O(n)
    space: O(d) d is depth of tree
    :param tree:
    :return:
    """
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree_recursive(tree.left)
    invertBinaryTree_recursive(tree.right)
