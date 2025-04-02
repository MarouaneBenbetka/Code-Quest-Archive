# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)

        mul = skill[0]*skill[n-1]
        sum = skill[0]+skill[n-1]

        start = 1
        end = n-2

        while start < end:
            s = skill[start]+skill[end]
            if s != sum:
                return -1
            else:
                mul += skill[start]*skill[end]

            start += 1
            end -= 1

        return mul
