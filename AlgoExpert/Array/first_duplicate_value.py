



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

