class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                i = d if d < m else m - 1
                j = 0 if d < m else d - m + 1
                while i >= 0 and j < n:
                    result.append(matrix[i][j])
                    i -= 1
                    j += 1
            else:
                i = 0 if d < n else d - n + 1
                j = d if d < n else n - 1
                while i < m and j >= 0:
                    result.append(matrix[i][j])
                    i += 1
                    j -= 1
        return result