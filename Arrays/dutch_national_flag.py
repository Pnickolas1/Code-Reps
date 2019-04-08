
import os

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, arr):

    pivot = arr[pivot_index]

    # keep the following invariants during partitioning
    # bottom group: arr[:smaller]
    # middle group: arr[smaller: larger]
    # unclassified: arr[equal: larger]
    # top group: arr[larger:]
    smaller, equal, larger = 0, 0, len(arr)

    #keep iterating as long as there is an unclassified element
    while equal < larger:

        # arr[equal] is the incoming unclassified
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif arr[equal] == pivot:
            equal += 1
        else:   # arr[equal] > pivot
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]

    return arr

x = [12, 1, 1, 3, 9, 2, 4, 8, 13, 0, 6]

if __name__ == "__main__":
    print(os.path.basename(__file__))
    print(dutch_flag_partition(1, x))
