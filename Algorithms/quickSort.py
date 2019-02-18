
def quick_sort(arr):

    quick_sort_help(arr ,0 ,len(arr ) -1)
    print(arr)

def quick_sort_help(arr ,first ,last):

    if first< last:
        splitpoint = partition(arr, first, last)

        quick_sort_help(arr, first, splitpoint - 1)
        quick_sort_help(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

random_numbers = [24,40,23,98,44,19,8,31,31,8,38,0,35,50,3,45,44,41,5,16,29,25,25,32,25,20,34,36,3,19]

quick_sort(random_numbers)

from random import randint


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
    for index in xrange(start, end):
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
# X=[0, 3, 4, 4, 4, 5, 6, 7, 22, 45, 82]