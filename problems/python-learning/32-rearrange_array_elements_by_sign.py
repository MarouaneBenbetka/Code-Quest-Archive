# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        res = []
        for n in nums:
            if n >= 0:
                pos.append(n)
            else:
                neg.append(n)
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
