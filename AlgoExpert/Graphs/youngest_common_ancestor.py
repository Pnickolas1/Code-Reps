"""
youngest common ancestor: medium

given 3 inputs, first is the top ancestor of some sort of ancestoral tree, the other 2 are descendants

graph problem, but more importantly, notice this is a tree, because there is a distinct flow of
relations, top down

time: O(d) d is depth of the lowest descendant
space: O(1) , we can do this iteratively

"""


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant

def getYoungestCommonAncestor(topAncestor, descandantOne, descendantTwo):
    depthOne = getDescendantDepth(descandantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descandantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descandantOne, depthTwo - depthOne)