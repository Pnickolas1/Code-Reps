"""
Min Heap Construction: medium

Implement a min heap class. the class should support insertiojn, removal (of the minimum/ root value)
peeking of (min/ root value)
sifting a value up and down the heap and building the heap from an input array
the heap should be represented in the form of an array

Sample input: [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
buildHeap(array)
-> insert(76)
-> remove()
-> remove()
-> insert(87)
SAMPLE OUTPUT:

similar to a binary tree, actually it is a binary tree
satisfies two additional properties:
    1. completeness
        -> all of its levels need to be filled completely EXCEPT
            the last or leaf level, if the leaf level is partially filled
            it has to be filled from the left to the right
    2. the heap property
        -> this is where you can distinguish between a minHeap and a maxHeap

        -> min heap
            - every node in the heap that has a value, is less than or equal it's children node's values
            -in a min heap the root node is the smallest node in the heap

        -> max heap
            - every node in the heap that has a value, is greater than or equal to it's children node's values
            - in a maxHeap the root node is the greatest node in the heap

    * a heap is not sorted *



"""

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        pass

    def siftDown(self):
        pass

    def peek(self):
        pass

    def remove(self):
        pass

    def insert(self):
        pass

