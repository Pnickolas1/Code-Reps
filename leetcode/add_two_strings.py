
"""

Input: num1 = "11", num2 = "123"
Output: "134"


given to string numbers, add them, return the sum in string form

"""


def addString(num1, num2):
    left = len(num1) - 1
    right = len(num2) - 1

    x = []
    carry = 0

    while left >= 0 or right >= 0:

        value1 = ord(num1[left]) - ord('0') if left >= 0 else 0
        value2 = ord(num2[right]) - ord('0') if right >= 0 else 0

        value = (value1 + value2 + carry) % 10
        carry = (value1 + value2 + carry) // 10

        x.append(str(value))
        left -= 1
        right -= 1

    if carry: 
        x.append(carry)

    return ''.join([str(i) for i in reversed(x)])
    

print(addString('123', '456'))
