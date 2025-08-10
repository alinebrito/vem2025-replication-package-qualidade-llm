class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                A[i][j] += min(A[i-1][max(0,j-1):min(len(A[0]), j+2)])
        return min(A[-1])