

# given a list of integers, find the highest product you can get from three of integers

def highest_product_of_3(list_of_ints):

    # Edge case
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    # Store/ Setup
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Walk through items, starting at index 2
    for i in xrange(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    print highest_product_of_3

inps = [-1, 5, 10, 4]


highest_product_of_3(inps)0