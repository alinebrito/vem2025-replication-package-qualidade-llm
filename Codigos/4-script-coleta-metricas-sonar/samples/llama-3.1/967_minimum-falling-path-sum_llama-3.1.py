class Solution:
    def minFallingPathSum(self, A):
        n = len(A)
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    A[i][j] += min(A[i-1][j], A[i-1][j+1])
                elif j == n-1:
                    A[i][j] += min(A[i-1][j-1], A[i-1][j])
                else:
                    A[i][j] += min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
        return min(A[-1])