

# write a function to check that a binary tree is a valid binary search tree

# sample binary tree
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_binary_sesarch_tree_iter(root):

    # start at the root, with an arbitrarily low lower bound
    # and arbitrarily upperbound

    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    #depth first traversal
    while len(node_and_bounds_stack):

        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # if this node is invalid we return false right away
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))

        if node.right:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node.right, upper_bound, node.value))

    return True



# done recursively
def is_binary_search_tree_recur(root, lower_bound=-float('inf'), upper_bound=float('inf')):

    if not root:
        return True

    if (root.value >= upper_bound or root.value <= lower_bound):
        return False

    return (is_binary_search_tree_recur(root.left, lower_bound, root.value)
            and is_binary_search_tree_recur(root.right, upper_bound, root.value))

