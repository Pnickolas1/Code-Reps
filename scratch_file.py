import sys
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                  45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def selection_sort(arr):

    for fillslots in range(len(arr)- 1, 0, -1):

        position_of_max = 0

        for location in range(1, fillslots + 1):

            if arr[location] > arr[position_of_max]:
                position_of_max = location

        temp = arr[fillslots]
        arr[fillslots] = arr[position_of_max]
        arr[position_of_max] = temp

    return arr



print(selection_sort(random_numbers))



