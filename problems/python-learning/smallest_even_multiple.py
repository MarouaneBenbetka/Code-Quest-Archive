# leet code
# https://leetcode.com/problems/smallest-even-multiple/description/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * [1, 2][n % 2]
