# https: // leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        read = 0
        write = 0
        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
            read += 1
