# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)

        k = len(s1)

        if len(s2) < k:
            return False

        window = Counter(s2[:k])
        if window == cnt:
            return True
        for i in range(k, len(s2)):
            c = s2[i]
            window[s2[i]] += 1
            window[s2[i-k]] -= 1

            if all(window[c] == cnt[c] for c in s1):
                return True

        return False
