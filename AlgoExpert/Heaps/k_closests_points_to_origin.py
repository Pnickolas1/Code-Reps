
"""
k closest points to origin

use a max heap!

max heap will place the max value at the top, so you know which one to eject


--- why dist is made negative?
what @TurtleShip is trying to explain below is minheap and maxheap

minheap: when pop, we will get the smallest value. In this problem, is the shortest
maxheap: when pop, we will get the largest value. In this problem, is the longest.

In python, heapq is implemented as minheap. Therefore, if we pop, we will get the smallest number which we don't want,
we want to keep the smallest values to return later.
TutleShip used a trick by adding negative so the largest number becomes smallest so we can use minheap as is. [1,999] -> [-1,-999]

hope my explanation helped.

"""
import heapq

def kClosestToOrigins(points, k):

    heap = []

    for (x, y) in points:
        dist = -(x*x + y*y)
        print(dist)
        if len(heap) == k:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))

    print(heap)

    return [(x, y) for (dist, x, y) in heap]


x = [[1,3],[-2,2], [4, 5], [8, 8], [6, 12]]
y = 3
print(kClosestToOrigins(x, y))

