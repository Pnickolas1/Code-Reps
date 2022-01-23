import heapq

"""

kth largest in stream

easy


Can add elements and remove the smallest (min-heap) or largest (max-heap) element in O(\log(n))O(log(n)).

The capability to remove and insert elements in \log(n)log(n) time makes heaps extremely useful


"""




class KthLargestInStream:

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]