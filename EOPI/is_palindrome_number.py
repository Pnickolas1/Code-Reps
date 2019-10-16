import math

def is_palindrome_numeber(x):
    if x < 0:
        return False

    num_digits = math.floor(math.log10(x)) + 1
    print('num_digits', num_digits)
    msd_mask = 10**(num_digits - 1)
    print(msd_mask)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask # remove the most significant digit of x
        x //= 10 # remove the least significant digit of x
    return True



print(is_palindrome_numeber(1234))