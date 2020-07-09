


"""
tower of hanoi
"""

def hanoi(n, source, target, spare):
    if n > 0:
        hanoi(n - 1, source, spare, target)
        target.append(source.pop())
        hanoi(n -1, spare, target, source)

