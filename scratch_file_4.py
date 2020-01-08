


x = [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]
y = [4, 9]

def isOutOfOrder(arr, idx, num):
    if idx == 0:
        return num > arr[idx + 1]
    elif idx == len(arr) - 1:
        return num < arr[idx - 1]
    return num < arr[idx - 1] or num > arr[idx + 1]

def subArraySort(arr):
    minValueOutOfOrder = float('inf')
    maxValueOutOfOrder = float('-inf')

    for i, num in enumerate(arr):
        if isOutOfOrder(arr, i, num):
            minValueOutOfOrder = min(minValueOutOfOrder, num)
            maxValueOutOfOrder = max(maxValueOutOfOrder, num)

    if minValueOutOfOrder == float('inf'):
        return [-1, -1]


    left = 0

    while minValueOutOfOrder >= arr[left]:
        left += 1

    right = len(arr) -1
    while maxValueOutOfOrder <= arr[right]:
        right -= 1

    return [left, right]


print(subArraySort(x))