class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_diagonal_sum = sum(mat[i][i] for i in range(n))
        secondary_diagonal_sum = sum(mat[i][n-i-1] for i in range(n))
        if n % 2 == 1:
            middle_element = mat[n//2][n//2]
            return primary_diagonal_sum + secondary_diagonal_sum - middle_element
        else:
            return primary_diagonal_sum + secondary_diagonal_sum