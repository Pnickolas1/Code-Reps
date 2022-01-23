


"""
given a string, confirm the string is a valid 
palindrome if you are able to skip 1 char



"""

def validPalindrome(s):

    def is_Pal(l, r):
      while l < r:

          if s[l] != s[r]:
              return False
          l += 1
          r -= 1
      return True



    l = 0
    r = len(s) - 1

    while l < r:


        if s[l] != s[r]:
            return is_Pal(l + 1, r) or is_Pal(l, r - 1)
        l += 1
        r -= 1
  
    return True