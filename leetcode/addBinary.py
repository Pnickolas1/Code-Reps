"""
Given 2 Binary Strings:

given 2 binary strings, add them, return binary string

bin -> takes in integer, returns binary representation of number
int -> takes in binary representation, returns
"""

def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(add_binary('11', '1'))


def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


