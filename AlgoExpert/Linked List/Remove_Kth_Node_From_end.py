"""
Remove Kth node from end - linked list



Space:
Time:

"""

def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next


def removeKthNodeFromEnd(head, k):
    counter = 1
    runner = head
    trailer = head
    while counter <= k:
        runner = runner.next
        counter += 1
    if runner is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while runner.next is not None:
        runner = runner.next
        trailer = trailer.next
    trailer.next = trailer.next.next