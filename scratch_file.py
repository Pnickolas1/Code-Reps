from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

randoms = [45, 44, 41, 5, 16, 29, 25, 25, 32]

"""

space: O(n)
time: O(n)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
196418, 317811,
"""

def getNthFib(n):

    firstTwo = [0, 1]
    counter = 3

    while counter <= n:
        nextFib = firstTwo[0] + firstTwo[1]
        firstTwo[0] = firstTwo[1]
        firstTwo[1] = nextFib
        counter += 1
    return firstTwo[1] if n > 1 else firstTwo[0]

print(getNthFib(10))