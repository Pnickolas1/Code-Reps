

def selection_sort(arr):
    for fillslots in range(len(arr) - 1, 0, -1):
        position_of_max = 0

        for location in range(1, fillslots + 1):

            if arr[location] > arr[position_of_max]:
                position_of_max = location

        temp = arr[fillslots]
        arr[fillslots] = arr[position_of_max]
        arr[position_of_max] = temp

    print arr


arr = [5, 12, 8, 3, 10, 11]
selection_sort(arr)

