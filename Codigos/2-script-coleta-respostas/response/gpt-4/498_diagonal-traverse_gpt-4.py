class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        result = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                r = min(d, m - 1)
                c = d - r  
                while r >= 0 and c < n:
                    result.append(matrix[r][c])
                    r -= 1  
                    c += 1  
            else:
                c = min(d, n - 1)
                r = d - c  
                while c >= 0 and r < m:
                    result.append(matrix[r][c])
                    c -= 1  
                    r += 1  
        return result  