
"""
Remove Element

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

"""

def removeElement(arr, val):
    start = 0
    last = len(arr) - 1
    while start <= last:
        if arr[start] == val:
            arr[start] = arr[last]
            arr[last] = arr[start]
            last -= 1
        else:
            start += 1
    print(arr)
    return start


print(removeElement([1,2,3,4,5,5,6,5], 5))
