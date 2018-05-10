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


# recursive binary search

def recur_binary_search(arr, item):

    # base case
    if len(arr) == 0:
        print False

    else:
        midpoint = len(arr) / 2

        if arr[midpoint] == item:
            print True

        else:
            if item < arr[midpoint]:
                return recur_binary_search(arr[:midpoint], item)
            else:
                return recur_binary_search(arr[midpoint + 1:], item)



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rec_bin_search(arr, 12)
binary_search_iter(arr, 35)
