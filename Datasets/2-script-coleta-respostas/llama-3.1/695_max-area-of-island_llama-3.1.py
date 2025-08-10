class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            area = 1
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        
        return ans