class Solution:
    def shortestPathBinaryMatrix(self, grid):
        def a_star_graph_search(grid):
            n = len(grid)
            if grid[0][0] == 1 or grid[n-1][n-1] == 1:
                return -1
            queue = [(0, 0, 1)]
            grid[0][0] = 1
            while queue:
                x, y, path_len = queue.pop(0)
                if x == n-1 and y == n-1:
                    return path_len
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny, path_len+1))
            return -1
        return a_star_graph_search(grid)