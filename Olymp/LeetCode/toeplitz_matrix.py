class Solution:
    def isToeplitzMatrix(self, matrix):
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            matrix[i] = list(reversed(matrix[i]))
        i, j = 0, 0
        while i != n - 1 or j != m - 1:
            if (i + j) % 2 == 0:
                if j == m - 1:
                    i += 1
                    num = matrix[i][j]
                elif i == 0:
                    j += 1
                    num = matrix[i][j]
                else:
                    i -= 1
                    j += 1
                    if matrix[i][j] != num:
                        return False
            elif (i + j) % 2 == 1:
                if i == n - 1:
                    j += 1
                    num = matrix[i][j]
                elif j == 0:
                    i += 1
                    num = matrix[i][j]
                else:
                    i += 1
                    j -= 1
                    if matrix[i][j] != num:
                        return False
        return True