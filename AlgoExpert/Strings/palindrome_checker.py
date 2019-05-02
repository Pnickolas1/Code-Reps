

"""
 - many ways to do this problem

 recursive approach adds frame to the call stack and keeps
 the space at O(N), (aside* lookup tail recursion and how that
 can be leveraged to reduce the space to O(1)

"""


"""
space: O(n) time: O(n^2)

O(N^2) time because everytime we loop through
we're creating a new string which increases time

"""

def isPalindrome(string):
    reverseString = ""
    for i in reversed(range(len(string))):
        reverseString += string[i]
    return string == reverseString


"""
time: O(n) || space: O(n)

"""
def isPalindrome_array(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

"""
time: O(n)
space: O(n)
"""
def isPalindrime_recursive(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrime_recursive(string, i + 1)


"""
tail recursive process

do some research on this **
"""
def is_palindrome_tail_recursion(string, i = 0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return is_palindrome_tail_recursion(string, i + 1)



"""
best solution:
Time: O(n)
Space: O(1)

* use pointers to not use additional space *

"""

def is_palindrome_best(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True