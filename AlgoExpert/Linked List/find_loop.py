"""
Write a function that takes in the head of a Singly Linked List that contains a loop

 - HARD

Time: O(n)
Space: O(1)


"""

def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second.second.next
    return first