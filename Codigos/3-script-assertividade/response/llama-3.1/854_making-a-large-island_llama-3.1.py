class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island_size = {}
        island_id = 1

        def dfs(i, j, island_id):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = island_id
                size = 1
                for d in directions:
                    size += dfs(i + d[0], j + d[1], island_id)
                return size
 return 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[island_id] = dfs(i, j, island_id)
                    island_id += 1

        max_size =0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1
 island_ids = set()
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != 0:
                            island_ids.add(grid[ni][nj])
                    for island_id in island_ids:
                        size += island_size[island_id]
                    max_size = max(max_size, size)

        return max_size if max_size > 0 else n * n