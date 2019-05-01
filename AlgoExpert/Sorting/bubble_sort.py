random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]
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

print(bubble_sort(random_numbers))