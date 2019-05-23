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

    * you can represent a heap beautifully in a conventional array *
    [8, 12, 23, 17, 31, 30, 44, 102, 18]

    Current node = Idx
    -> child one = (2 * idx) + 1
    -> child two = (2 * idx) + 2

    TO find the parent node of a current node:
    floor((idx - 1)/ 2)

    - typically use a heap when you want to keep track of the greatest value or the
    smallest value


"""

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        """
        time: O(n)
        space: O(1)

        takes unsorted list and represents a heap with an array
        you want to implement with siftdown Method

        :param array:
        :return:
        """
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        """
        time: O(log n)
        space: O(log n)

        * famous method of a min heap


        :return:
        """
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != 1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break


    def siftUp(self, currentIdx, heap):
        """
        time: O(log n)
        space: O(log n)

        :return:
        """
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2


    def peek(self):
        return self.heap[0]

    def remove(self):
        """
        swaps the root with the last value in the heap
         and then popping the last value in the heap
        :return:
        """
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        """
        :return:
        """
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i] , heap[j] = heap[j], heap[i]