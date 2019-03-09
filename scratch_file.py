from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def quicksort(arr, start, end):

    if start < end:
        pIndex = partition(arr, start, end)
        quicksort(arr, start, pIndex -1)
        quicksort(arr, pIndex + 1, end)
    return arr


def partition(arr, start, end):

    # gettting a random integer from the index range of start and end
    pivot = randint(start, end)

    # setting temp as the last item in the array
    temp = arr[end]

    # overwriting the last item in the array w/ the pivot index's value
    arr[end] = arr[pivot]

    # overwrite the location of the pivot index with the last item in the array
    arr[pivot] = temp

    # starting point, the first item in the array
    pIndex = start

    for i in range(start, end):
        if arr[i] <= arr[end]:
            temp = arr[i]
            arr[i] = arr[pIndex]
            arr[pIndex] = temp
            pIndex += 1
    temp1 = arr[end]
    arr[end] = arr[pIndex]
    arr[pIndex] = temp1

    return pIndex


print(quicksort(random_numbers, 0, len(random_numbers) -1))
2