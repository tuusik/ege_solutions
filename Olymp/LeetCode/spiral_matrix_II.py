class Solution:
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for _ in range(n)]
        inc = 1
        if n == 1:
            return [[inc]]
        l, r = 0, n - 1
        u, d = 0, n - 1
        while l <= r and u <= d:
            for j in range(l, r + 1):
                res[u][j] = inc
                inc += 1
            u += 1
            for i in range(u, d + 1):
                res[i][r] = inc
                inc += 1
            r -= 1
            if u <= d:
                for j in range(r, l - 1, -1):
                    res[d][j] = inc
                    inc += 1
                d -= 1
            if l <= r:
                for i in range(d, u - 1, -1):
                    res[i][l] = inc
                    inc += 1
                l += 1
        return res