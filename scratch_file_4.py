



def stairCase(n):

    cache = {}

    def helper(n):
        if n in cache:
            return cache[n]
        elif n <= 2:
            return n
        else:
            x = helper(n - 1)
            cache[n] = x

    helper(5)


print(stairCase(6))



def inorderTraverse(root, array):

    if root is not None:

        inorderTraverse(root.left, array)
        array.append(root.value)
        inorderTraverse(root.right, array)
    return array





