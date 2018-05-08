

def highest_product_of_three(inputs):

    # edge case
    if len(inputs) < 3:
        raise ValueError('this is an error')

    # storage and setup
    highest_product_of_3 = inputs[0] * inputs[1] * inputs[2]
    highest_product_of_2 = inputs[0] * inputs[1]
    lowest_product_of_2 = inputs[0] * inputs[1]
    highest = max(inputs[0], inputs[1])
    lowest = min(inputs[0], inputs[1])

    # iterate through
    for i in xrange(2, len(inputs)):
        current = inputs[i]
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2,
                                   )
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest,
                                   )
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest,
                                  )
        highest = max(current, highest )
        lowest = min(lowest, current)

    print highest_product_of_3

inps = [-1, 5, 10, 4]
highest_product_of_three(inps)
