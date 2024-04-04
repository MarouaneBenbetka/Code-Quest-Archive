# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums):
        i = 0
        res = []
        n = len(nums)
        cpt = 0
        while (i < n - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

            if nums[i] != 0:
                res.append(nums[i])
                cpt += 1

            i += 1

        if nums[i] != 0:
            res.append(nums[i])
            cpt += 1
        return res + (n-cpt) * [0]
