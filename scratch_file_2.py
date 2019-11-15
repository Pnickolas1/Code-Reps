from itertools import zip_longest
import math
import collections

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

#intersect
r3 = Rectangle(1, 2, 3, 4)
r4 = Rectangle(1, 2, 3, 4)

# does not intersect
r1 = Rectangle(1, 2, 3, 4)
r2 = Rectangle(5, 3, 2, 4)


def longest_palindromic_subsequence(s):

    def is_palindrome(s):
        leftIdx = 0
        rightIdx = len(s) - 1
        while leftIdx <= rightIdx:
            if s[leftIdx] != s[rightIdx]:
                return False
            leftIdx += 1
            rightIdx -= 1
        return True

    longest = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i: j + 1]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    return longest



print(longest_palindromic_subsequence('abababaxb'))











