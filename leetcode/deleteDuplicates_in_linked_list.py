
"""
Delete Duplicates in Linked List


1 => 1 => 2
returns: 1 => 2

"""


def delete_duplicates_in_linked_list(head):
    curNode = head
    while curNode:
        while curNode.next and curNode.val == curNode.next.val:
            curNode.next = curNode.next.next
        curNode = curNode.next
    return head

def delete_dupes(head):
    node = head
    while node:
        while node.next and node.next == node.next.next:
            node.next = node.next.next
        node = node.next
    return head