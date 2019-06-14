from random import randint

from class_test import Car


class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

aBST = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
isBST = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
    .insert(500).insert(1500).insert(50).insert(200).insert(10000).insert(2200)
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
randoms = [45, 44, 41, 5, 16, 29, 32, 36]
randoms_with_negative_numbers = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
"""
space: O(n)
time: O(n)
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
196418, 317811,
"""
