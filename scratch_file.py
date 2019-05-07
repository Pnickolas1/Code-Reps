from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

"""

space: O(n)
time: O(n)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
196418, 317811,
"""


def three_number_sum(arr, target):
    triplets = []
    arr.sort()

    for i in range(len(arr) - 2):
        leftIdx = i + 1
        rightIdx = len(arr) - 1
        while leftIdx < rightIdx:
            currentSum = arr[i] + arr[leftIdx] + arr[rightIdx]
            if currentSum == target:
                triplets.append([arr[i], arr[leftIdx], arr[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif currentSum < target:
                leftIdx += 1
            elif currentSum > target:
                rightIdx -= 1
    return triplets

print(three_number_sum([3, 5, 10, 3, ]))

