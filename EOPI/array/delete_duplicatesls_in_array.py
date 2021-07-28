




def delete_duplicates(arr):

    if not arr:
        return 0

    write_index =1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            wi = arr[write_index - 1]
            Ith = arr[i]
            print(write_index)
            arr[write_index] = arr[i]
            write_index += 1
    print(arr)
    print(arr[:write_index])
    return write_index

x = [0, 1, 2, 3, 3, 4, 6, 7, 7, 7, 8, 9, 10, 10, 10, 12]

print(print(delete_duplicates(x)))