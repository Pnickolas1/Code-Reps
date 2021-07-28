



"""

Merge overlapping intervals



"""


intervals = [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]


def merge_overlapping_intervals(intervals):

    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    updatedIntervals = []

    currentInterval = sortedIntervals[0]
    updatedIntervals.append(currentInterval)

    for i in range(1, len(sortedIntervals)):
        nextInterval = sortedIntervals[i]
        start, end = nextInterval

        if currentInterval[1] >= start:
            currentInterval[1] = max(currentInterval[1], end)
        else:
            updatedIntervals.append(nextInterval)
            currentInterval = nextInterval

    return updatedIntervals

print(merge_overlapping_intervals(intervals))
