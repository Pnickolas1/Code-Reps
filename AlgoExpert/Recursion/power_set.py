"""
powerset - medium
a powerset is a math "thing", the set of all subsets of another
set.



Time: O(2 ^ n * n/2) => converges to O(2 ^n)
"""

def powerset_iterative(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets



# Time: O(n*2^n)
# Space: O(n*2^n)
def powerset(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        currentSubsets = subsets[i]
        subsets.append(currentSubsets + [ele])
    return subsets

