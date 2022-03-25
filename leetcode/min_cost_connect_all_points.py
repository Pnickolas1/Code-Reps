

"""
  minimum cost to connect all points

  MST - or Minimum Spanning Tree

  - 1584 minimum cost to connect all points

  prims algorithm

  graph
  heap (min Heap)
    purpose, connect all nodes, DO NOT form a cycle


"""
import heapq

def min_cost_to_connect_all_points(points):
    N = len(points)

    adj = { i: [] for i in range(N) }

    # pre work
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])
    

    # Prims Algorithm
    res = 0
    visit = set()
    minH = [[0, 0]]
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCos, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, (neiCos, nei))
    return res