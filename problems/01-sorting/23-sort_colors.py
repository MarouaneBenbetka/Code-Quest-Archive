# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        d = [0, 0, 0]
        for i in nums:
            d[i] += 1

        cpt = 0
        for color, color_count in enumerate(d):
            for j in range(color_count):
                nums[cpt] = color
                cpt += 1
