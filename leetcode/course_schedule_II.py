from collections import defaultdict

"""

  course schedule II

time : O(e + v)
space: O(e + v)

"""

WHITE = 1
GRAY = 2
BLACK = 3

def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    # Create the adjacency list representation of the graph
    prereq = { c:[] for c in range(numCourses) }
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if dfs(pre) == False:
                return False
        
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []
    return output