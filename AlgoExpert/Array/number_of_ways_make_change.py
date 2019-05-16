

"""
medium:  number of ways to make change.

dynamic programming

target amount of money, dollars our currency and coin denominations at our disposal
$ 10, given [1, 5, 10, 25] return 4

space: O(n)
time: O(nd) - n is the target amount, d is number of coin denominations
"""

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]
