"""

shifted binary search
* hard
* given a sorted array of integers and a target integer, the numbers have been shifted (rotated by some number)

[45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
33
output would be 8 (the idx the target resides in the array)

"""

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)


def shiftedBinarySearchHelper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    potentialMatch = array[middle]

    leftNum = array[left]
    rightNum = array[right]

    if target == potentialMatch:
        return middle

    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            return shiftedBinarySearchHelper(array, target, left, middle - 1)
        else:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
    else:
        if target > potentialMatch and target <= rightNum:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
        else:
            return shiftedBinarySearchHelper(array, target, left, middle - 1)

def shiftedBinarySearch(arr, target):
    return binary_search(arr, target, 0, len(arr) - 1)

def binary_search(arr, target, left, right):

    while left <= right:
        mid = (left + right) // 2
        leftNum = arr[left]
        rightNum = arr[right]
        potentialMatch = arr[mid]


        if target == potentialMatch:
            return mid
        if leftNum < potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > potentialMatch and target <= rightNum:
                left = mid + 1
            else:
                right = mid - 1
    return -1