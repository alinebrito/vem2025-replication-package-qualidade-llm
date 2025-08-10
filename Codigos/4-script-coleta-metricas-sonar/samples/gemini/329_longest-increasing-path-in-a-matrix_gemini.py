class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 1
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(x, y) + 1)
            return dp[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans