# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs):

        n = min(len(s) for s in strs)
        prefix = ""
        for i in range(n):
            l = strs[0][i]
            if all(s[i] == l for s in strs):
                prefix += l
            else:
                return prefix

        return prefix
