class Solution:
    def diagonalSum(self, mat):
        l = len(mat)
        res = 0
        for i in range(l):
            res += mat[i][i]
            res += mat[i][l - 1 - i]
        if l % 2 == 0:
            return res
        return res - mat[l // 2][l // 2]