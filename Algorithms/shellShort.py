random_numbers = [98,24,40,23,44,19,8,31,31,8,38,0,35,50,3,45,44,41,5,16,29,25,25,32,25,20,34,36,3,19]

def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):

        currentValue = arr[i]
        position = i

        while position >= gap and arr[position - gap] > currentValue:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = currentValue


def shell_sort(arr):

    sublistcount = len(arr) / 2

    while sublistcount > 0:
        for start in range(sublistcount):
            try:
                gap_insertion_sort(arr, start, sublistcount)
            except SyntaxError:
                pass

        sublistcount = sublistcount / 2
    print(arr)



shell_sort(random_numbers)