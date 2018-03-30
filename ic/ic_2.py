
# You have a list of integers, and for each index you want to
# find the product of every integer except the integer at that index.

#greedy approach


nums = [3, 2, 5]

def get_products_of_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise ValueError('Need more integers in list')

    products_of_all_ints_except_at_index = len(int_list) * [None]

    product_so_far = 1

    for i in xrange(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]


    product_so_far = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    print products_of_all_ints_except_at_index



get_products_of_ints_except_at_index(nums)