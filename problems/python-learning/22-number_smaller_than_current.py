# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)

        nums_sorted = sorted((a, i) for i, a in enumerate(nums))
        save = {}
        res = [0]*len(nums)
        for i in range(n):
            if nums_sorted[i][0] in save:
                res[nums_sorted[i][1]] = save[nums_sorted[i][0]]
            else:
                res[nums_sorted[i][1]] = i
                save[nums_sorted[i][0]] = i

        return res
