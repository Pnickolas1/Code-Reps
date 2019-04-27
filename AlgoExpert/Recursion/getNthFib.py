


"""
memoized version
time: O(n)
space: O(n)


iterative approach
time: O(n)
space: O(1)

fibs =>

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
196418, 317811,
"""



#memoize versions
def getNthFib_memoize(n, memoize = {1: 0, 2: 1}):

    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib_memoize(n -1, memoize) + getNthFib_memoize(n-2, memoize)
        return memoize[n]

print(getNthFib_memoize(11))



# iterative approach
def getNthFib_iterative(n):

    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[1] + lastTwo[0]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


print(getNthFib_iterative(11))o