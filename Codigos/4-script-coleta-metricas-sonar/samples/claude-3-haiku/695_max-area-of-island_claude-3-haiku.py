class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        
        return ans