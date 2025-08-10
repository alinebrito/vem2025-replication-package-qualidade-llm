class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        @lru_cache(None)
        def dfs(i, j):
            max_length = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(x, y))
            return max_length

        return max(dfs(i, j) for i in range(m) for j in range(n))