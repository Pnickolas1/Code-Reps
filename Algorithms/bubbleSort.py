def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        print "setup: ", range(len(arr) - 1, 0, -1)
        print 'this is the n: ', n

        for k in range(n):
            print 'this is the k index check: ', k
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp
                print arr

    return arr


arr = [5, 3, 7, 2]
bubble_sort(arr)
