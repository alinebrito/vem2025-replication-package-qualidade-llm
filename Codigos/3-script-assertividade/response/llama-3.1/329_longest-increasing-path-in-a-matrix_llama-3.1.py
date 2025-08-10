class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            val = matrix[i][j]
            max_len = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > val:
                    max_len = max(max_len, 1 + dfs(x, y))
            dp[i][j] = max_len
            return max_len

        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i, j))
        return max_len