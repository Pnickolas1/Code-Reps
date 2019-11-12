"""

remove duplicates from a linked list


"""



def remove_duplicates_from_linked_list(head):
    curNode = head
    while curNode:
        while curNode.next and curNode.val == curNode.next.val:
            curNode.next = curNode.next.next
        curNode = curNode.next
    return head



