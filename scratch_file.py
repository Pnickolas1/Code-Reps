arr = [1,2,3,4,5,6,7,8,9,10]

def binary_search_iter(arr, item):

    found = False
    first = 0
    last = len(arr) - 1

    while first <= last and not found:

        mid = int((first + last) /2)
        if item == arr[mid]:
            print(False)

        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    print(found)

binary_search_iter(arr, 10)
