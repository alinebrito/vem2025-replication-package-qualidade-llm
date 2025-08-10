class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island_id = 2
        island_sizes = {}

        def dfs(row, col, island_id):
            if row < 0 or row >= n or col < 0 or col >= n or grid[row][col] != 1:
                return 0
            grid[row][col] = island_id
            size = 1
            for dr, dc in dirs:
                size += dfs(row + dr, col + dc, island_id)
            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1

        max_area = max(island_sizes.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_islands = set()
                    for dr, dc in dirs:
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            neighbor_islands.add(grid[nr][nc])
                    potential_area = 1
                    for island in neighbor_islands:
                        potential_area += island_sizes.get(island, 0)
                    max_area = max(max_area, potential_area)

        return max_area