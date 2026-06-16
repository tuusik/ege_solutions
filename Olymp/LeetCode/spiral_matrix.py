class Solution:
    def spiralOrder(self, matrix):
        n, m = len(matrix), len(matrix[0])
        res = []
        if n == 1 or m == 1:
            for i in range(n):
                for j in range(m):
                    res.append(matrix[i][j])
            return res
        l, r = 0, m - 1
        u, d = 0, n - 1
        while l <= r and u <= d:
            for j in range(l, r + 1):
                res.append(matrix[u][j])
            u += 1
            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if u <= d:
                for j in range(r, l - 1, -1):
                    res.append(matrix[d][j])
                d -= 1
            if l <= r:
                for i in range(d, u - 1, -1):
                    res.append(matrix[i][l])
                l += 1
        return res