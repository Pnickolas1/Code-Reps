
"""
validate a BST

time: O(n) # n is the number of nodes
space: O(d) # d is the depth of the tree, length of the longest branch
 - this is because we are calling the function and putting it on the call stack

"""


def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBSTHelper(tree.right, tree.value, maxValue)

def validate(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))


