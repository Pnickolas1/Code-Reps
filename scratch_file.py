from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]




def two_number_sum(arr, number):

    nums = {}

    for num in arr:
        target = number - num
        if target in nums:
            return sorted(([num, target]))
        else:
            nums[num] = True

    return []


print(two_number_sum([2,5,0,10,3, 4, 2],50))