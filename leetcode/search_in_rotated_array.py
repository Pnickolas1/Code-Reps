

"""
leetcode 33: search in rotated array




"""


        
def searchRotatedArray(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:

        midpt = (l + r) // 2

        if target == nums[midpt]:
            return midpt

        # left sorted portion

        # 12, 13, 14, 15, 3, 4, 5, 6
        # 13


        # 5, 10, [1], 2, 3, 4
        # 3
        if nums[l] <= nums[midpt]:
            if target > nums[midpt] or target < nums[l]:
                l = midpt + 1
            else:
                r = midpt - 1
        else:
            if target < nums[midpt] or target > nums[r]:
                r = midpt - 1
            else:
                l = midpt + 1

    return -1



