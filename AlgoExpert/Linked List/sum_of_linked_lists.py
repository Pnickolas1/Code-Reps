

"""
sum of linked lists:




"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedList = LinkedList(0)
    currentNode = newLinkedList
    carry= 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry > 0:
        nodeOneValue = nodeOne.value if nodeOne is not None else 0
        nodeTwoValue = nodeTwo.value if nodeTwo is not None else 0

        nodeSums = nodeOneValue + nodeTwoValue + carry
        newValue = nodeSums % 10

        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = currentNode.next

        carry = nodeSums // 10

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedList.next
