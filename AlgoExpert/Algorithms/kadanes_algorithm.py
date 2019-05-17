"""
Kadanes Algorithm: medium
write a function that takes in a non-empty array of integers and returns
the maximum sum that can be obtained by summing up all the numbers
in a non-empty subarray of the input array. A subarrray must only
contain adjacent numbers:

sample input [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
sample output: 19    ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1])

** dynamic programming **

Space: O(1)
Time: O(n)

"""


def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar

print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))