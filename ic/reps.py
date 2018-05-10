arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 23, 24, 26, 29, 30, 35]
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
nums = [3, 4, 6]



def binary_search_iter(arr, ele):

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:

        mid = (first + mid) /2

        if arr[mid] == ele:
            found = True

        if ele < arr[mid]:
            last = mid - 1

        else:
            first = mid + 1

    print found


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






recur_binary_search(arr, 45)