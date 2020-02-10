 """
Min Number of Jumps - HARD

Time: O(n)
Space: O(1)

x = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
"""

def minNumberOfJums(array):
    """
    time: O(n^2)
    space: O(n)
    :param array:
    :return:
    """
    jumps = [float('inf') for a in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j] + 1, jumps[i])
    return jumps[-1]


def minNumberOfJumps_optimal(array):
    """
    Time: O(n)
    Space: O(1)
    :param array:
    :return:
    """
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1

