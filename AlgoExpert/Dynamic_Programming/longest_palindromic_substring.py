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


print(longestPalindromicSubstring('abaaasasab'))



"""

can be done with double for loop or using dynamic programming





"""