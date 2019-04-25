


"""
two number sum
time: O(n)
space: O(n)
"""

def twoNumberSum(array, targetSum):

    nums = {}

    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return sorted([potentialMatch, num])
        else:
            nums[num] = True

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))

