# write a function that, given
    # an amount of money
    # a list of coin demoniations

# computes the number of ways to make the amount of money with coins of the available


def change_possibilities_bottom_up(amount, denominations):

    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:

        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]


    print '# of Possibilities: ', ways_of_doing_n_cents[amount]

coins = [1,3,5]
amount = 5

change_possibilities_bottom_up(amount, coins)



# take aways: Dynamic Programming
# bottom up algorithm: avoid recursive approach and ultimately the potential to build up a large call stack that
# could cause a `stack overflow error`
#

