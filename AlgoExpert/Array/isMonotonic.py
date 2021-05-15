

"""

isMonotonic Array







"""

def isMonotonic(arr):
    isNonIncreasing = True
    isNonDecreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            isNonIncreasing = False
        if arr[i] > arr[i - 1]:
            isNonDecreasing = False
    return isNonIncreasing or isNonDecreasing
``