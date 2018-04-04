# write a function that, given
    # an amount of money
    # a list of coin demoniations

# computes the number of ways to make the amount of money with coins of the available


class Change(object):

    def __init__(self):
        self.memo = {}

        def change_possibilities_top_down(self, amount_left, denominations, current_index= 0):
            