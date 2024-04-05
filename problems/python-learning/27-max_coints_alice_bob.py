# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/1223659055/

class Solution:
    def maxCoins(self, piles):

        piles_sorted = sorted(piles)
        n = len(piles)
        res = 0
        for i in range(0, n-n//3, 2):
            res += piles_sorted[n//3+i]

        return res
