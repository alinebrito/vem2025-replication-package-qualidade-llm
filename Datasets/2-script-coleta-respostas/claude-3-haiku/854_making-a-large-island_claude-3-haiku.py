class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def dfs(i, j, label):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = label
            return 1 + dfs(i-1, j, label) + dfs(i+1, j, label) + dfs(i, j-1, label) + dfs(i, j+1, label)
        
        label = 2
        areas = {1: 1}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[label] = dfs(i, j, label)
                    label += 1
        
        max_area = max(areas.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                        if 0 <= i+di < n and 0 <= j+dj < n and grid[i+di][j+dj] > 1:
                            neighbors.add(grid[i+di][j+dj])
                    if neighbors:
                        max_area = max(max_area, sum(areas[n] for n in neighbors) + 1)
        return max_area