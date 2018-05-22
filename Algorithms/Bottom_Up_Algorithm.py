

# Bottom up algorithms offer another option in solving a problem. Bottom up algorithms are often used instead of a
# recursive approach. While recursion offers highly readable, succinct code, it is succeptible to a high memory cost
# O(n) and could lead to a stack overflow.

# recursion starts from the "end and works it's way back" (hence the need for a base case)
# bottom up algorithms start from the bottom (or start) and work their way up

# going bottom up is a common strategy for dynamic programming
# dynamic programming are coding problems where the solution is composed of solutions to the same problem with
# smaller inputs
# the other common strategy is memoization

# recursive approach
def product_1_to_n(n):
    # we assume n >= 1
    return n * product_1_to_n(n - 1) if n > 1 else 1


# to avoid this we can use a bottom up approach
def product_1_to_n_bottom_up(n):

    # we assume n >= 1
    result = 1
    for num in range(1, n + 1):
        result *= num

    print result


product_1_to_n(15)

product_1_to_n_bottom_up(15)