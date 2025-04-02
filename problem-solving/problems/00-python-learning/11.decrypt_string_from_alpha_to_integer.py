
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/


class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0

        res = ""
        while i < len(s)-2:
            if s[i+2] == "#":
                res += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                res += chr(int(s[i])+96)
                i += 1

        while i < len(s):
            res += chr(int(s[i])+96)
            i += 1

        return res
