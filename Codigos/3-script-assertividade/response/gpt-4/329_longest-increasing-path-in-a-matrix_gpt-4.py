class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            length = 1
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    length = max(length, 1 + dfs(ni, nj))
            dp[i][j] = length
            return length
        
        max_length = 0
        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))
        return max_length