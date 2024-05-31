# https: // leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            print(left, right)
            print(mid, nums[mid])

            if nums[mid] == target:
                return mid

            if target <= nums[mid]:
                right = mid-1
            else:
                left = mid+1

        return -1
