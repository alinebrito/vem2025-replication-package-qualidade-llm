class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(1, n):
            for j in range(n):
                A[i][j] += min(A[i-1][j], A[i-1][j-1] if j > 0 else float('inf'), A[i-1][j+1] if j < n - 1 else float('inf'))
        return min(A[-1])