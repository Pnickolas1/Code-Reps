
"""
sort a list of numbers


time: O(n^2)
 * best case O(n)
space: O(1)

bubble sort occurs inplace
the last number is in the final position


"""


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def bubble_sort(array):

    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) -1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
    return array