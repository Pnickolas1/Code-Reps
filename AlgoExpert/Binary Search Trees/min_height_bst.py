

"""
min height bst

given a sort array of uniq  ue integers, create a BST with a minimum heights:

the catch:

leverage the sorted, array, you need to insert midpoints, and  midpoints of the subarrays, also, while using
bst.insert method, you should know that the insert method of the a bst class runs in the O(n log(n)).

The O(n log(n)) seems like we can be more efficient.





"""



def helper(arr, bst, left, right):

    if left > right:
        return

    midpt = (left + right) // 2
    value = arr[midpt]
    node = BST(value)
    if bst is None:
        bst = node
    else:
        if node.value < bst.value:
            bst.left = node
            bst = bst.left
        else:
            bst.right = node
            bst = bst.right

    helper(arr, bst, left, midpt - 1)
    helper(arr, bst, midpt + 1, right)
    return bst


def minHeightBst(array):
    return helper(array, None, 0, len(array) - 1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)