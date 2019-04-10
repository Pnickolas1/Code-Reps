

def delete_duplicates(arr):

    if not arr:
        return 0

    write_index =1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index


print(delete_duplicates([1,3, 3, 5, 6, 7, 7, 7, 9, ]))
