


nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]

def searchRange_double_binary_seaarch(nums, target):
    def binarySearchLeft(A, x):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if x > A[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binarySearchRight(A, x):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if x >= A[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return [left, right] if left <= right else [-1, -1]
