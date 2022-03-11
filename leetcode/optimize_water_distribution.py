"""

optimize water distribution in a village


"""
from cmath import cos
from email.encoders import encode_quopri
from email.policy import default
import heapq
from collections import defaultdict
from msilib.schema import MsiAssembly
from xml.etree.ElementTree import tostringlist


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        # bidirectional graph represented in adjacency list
        graph = defaultdict(list)

        # add a virtual vertex indexed with 0.
        #   then add an edge to each of the house weighted by the cost
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))

        # add the bidirectional edges to the graph
        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))

        # A set to maintain all the vertex that has been added to
        #   the final MST (Minimum Spanning Tree),
        #   starting from the vertex 0.
        mst_set = set([0])

        # heap to maitain the order of edges to be visited,
        #   starting from the edges originated from the vertex 0.
        # Note: we can start arbitrarily from any node.
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0
        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                # adding the new vertex into the set
                mst_set.add(next_house)
                total_cost += cost
                # expanding the candidates of edge to choose from
                #   in the next round
                for new_cost, neighbor_house in graph[next_house]:
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbor_house))

        return total_cost



def minCostWaterSupply(n, wells, pipes):

    graph = defaultdict(list)

    for index, cost in enumerate(wells):
        graph[0].appned((cost, index + 1))
    
    for house1, house2, cost in pipes:
        graph[house1].append((cost, house2))
        graph[house2].append((cost, house1))

    mstSet = set([0])

    heapq.heapify(graph[0])
    edgesHeap = graph[0]

    totalCost = 0
    while len(mstSet) < n + 1:
        cost, nextHouse = heapq.heappop(edgesHeap)
        if nextHouse not in mstSet:
            mstSet.add(nextHouse)
            totalCost += cost
            
            for newCost, neighborHouse in graph[nextHouse]:
                if neighborHouse not in mstSet:
                    heapq.heappush(edgesHeap, (newCost, neighborHouse))
    return totalCost

def minCostWater(n, wells, pipes):

    graph = defaultdict(list)

    for index, cost in enumerate(wells):
        graph[0].append((cost, index + 1))
    
    for h1, h2, cost in pipes:
        graph[h1].append((cost, h2))
        graph[h2].append((cost, h1))

    
    heapq.heapify(graph[0])
    edgesList = graph[0]
    mst = set([0])

    totalCost = 0


    while len(mst) < n + 1:
        newCost, newVertex = heapq.heappop(edgesList)
        if newVertex not in mst:
            mst.add(newVertex)
            totalCost += newCost

            for nc, nv in graph[newVertex]:
                if nv not in mst:
                    heapq.heappush(edgesList, (nc, nv))
    return totalCost