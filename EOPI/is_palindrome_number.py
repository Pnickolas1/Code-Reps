import math

def is_palindrome_number(x):
    if x < 0:
        return False
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= 10
        x //= msd_mask
        msd_mask //= 100
    return True



print(is_palindrome_number(234432))
print(is_palindrome_number(153351))