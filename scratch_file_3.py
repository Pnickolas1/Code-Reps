





def kadaneAlgo(arr):
    addAndIterate = arr[0]
    maxSoFar = arr[0]
    for i in range(1, len(arr)):
        addAndIterate = max(arr[i] , addAndIterate + arr[i])
        maxSoFar = max(maxSoFar, addAndIterate)
    return maxSoFar