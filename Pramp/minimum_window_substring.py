"""
minimum window substring

pramp: hard
"""
import collections

def minWindow(s, t):
    need = collections.Counter(t)
    missing = len(t)
    i = 0
    I = 0
    J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]



arr = ['x','y','z']
s = "xyyzyzyx"

# output: "zyx"

print(minWindow(s, arr))