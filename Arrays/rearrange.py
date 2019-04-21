

"""
write a program that takes an array A of n numbers and rearranges A's
elements to get a new B having the property B[0] <_ B[1] >_ B[2] <_ B[3] >_
"""


def rearrange(A):
    for i in range(len(A)):
        A[i: i + 2] = sorted(A[i: i + 2], reverse=i % 2)
    return A


print(rearrange([3,5, 10, 3, 4, 6, 8]))