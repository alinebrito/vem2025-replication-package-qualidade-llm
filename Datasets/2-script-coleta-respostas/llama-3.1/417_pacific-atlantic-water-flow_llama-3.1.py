class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        def dfs(r, c, visited, ocean):
            if (r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or visited[r][c] or matrix[r][c] < ocean):
                return False
            visited[r][c] = True
            dfs(r+1, c, visited, ocean)
            dfs(r-1, c, visited, ocean)
            dfs(r, c+1, visited, ocean)
            dfs(r, c-1, visited, ocean)
            return True

        m, n = len(matrix), len(matrix[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        for i in range(m):
            dfs(i, 0, pacific, matrix[i][0])
            dfs(i, n-1, atlantic, matrix[i][n-1])

        for j in range(n):
            dfs(0, j, pacific, matrix[0][j])
            dfs(m-1, j, atlantic, matrix[m-1][j])

        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result