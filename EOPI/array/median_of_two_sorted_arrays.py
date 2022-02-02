import math

"""
Median of two sorted arrays

O(log(min(n, m))




"""


def findMedianSortedArrays(nums1, nums2) -> float:
    # binary search on the smaller of the two arrays O(log(min(x, y)))
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    # nums1 will be shortest array
    m, n = len(nums1), len(nums2)

    left = 0
    right = m - 1

    while True:
        pointer1 = left + (right - left) // 2
        pointer2 = (m + n) // 2 - pointer1 - 2

        left1 = nums1[pointer1] if pointer1 in range(m) else -math.inf
        left2 = nums2[pointer2] if pointer2 in range(n) else -math.inf
        right1 = nums1[pointer1 + 1] if pointer1 + 1 in range(m) else math.inf
        right2 = nums2[pointer2 + 1] if pointer2 + 1 in range(n) else math.inf

        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return min(right1, right2)

        elif left1 > right2:
            right = pointer1 - 1
        else:
            left = pointer1 + 1