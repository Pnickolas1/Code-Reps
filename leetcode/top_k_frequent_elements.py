from collections import Counter
import heapq
from re import L


"""

Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.


# only min heaps are implementeed in heapq

"""

def topKFrequent(nums, k):

    if k == len(nums):
        return nums

    counterOfnums = Counter(nums)

    q = []
    heapq.heapify(q)
    
    for i, item in enumerate(counterOfnums.items()):
        num, ctOfNum = item

        # min heap only, 3 * -1 = -3
        heapq.heappush(q, (ctOfNum * -1, num))
    
    ans = []

    for i in range(k):
        ctOfNum, num = heapq.heappop(q)
        ans.append(num)
    
    return ans

z = [1,1,1,2,2,3]
x = 2


print(topKFrequent(z, x))