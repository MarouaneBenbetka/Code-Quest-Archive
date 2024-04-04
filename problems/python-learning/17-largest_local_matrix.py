
# https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution:
    def largestLocal(self, matrix):
        res = []
        for i in range(len(matrix)-3+1):
            row = []
            for j in range(len(matrix[0])-3+1):
                row.append(max(matrix[i+i2][j+j2]
                           for i2 in range(3) for j2 in range(3)))
            res.append(row)

        return res
