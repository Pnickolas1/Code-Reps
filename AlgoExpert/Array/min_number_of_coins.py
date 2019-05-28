"""
min number of coins: medium

"""


def minNumberofCoins(n, denoms):
    numberOfcoins = [float('inf') for amount in range(n +1)]
    numberOfcoins[0] = 0
    for denom in denoms:
        for amount in range(len(numberOfcoins)):
            if denom <= amount:
                numberOfcoins[amount] = min(numberOfcoins[amount],
                                            1 + numberOfcoins[amount - denom])
    return numberOfcoins[n] if numberOfcoins[n] != float('inf') else -1


print(minNumberofCoins(7, [1, 3, 5]))

print(minNumberofCoins(10, [1, 5, 10]))



