

"""
max sum increasing sub sequence: HARD



time: O(n^2)
space: O(n)

"""

x = [8, 12, 2, 3, 15, 5, 7]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i]= sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    print(sums)
    print(array)
    print(sequences)
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


print(maxSumIncreasingSubsequence(x))