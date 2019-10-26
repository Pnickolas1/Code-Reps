

"""
merge two sorted linked lists

merged two sorted linked lists and return is as a new list. the new list should be made by splicing
together the nodes of the first two lists


"""


def merge_two_sorted_linked_lists(l1, l2):
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