
""""
write a program that takes an array of digits encoding a decimal integer D and
updates the array to represent D + 1
[1,2,9] should return [1,3,0]

algorithm should work even if the language has finite precision arithmetic
"""

# 1.
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i -1] += 1
    if arr[0] == 10:
        # need additional digit as the most significant digit (i e arr[0] has a carryout
        arr[0] = 0
        arr.inser(0, 1)

    return arr


# 2.
def plus_one_test(arr):
    arr[-1] += 1
    for i in range(len(arr) -1, 0, -1):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i -1] += 1
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0, 1)
    return arr

print(plus_one_test([9,9,9]))





def plus_one_brute_force(arr):
    number = int(''.join(map(str, arr))) + 1
    return [int(num) for num in str(number)]