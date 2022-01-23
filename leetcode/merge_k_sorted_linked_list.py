from heapq import heapify, heappop, heappushpop, heappush



"""

merge k sorted lists : 23

understnad pointer manipulation and that this problem builds on the merging two sorted linked lists

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge2SortedLLs(l1, l2):

    dummy = ListNode()
    curr = dummy

    while l1 and l2:

        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2

    return dummy.next


def mergeKLists(lists):

    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(merge2SortedLLs(l1, l2))
        
        lists = mergedLists
    return lists[0]
    



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    

        q = []
        heapify(q)

        for i, node in enumerate(lists):
            if node:
                heappush(q, (node.val, i))

        head = ListNode()
        curr = head

        while q:
            v, i = heappop(q)
            curr.next = lists[i]
            if lists[i].next:
                lists[i] = lists[i].next

                heappush(q, (lists[i].val, i))
            curr = curr.next

        return head.next
