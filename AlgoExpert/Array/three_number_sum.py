

"""
medium difficulty

sorting the array, left and right pointer

sorting will take O(n log n), this will not take up any additional space bc
using quicksort will help us sort in place

time: O(n^2)
space: O(n)

"""


def three_number_sum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        leftIdx = i + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            currentSum = array[i] + array[leftIdx] + array[rightIdx]
            if currentSum == targetSum:
                triplets.append([array[i], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1

            elif currentSum < targetSum:
                leftIdx += 1
            elif currentSum > targetSum:
                rightIdx -= 1
    return triplets


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, value):
        self.children.append(Node(value))

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.value)
            for child in current.children:
                queue.append(child)
        return array
