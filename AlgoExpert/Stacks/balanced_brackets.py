"""
Balanced Brackets: medium

write a function that takes in a string of brackets, and return a boolean representing whether or not the string
is balanced.

A string is said to be balanced if it has as many opening brackets of a given type as it has closing brackets of that
type and if no brackets is unmatched

Sample input: "([])(){}(())()()"
Output => True (it is balanced)

"""


def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


