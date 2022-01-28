"""

lc - medium

minimum to connect sticks


"""
import heapq

def minCostToConnectSticks(sticks):

    if len(sticks) == 0:
        return 0

    pq = []
    for stick in sticks:
        heapq.heappush(pq, sticks)
    
    tc = 0
    while len(pq) > 1:
        s, ss = heapq.heappop(pq), heapq.heappop(pq)

        cost = s + ss
        tc += cost
        heapq.heappush(pq, cost)
    
    return tc