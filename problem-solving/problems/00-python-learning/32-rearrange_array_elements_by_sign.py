# https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution:
    def rearrangeArray(self, nums):
        pos = 0
        neg = 1

        res = [0]*len(nums)

        for n in nums:
            if n >= 0:
                res[pos] = n
                pos += 2
            else:
                res[neg] = n
                neg += 2

        return res
