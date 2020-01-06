
def index_equals_value_search(arr):
    """
    - sorted *
    - minValue = float('inf')
    """
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2

        if arr[mid] - mid < 0:
            first = mid + 1

        elif (arr[mid] - mid == 0) and ((mid == 0) or (arr[mid - 1] - (mid - 1) < 0)):
            return mid
        else:
            last = mid - 1
    return -1

arr = [-5,0,2,3,10,29]

print(index_equals_value_search(arr))



def tet(arr):

    first = 0
    last = len(arr) -1

    while first <= last:

