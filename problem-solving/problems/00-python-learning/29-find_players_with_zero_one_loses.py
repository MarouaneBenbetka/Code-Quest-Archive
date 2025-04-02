
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

import bisect


class Solution:
    def findWinners(self, matches):
        answer = [[], []]

        d = {}

        for match in matches:
            d[match[1]] = d.get(match[1], 0)+1
            if match[0] not in d:
                d[match[0]] = 0

        for player, loses in d.items():
            if loses == 0:
                bisect.insort(answer[0], player)
            elif loses == 1:
                bisect.insort(answer[1], player)

        return answer
