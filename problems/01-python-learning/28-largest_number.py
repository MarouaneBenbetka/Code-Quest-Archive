# https://leetcode.com/problems/largest-number/

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):

        def sort_function(a, b):
            a = str(a)
            b = str(b)
            if a.startswith(b) or b.startswith(a):
                return int(a+b)-int(b+a)
            else:
                if a < b:
                    return -1
                elif a > b:
                    return 1
                else:
                    return 0
        nums = sorted(nums, key=cmp_to_key(sort_function), reverse=True)
        return str(int("".join(str(n)for n in nums)))
