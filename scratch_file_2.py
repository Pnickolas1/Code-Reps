from itertools import zip_longest

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

