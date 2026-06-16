class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        new = []
        for i in range(m * n):
            if i % c == 0:
                new.append([])
            new[i // c].append(mat[i // n][i % n])
        return new