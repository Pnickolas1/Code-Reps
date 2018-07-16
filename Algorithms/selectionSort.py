def selection_sort(arr):
    for fillslots in range(len(arr) - 1, 0, -1):
        print ('fillslots: '), fillslots

        position_of_max = 0

        for location in range(1, fillslots + 1):

            if arr[location] > arr[position_of_max]:
                print "Yes: ", arr[location], " > ", arr[position_of_max]
                print "arr[location]: ", arr[location]
                position_of_max = location

        temp = arr[fillslots]
        print "temp: ", temp
        print "arr: ", arr
        arr[fillslots] = arr[position_of_max]
        print "arr[fillslots]: ", arr[fillslots]
        arr[position_of_max] = temp
        print "arr 2: ", arr

    return arr


arr = [5, 8, 3, 10, 11]
selection_sort(arr)


