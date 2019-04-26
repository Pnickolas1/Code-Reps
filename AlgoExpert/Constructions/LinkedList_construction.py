

"""
### implementation of a Linked List - (double linked list)

a data structure that consists of nodes, each node has a value
also every node will have pointers to the node before and after that node

- in a singly linked list, every node will point to the following node
- typically convention is prev and next
- every linked list has a head and tail, the head is the beginning of a linked list
- you only can have access to the head and tail, everything in between you have to traverse to


space & time

search :
time: O(n)
space: o(1)

removal methods:
time: O(1)
space: O(1)

remove all nodes in a linked list w/ value X:
time: O(n)
space: O(1)

insert before, insert after, insert head, insert tail
time: O(1)
space: O(1)


insert @ position P:
time: O(p) , you have to traverse to position p
space: O(1)

"""

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        pass

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, node):
        pass

    def removeNodesWithValue(self, value):
        pass

    def remove(self, node):
        pass

    def containsNodeWithValue(self, value):
        pass





