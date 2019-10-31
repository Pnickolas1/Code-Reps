from itertools import zip_longest
import math
import collections

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

#intersect
r3 = Rectangle(1, 2, 3, 4)
r4 = Rectangle(1, 2, 3, 4)

# does not intersect
r1 = Rectangle(1, 2, 3, 4)
r2 = Rectangle(5, 3, 2, 4)


def two_sorted_linked_lists(l1, l2):

    if not l1:
        return l2
    if not l2:
        return l1
    if not l1 and not l2:
        return None

    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curNode = head


    while l1 or l2:
        if (l1 and not l2) or (l1 and l2 and l1.val <= l2.val):
            curNode.next = l1
            curNode = curNode.next
            l1 = l1.next
        elif (l2 and not l1) or (l1 and l2 and l1.val > l2.val):
            curNode.next = l2
            curNode = curNode.next
            l2 = l2.next

    return head