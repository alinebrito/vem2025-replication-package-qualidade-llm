class Solution:
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        for i in range(n):
            A.append([0]*n)
        left, right, top, bottom = 0, n-1, 0, n-1
        while lo > 1:
            for i in range(left, right + 1):
                A[top][i] = lo - 1
                lo -= 1
            top += 1
            for i in range(top, bottom + 1):
                A[i][right] = lo - 1
                lo -= 1
            right -= 1
            for i in range(right, left - 1, -1):
                A[bottom][i] = lo - 1
                lo -= 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                A[i][left] = lo - 1
                lo -= 1
            left += 1
        return A