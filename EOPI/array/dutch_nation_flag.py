


"""

Dutch National Flag problem

what this really means, is given a index value, or a num:int , sort the array
in values less than the pivot/idx value, equal to index value, and greater than value

you should be able to do this in place

"""


def dutchNationalFlag(arr, idx):

    value = arr[idx]

    leftIdx = 0
    for i in range(len(arr)):
        if arr[i] < value:
            arr[i], arr[leftIdx] = arr[leftIdx], arr[i]
            leftIdx += 1


    lastIdx = len(arr) - 1

    for i in reversed(range(leftIdx, len(arr) - 1)):
        if arr[i] > value:
            arr[i], arr[lastIdx] = arr[lastIdx], arr[i]
            lastIdx -= 1

    return arr

x = [0, 1, 2, 2, 2, 1, 0, 2, 0, 2, 1]

print(dutchNationalFlag(x, 1))
