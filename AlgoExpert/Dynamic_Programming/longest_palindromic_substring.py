"""
longest palindromic sequence - med

write a function that, given a string,, returns its longest palindromic substring. A palindrome is defined as
as a string that is written the same forward and backward. Assume that there will only be one longest
palindromic substring

Sample input: "abaxyzzyxf"
Sample output: "xyzzyx"

"""


def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest


def getPal(s, l, r):

    while l >= 0 and r < len(s):
        if s[l] != s[r]:
            break
        l -= 1
        r += 1
    return [l + 1, r]

def longestPalindromicSubstring(s):
    currentLongest = [0, 1]

    for i in range(1, len(s)):
        odd = getPal(s, i - 1, i + 1)
        even = getPal(s, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key= lambda x: x[1] - x[0])
    
    return s[currentLongest[0]: currentLongest[1]]


print(longestPalindromicSubstring('abaaasasab'))





"""

can be done with double for loop or using dynamic programming





"""

