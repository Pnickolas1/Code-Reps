
def binary_search(arr, term):
    return binary_search_helper(arr, 0, len(arr), term)

def binary_search_helper(arr, start, end, term):
    if end > start:
        middle_index = (end + start) // 2
        curr_middle = arr[middle_index]
        if curr_middle == term:
            return middle_index
        elif term < curr_middle:
            return binary_search_helper(arr, start, middle_index, term)
        elif term > curr_middle:
            return binary_search_helper(arr, middle_index + 1, end, term)
    return -1

def binary_search_applicable(arr):
    return binary_seach_applicable_helper(arr, 0, len(arr))

def binary_seach_applicable_helper(
    arr,
    start,
    end,
    min_val=None,
    max_val=None,
    results=set()
):
    if end > start:
        middle_index = (end + start) // 2
        curr_middle = arr[middle_index]
        if (
            (min_val is None or curr_middle > min_val) and
            (max_val is None or curr_middle < max_val)
        ):
            results.add(curr_middle)
            binary_seach_applicable_helper(
                arr,
                start,
                middle_index,
                min_val=min_val,
                max_val=curr_middle,
                results=results
            )
            binary_seach_applicable_helper(
                arr,
                middle_index + 1,
                end,
                min_val=curr_middle,
                max_val=max_val,
                results=results
            )
    return results

applicable = binary_search_applicable([7, 2, 3, 0, 5])
print(applicable)