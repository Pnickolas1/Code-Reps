arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 23, 24, 26, 29, 30, 35]
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
nums = [3, 4, 6]
inps = [-1, 5, 10, 4]
times = [(4, 8), (10, 12), (9, 10), (3, 5), (0, 1)]
random_numbers = [98,24,40,23,44,19,8,31,31,8,38,0,35,50,3,45,44,41,5,16,29,25,25,32,25,20,34,36,3,19]


def selection_sort(arr):

    for fillslots in range(len(arr) -1, 0, -1):

        position_of_max = 0

        for item in range(1, fillslots +1):

            if arr[item] > arr[position_of_max]:
                position_of_max = item

        temp = arr[fillslots]
        arr[fillslots] = arr[position_of_max]
        arr[position_of_max] = temp

    print(arr)

selection_sort(random_numbers)


def binary_search_recur(arr, item):

    # base case
    if len(arr) == 0:
        print False

    else:
        midpoint = (len(arr) -1 )/2

        if item == arr[midpoint]:
            print True

        else:
            if item < arr[midpoint]:
                return binary_search_recur(arr[:midpoint], item)
            else:
                return binary_search_recur(arr[midpoint +1:], item)

binary_search_recur(arr, 1)

def bubble_sort(arr):

    for x in range(len(arr)-1, 0, -1):
        for n in range(x):
            if arr[n] > arr[n+1]:
                temp = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = temp

    print(arr)

bubble_sort(random_numbers)




