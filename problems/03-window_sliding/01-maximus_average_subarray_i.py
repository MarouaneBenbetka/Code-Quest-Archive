# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window = sum(nums[:k])
        max_window = window
        for i in range(k, len(nums)):
            window -= nums[i-k]
            window += nums[i]
            if max_window < window:
                max_window = window

        return max_window/k
