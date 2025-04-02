# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums, target: int):

        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n == target:
                res.append(i)
            elif n > target:
                break
        return res
