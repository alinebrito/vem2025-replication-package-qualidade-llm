class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        pacific_reachable = [[False]*cols for _ in range(rows)]
        atlantic_reachable = [[False]*cols for _ in range(rows)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not reachable[nr][nc] and matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, reachable)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows-1, c, atlantic_reachable)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols-1, atlantic_reachable)

        return [[r, c] for r in range(rows) for c in range(cols) if pacific_reachable[r][c] and atlantic_reachable[r][c]]