

# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums):

        can_modify = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] <= nums[i+1]:
                i += 1
                continue
            elif can_modify:
                can_modify -= 1
                if i > 0:
                    if nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i+1] = nums[i]
                else:
                    nums[i] = float('-inf')
            else:
                return False
        return True
