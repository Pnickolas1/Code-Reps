

# write a function to see if a binary tree is 'superbalanced' ( a new tree property we just made up)
# if trouble is from recursive approach, try an iterative one


# well what are common ways to traverse a tree, 1. depth first, 2. breadth first
# ... well a depth search first will generally hit the leaves first (relative to a breadth first search)

## depth first search vs breadth first search
# advantages: DFS typically uses less memory, DFS can be easily implemented with recursion

# disadvantages: BFS typically finds the shortest path to a node



def is_balanced(tree_root):

    # a tree with no nodes is superbalanced, since there are no leaves
    if tree_root is None:
        return True

    # short-circuit as soon as we find more than 2
    depths = []

    # treat this list as a stack, and store in tuple with (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        # pop a node and its depth from the top of our stack
        node, depth = nodes.pop()

        # case: we found a leaf
        if (not node.left) and (not node.right):

            # we only case if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # two ways we might have a an unbalanced tree
                # 1. more than 2 different leaf depths
                # 2. 2 leaf depths that are more than 1 apart

                if((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0]) - depths[1] > 1)):
                    return False

            else:
                # case this is not a leaf - keep stepping down
                if nodes.left:
                    nodes.append((node.left, depth + 1))
                if nodes.right:
                    nodes.append((node.right, depth + 1))

    return True