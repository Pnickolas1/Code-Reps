from collections import Counter

"""
find all anagrams within a strings

return the indexs of starting point of any, all anagrams of P within string



"""


def findAnagrams(string, p):

    ns = len(string)
    np = len(p)

    indexes = []

    p_counter = Counter(p)
    s_counter = Counter()

    for i in range(len(string)):

        s_counter[string[i]] += 1

        if i >= np:

            if s_counter[string[i - np]] == 1:
                del s_counter[string[i - np]]
            else:
                s_counter[string[i - np]] -= 1
        if p_counter == s_counter:
            indexes.append(i - np + 1)
    return indexes
