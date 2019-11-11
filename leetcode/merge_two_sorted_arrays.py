

"""
 Merge Sorted Arrays
"""

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def merge_two_sorted_arrays(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if len(nums2) == 0:
        return nums1
    length1 = len(nums1)
    j = 0
    i = 0
    while j <= n - 1:
        if nums1[i] >= nums2[j] or i > m - 1 + j:
            nums1.insert(i, nums2[j])
            del nums1[-1]
            j += 1
            i += 1
        else:
            i += 1
    return nums1


print(merge_two_sorted_arrays(nums1, m, nums2, n))