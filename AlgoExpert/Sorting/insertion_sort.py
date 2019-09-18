
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

"""

space: O(1) inplace
time: O(n^2)


"""

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def insertion_sort(array):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j -1]:
            swap(j, j-1, array)
            j -= 1
    return array

print(insertion_sort(random_numbers))