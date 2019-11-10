
"""
Valid Palindrome:

take aways:

isalnum() ->

isalpha() ->

"""


def valid_palindrome(string):
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
