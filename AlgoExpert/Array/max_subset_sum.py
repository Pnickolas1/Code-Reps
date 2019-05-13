"""
medium

max subset sum no adjacent elements

given an array of only positive integers find the greatest sum you can generate without adding up
2 numbers that are positioned next to eachother in the array

[7, 10, 12, 7, 9, 14]

solution is = 7 + 12 + 14 = 33

dynamic programming, solving smaller problems, to build up into our final solution



** always be sure to say what N ids ! **
time: O(n) , n is the length of the input array
space: O(n) space
"""


def maxSubsetSumNoAdjacent(array):
    """
    time: O(n) , n is the length of the input array
    space: O(n) space
    :param array:
    :return:
    """

    if not len(array):
        return False
    elif len(array) == 1:
        return array[0]

    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i -1], maxSums[i - 2] + array[i])
    return maxSums[-1]

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))


def maxSubsetSum_optimal(array):
    """
    time: O(n)
    space: O(1)
    :param array:
    :return:
    """
    if not len(array):
        return False
    elif len(array) == 1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


print(maxSubsetSum_optimal([75, 105, 120, 75, 90, 135]))

