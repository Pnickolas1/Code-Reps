


# recursively
def level_order_recursion(root):

    levels = []
    if not root:
        return levels

    def helper(root, level):
        # start the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(root.val)

        # process child nodes for the next level
        if root.left:
            helper(root.left, level + 1)
        if root.right:
            helper(root.right, level + 1)


    helper(root, 0)
    return levels



from collections import deque

# iterative
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root, ])
    while queue:
        # start the current level
        levels.append([])
        # number of elements in the current level
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # fulfill the current level
            levels[level].append(node.val)

            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # go to next level
        level += 1

    return levels