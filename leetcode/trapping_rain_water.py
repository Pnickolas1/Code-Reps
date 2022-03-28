
"""

  trapping rain water


"""

def trapping_rain_Water(heights):

    if len(heights) == 0:
        return 0
    
    elif len(heights) == 1:
        return 0

    
    leftIdx = 0
    rightIdx = len(heights) - 1

    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]


    surfaceArea = 0

    while leftIdx < rightIdx:
        if heights[leftIdx] < heights[rightIdx]:
            leftIdx += 1
            leftMax = max(leftMax, heights[leftIdx])
            surfaceArea += leftMax - heights[leftIdx]
        else:
            rightIdx -= 1
            rightMax = max(rightMax, heights[rightIdx])
            surfaceArea += rightMax - heights[rightIdx]
    return surfaceArea


