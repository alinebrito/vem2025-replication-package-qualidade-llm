class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, visited)
        
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)
        
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result