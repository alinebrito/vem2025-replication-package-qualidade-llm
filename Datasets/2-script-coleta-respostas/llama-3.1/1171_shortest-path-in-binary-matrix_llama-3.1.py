class Solution:
    def shortestPathBinaryMatrix(self, grid):
        from collections import deque

        def in_bounds(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def neighbors(x, y):
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and grid[nx][ny] == 0:
                    yield nx, ny

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        q = deque([(0, 0, 1)])
        grid[0][0] = 1

        while q:
            x, y, d = q.popleft()
            if x == y == len(grid) - 1:
                return d
            for nx, ny in neighbors(x, y):
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    q.append((nx, ny, d + 1))

        return -1