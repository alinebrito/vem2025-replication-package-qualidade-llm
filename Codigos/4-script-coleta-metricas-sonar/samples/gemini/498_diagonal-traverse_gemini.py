class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        result = []
        row, col = 0, 0
        up = True
        for i in range(m * n):
            result.append(matrix[row][col])
            if up:
                if row - 1 >= 0 and col + 1 < n:
                    row -= 1
                    col += 1
                else:
                    up = False
                    if col + 1 < n:
                        col += 1
                    else:
                        row += 1
            else:
                if row + 1 < m and col - 1 >= 0:
                    row += 1
                    col -= 1
                else:
                    up = True
                    if row + 1 < m:
                        row += 1
                    else:
                        col += 1
        return result