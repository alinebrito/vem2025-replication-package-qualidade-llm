class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = [(0, 0, 1)]
        visited = set((0, 0))
        
        while queue:
            x, y, length = queue.pop(0)
            if (x, y) == (n - 1, n - 1):
                return length
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, length + 1))
        return -1