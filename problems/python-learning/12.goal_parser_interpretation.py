
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0

        res = ""
        while (i < n):
            if command[i] == "G":
                res += "G"
                i += 1
            elif command[i:i+2] == "()":
                res += "o"
                i += 2
            else:
                res += "al"
                i += 4

        return res
