

"""
sort stack: medium

time: O(n^2)
space: O(n)

"""


def insertInSortedOrder(stack, value):

    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insertInSortedOrder(stack, value)
    stack.append(top)


def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack, top)
    return stack