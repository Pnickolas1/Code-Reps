


""""
write a program that applies the permutation: perm to the the array: arr
"""


def apply_permutation(perm, arr):

    for i in range(len(arr)):
        next = i
        while perm[next] >= 0:
            arr[i], arr[perm[next]] = arr[perm[next]], arr[i]
            temp = perm[next]
            # subtracts len(perm) from an array in perm to make it negative
            # which indicates the corresponding move has been performed
            perm[next] -= len(perm)
            next = temp
        # restore permp;.0¬
    perm[:] = [a + len(perm) for a in perm]
    return arr

print(apply_permutation([2, 0, 1, 3], ['a', 'b', 'c', 'd']))

