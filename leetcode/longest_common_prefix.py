


x = ["flower","flow","flight"]


class Solution:

    def longestCommonPrefix(self, strs):
        """Find the longest common prefix using horizontal scanning"""
        """Performs a horizontal scanning"""
        """LCP(S1,...,Sn) = LCP(LCP(LCP(S1,S2),S3),S4)"""
        """Computational complexity: O(S) where S is the sum of length of all strings"""
        """Space complexity: O(1) constant space requirement"""

        # (0) Special cases: when the list is empty
        if len(strs) == 0:
            return ""

        # The first string is prefix
        prefix = strs[0]

        # (1) Iterate through all the list
        for current in strs:
            while current.startswith(prefix) == False:

                # reduce the prefix length by 1
                prefix = prefix[:-1]

                # there is no overlap, return it
                if prefix == "":
                    return prefix

        return prefix

