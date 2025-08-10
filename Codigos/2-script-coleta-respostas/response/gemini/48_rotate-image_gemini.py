class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j]