

"""
medium difficulty

two arrays find the pair of numbers, 1 number from each array, with the smallest
difference

time: O(n log(n)) + O(m log(m))
    - where n is the length of array1 and m is the length of array2
space: O(1)

1. sort both arrays in ascend order before we do anything
2. take advantage of a sorted arrays


"""

def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    idxOne = 0
    idxTwo = 0

    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idxOne < len(arr1) and idxTwo < len(arr2):
        firstNum = arr1[idxOne]
        secondNum = arr2[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


one = [-1, 5, 10, 20, 3]
two = [26, 134, 135, 15, 17]

print(smallest_difference(one, two))