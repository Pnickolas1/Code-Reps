import math

"""
checking if a integer is a palindrome can be 2 waysL

Optimal:
space: O(1)
time:: O(n)

1. way, reverse the integer, and then compare to the given parameter
2. iterate through through the param, popping off the most significant int, and the 
   least significant digit, comparing, if they dont match, return false, 
   if they do match, remove the most/least significant arg and continue

   edge case, if the given arg is less than 0


"""

def is_number_palindrome(x):

  if x < 0:
    return False

  num_digits = math.floor(math.log10(x)) + 1
  msd_mask = 10**(num_digits - 1)
  for i in range( num_digits // 2):

    if x // msd_mask != x % 10:
      return False
    
    x %= msd_mask
    x //= 10
    msd_mask //= 100
  return True


print(is_number_palindrome(12321))

