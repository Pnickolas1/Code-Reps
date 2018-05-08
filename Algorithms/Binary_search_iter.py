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

    print found


# recursive implementation
def rec_bin_search(arr, ele):
    # base case
    if len(arr) == 0:
        return False

    else:
        mid = len(arr) / 2

        if arr[mid] == ele:
            return True

        else:
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)


            else:
                return rec_bin_search(arr[mid + 1:], ele)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rec_bin_search(arr, 12)
binary_search_iter(arr, 35)
