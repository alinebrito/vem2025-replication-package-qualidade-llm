class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_val = float('inf')
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < min_val:
                    min_val = matrix[i][j]
                k -= 1
                if k == 0:
                    return min_val
        return -1