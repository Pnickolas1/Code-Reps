

"""

given integers in array, increment them by 1





"""

def plus_one(arr):

    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1

    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0, 1)

    return arr

print(plus_one([1, 4, 8]))







