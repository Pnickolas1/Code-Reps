

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
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)


    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self._removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None


    def _removeNodeBindings(self, node):
        """
        removing node bindings in the correct order
        :param node:
        :return:
        """
        if node.prev is not None:
            node.prev.next = node.next
        node.prev = None

        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None





































