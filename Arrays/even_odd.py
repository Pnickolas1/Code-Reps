

# when working with arrays, take advantage of the fact you operate on both ends
# efficiently


# given an array of ints, sort evens first then odds
x = [2, 3, 7, 5, 10, 14, 15, 22, 27, 31]
print(len(x))


def even_odd(arr):
    next_even = 0
    next_odd = len(arr) -1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

    return arr


if __name__ == "__main__":
    print(len(x))
    print(even_odd(x))


