def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


def updateThreeLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def threeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateThreeLargest(threeLargest, num)
    return threeLargest




print(threeLargestNumbers([10, 3, 4, 12, 1, 6, 8, 9 , 15, 21, 2]))