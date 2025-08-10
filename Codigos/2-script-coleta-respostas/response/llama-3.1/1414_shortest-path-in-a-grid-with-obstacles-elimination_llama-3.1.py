class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = [(0, 0, k, 0)]
        visited = {(0, 0, k)}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            x, y, k, step = queue.pop(0)
            if x == m - 1 and y == n - 1:
                return step
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0 and (nx, ny, k) not in visited:
                        queue.append((nx, ny, k, step + 1))
                        visited.add((nx, ny, k))
                    elif grid[nx][ny] == 1 and k > 0 and (nx, ny, k - 1) not in visited:
                        queue.append((nx, ny, k - 1, step + 1))
                        visited.add((nx, ny, k - 1))
        return -1