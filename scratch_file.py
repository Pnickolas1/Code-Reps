from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def partition(arr, start, end):

    pivot = randint(start, end)
    temp = arr[end]
    arr[end] = arr[pivot]
    arr[pivot] = temp
    pindex = start

    for i in range(start, end):
        if arr[i] <= arr[end]:
            temp = arr[i]
            arr[i] = arr[pindex]
            arr[pindex] = temp
            pindex += 1
    temp1 = arr[end]
    arr[end] = arr[pindex]
    arr[pindex] = temp1
    return pindex

def quicksort(arr, start, end):

    if start < end:
        pindex = partition(arr, start, end)
        quicksort(arr, start, pindex -1)
        quicksort(arr, pindex +1, end)
    return arr



if __name__ == "__main__":
    print(quicksort(random_numbers, 0, len(random_numbers) -1))

