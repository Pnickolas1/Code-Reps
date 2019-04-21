from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                  45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

def quick_sort(a):
    inPlaceQuickSort(a, 0,  len(a) -1)

def inPlaceQuickSort(A, start, end):
    if start < end:
        pivot = randint(start, end)
        temp = A[end]
        A[end] = A[pivot]
        A[pivot] = temp

        p = inPlacePartition(A, start, end)
        inPlaceQuickSort(A, start, p - 1)
        inPlaceQuickSort(A, p + 1, end)


def inPlacePartition(A, start, end):
    pivot = randint(start, end)
    temp = A[end]
    A[end] = A[pivot]
    A[pivot] = temp
    newPivotIndex = start - 1
    for index in range(start, end):
        if A[index] < A[end]:  # check if current val is less than pivot value
            newPivotIndex = newPivotIndex + 1
            temp = A[newPivotIndex]
            A[newPivotIndex] = A[index]
            A[index] = temp
    temp = A[newPivotIndex + 1]
    A[newPivotIndex + 1] = A[end]
    A[end] = temp
    return newPivotIndex + 1


X = [4, 5, 7, 4, 3, 6, 0, 4, 22, 45, 82]
inPlaceQuickSort(X, 0, len(X) - 1)

print('pre sort', random_numbers)
quick_sort(random_numbers)
print(random_numbers)

# this is another way


def quicksort(alist, start, end):
    '''This function calls the partition and then recurse itself using the index returned by partition'''
    if start < end:
        pIndex = partition(alist, start, end)
        quicksort(alist, start, pIndex - 1)
        quicksort(alist, pIndex + 1, end)

    return alist


def partition(alist, start, end):
    """
    This function will devide the list in two halves wrt pivot
    This will return the index of pivot after deviding
    """
    pivot = randint(start, end)
    temp = alist[end]
    alist[end] = alist[pivot]
    alist[pivot] = temp
    pIndex = start

    for i in range(start, end):
        if alist[i] <= alist[end]:
            temp = alist[i]
            alist[i] = alist[pIndex]
            alist[pIndex] = temp
            pIndex += 1
    temp1 = alist[end]
    alist[end] = alist[pIndex]
    alist[pIndex] = temp1

    return pIndex

if __name__ == '__main__':
    list = [2, 5, 6, 8, 3, 7, 5, 6, 20, 100, 85, -20]
    print(quicksort(list, 0, len(list) - 1))