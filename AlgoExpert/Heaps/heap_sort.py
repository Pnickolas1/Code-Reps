"""
Heap Sort:

its O(1) space
-practically very slow due to cache-inefficiency

Mian Advantages:
- great worst case runtime O(n * log (n)) regardless of input data
- relies heavily on heap data structure (a common implementation of a Priority Queue)


- in place algorithm
- unstable - does not* maintain the relative order of elements with equal values
-



the heap data structure:

- heaps are useful when keeping track of samallest element (min heap), the similarly, a max heap, tracking the
largest element

- a tree based data structure, where every node is smaller than all of its children



- you can only delete the first element in a heap, after it is then resorted.
- heaps naturally "re-sort" themselves after an element is added or removed, so that the smallest element is always in
the first position

- a heap is utilized when performing a heap sort, because the root node is the next smallest element




heapq:
heap queue algorithm, also known as the priority queue algorithm.

"""


from heapq import heappop, heappush

def heap_sort(arr):
    heap = []
    for element in arr:
        heappush(heap, element)
        print(heap)


    ordered = []
    while heap:
        ordered.append(heappop(heap))

    return ordered

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]

heap_sort(array)