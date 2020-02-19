
import pprint
import sys
x = [8, 12, 2, 3, 15, 5, 7]
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
z = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
sampleInput = [[1,3,4,10],
               [2,5,9,11],
               [6,8,12,15],
               [7,13,14,16]]
wordbank = ['this', 'that', 'apple', 'is', 'apology']

def lowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    numberImportantReports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numberImportantReports += orgInfo.lowestCommonManager
    if manager == reportOne or manager == reportTwo:
        numberImportantReports += 1
    lowestCommonManager = manager if numberImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numberImportantReports)

class OrgInfo:
    def __init__(self, lowestCommonManager, numberImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numberImportantReports
