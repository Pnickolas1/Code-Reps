


"""

running sum
"""


def runnningProductsum(arr):

    left = [1 for x in arr]
    right = [1 for x in arr]

    leftRunningTotal = 1

    for i in range(len(arr)):
        left[i] = leftRunningTotal
        leftRunningTotal = arr[i] * leftRunningTotal
    
    rightRunningTotal = 1
    for i in reversed(range(len(arr))):
        right[i] = rightRunningTotal 
        rightRunningTotal = arr[i] * rightRunningTotal

    for i in range(len(arr)):
      left[i] = left[i] * right[i]


    return left