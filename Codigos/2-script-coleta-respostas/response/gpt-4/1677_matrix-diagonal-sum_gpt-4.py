class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = sum(mat[i][i] + mat[i][n - i - 1] for i in range(n))
        if n % 2 == 1:
            diagonal_sum -= mat[n // 2][n // 2]
        return diagonal_sum