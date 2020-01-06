"""
what did i learn

lookup in a set is O(1)



"""




def getting_different_number(arr):
    items = set(arr)
    for i in range(len(arr)):
        if i not in items:
            return i
    return len(arr)


arr = [0, 1, 2, 3]

print(getting_different_number(arr))



"""
more efficeint 
"""
def getDifferentNumber(arr):
    function
    getDifferentNumber(arr):
    n = arr.length
    temp = 0

    # put each number in its corresponding index, kicking out
    # the original number, until the target index is out of range.
    for i from 0 to n-1:
        temp = arr[i]
        while (temp < n AND arr[temp] != temp):
            swap(temp, arr[temp])

    for i from 0 to n - 1:
        if (arr[i] != i):
            return i  # i isn’t in arr, hence we can return it

    # we got here since every number from 0 to n-1 is in arr.
    # By definition then, n isn’t in arr. Otherwise, the size of arr
    # would have been n+1 and not n.
    return n