# iterative
def binary_search_iter(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:

        mid = (first + last) / 2

        if arr[mid] == ele:
            found = True

        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


# recursive binary search

def recur_binary_search(arr, item):

    # base case
    if len(arr) == 0:
        return False

    else:
        midpoint = len(arr) / 2

        if arr[midpoint] == item:
            return True

        else:
            if item < arr[midpoint]:
                return recur_binary_search(arr[:midpoint], item)
            else:
                return recur_binary_search(arr[midpoint + 1:], item)



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recur_binary_search(arr, 12)
binary_search_iter(arr, 35)


def find_duplicates(arr1, arr2):
    duplicates = []

    while arr1 and arr2:
        arr1_ = arr1[0]
        if arr1_ < arr2[0]:
            arr1.pop(0)
        elif arr1_ > arr2[0]:
            arr2.pop(0)
        else:
            duplicates.append(arr1_)
            arr1.pop(0)
            arr2.pop(0)
    return duplicates
