class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or matrix[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, matrix[r][c])
            dfs(r - 1, c, visited, matrix[r][c])
            dfs(r, c + 1, visited, matrix[r][c])
            dfs(r, c - 1, visited, matrix[r][c])

        for c in range(cols):
            dfs(0, c, pacific, matrix[0][c])
            dfs(rows - 1, c, atlantic, matrix[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, matrix[r][0])
            dfs(r, cols - 1, atlantic, matrix[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res