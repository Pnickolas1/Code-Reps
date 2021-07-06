

"""
facebook questions

total occurrence of k in a sort algorithm


memory - O(n)
runtime: O(n)


"""

x = [1, 2, 3, 5, 5, 5, 5, 8, 10, 12, 15, 19, 20, 21]

def isInBounds(arr, idx):
    if 0 < idx > len(arr) - 1:
        return False
    return True


def binarySearch(arr, left, right, k, type):

    if len(arr) == 0 or left > right:
        return -1

    midpt = left + (right - left) // 2

    if arr[midpt] == k:
        if type == 'FIRST':
            if isInBounds(arr, midpt - 1) and arr[midpt] == arr[midpt - 1]:
                return binarySearch(arr, left, midpt - 1, k, 'FIRST')

        elif type == 'LAST':
            if isInBounds(arr, midpt + 1) and arr[midpt] == arr[midpt + 1]:
                return binarySearch(arr, midpt + 1, right, k, 'LAST')

        return midpt
    elif arr[midpt] < k:
        return binarySearch(arr, midpt + 1, right, k, 'FIRST')
    else:
        return binarySearch(arr, left, midpt - 1, k, 'FIRST')

def occurrencesOfK(arr, k):

    firstOccurrence = binarySearch(arr, 0, len(arr) - 1, k, 'FIRST')

    if firstOccurrence == -1:
        return 0

    lastOccurrence = binarySearch(arr, 0, len(arr) - 1, k, 'LAST')

    return lastOccurrence - firstOccurrence + 1

print(occurrencesOfK(x, 5))



