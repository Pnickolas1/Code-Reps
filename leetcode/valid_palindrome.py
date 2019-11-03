
"""
Valid Palindrome:

take aways:

isalnum() ->

isalpha() ->

this can and should be done in O(1) space

"""


def valid_palindrome(s):
    if s == "":
        return False

    string = s.replace(" ", "")

    start = 0
    last = len(string) - 1
    while start <= last:
        if string[start].isalnum() and string[last].isalnum():
            if string[start].lower() != string[last].lower():
                return False
            start += 1
            last -= 1
        elif not string[start].isalnum():
            start += 1
        elif not string[last].isalnum():
            last -= 1

    return True


p