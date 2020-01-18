



"""
max depth in binary tree:



"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # iterative
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue

        return depth

    # recursive
    def maxDepthRecur(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(
                self.maxDepthRecur(root.left),
                self.maxDepthRecur(root.right),
            )

