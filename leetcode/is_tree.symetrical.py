


def isSymmetric(root):

    stack = [root, root]

    while stack:

        t1 = stack.pop(0)
        t2 = stack.pop(0)


        if t1 is None and t2 is None:
            continue

        if t1 and not t2:
            return False

        if not t1 and t2:
            return False

        if t1.val != t2.val:
            return False

        stack.append(t1.left)
        stack.append(t2.right)
        stack.append(t1.right)
        stack.append(t2.left)
    
    return True