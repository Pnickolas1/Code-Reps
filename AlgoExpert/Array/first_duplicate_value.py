



"""
first duplicate value:
medium



"""

def firstDuplicateValue(arr):
    seen = set()

    for i, item in enumerate(arr):
        if item in seen:
            return item
        seen.set(item)
    return -1

def firstDuplicateValue(arr):
    for item in arr:
        absValue = abs(item)
        if arr[absValue - 1] < 0:
            return absValue
        arr[absValue - 1] *= -1
    return -1