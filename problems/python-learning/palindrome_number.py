# Leet Code
# https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = 0
        original_x = x

        while (x > 0):
            x, a = divmod(x, 10)
            reversed_x = a + reversed_x * 10

        return reversed_x == original_x
