class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        from collections import deque
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, k, 0)]) 
        visited = set((0, 0, k))
        
        while queue:
            x, y, obstacles_left, steps = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1 and obstacles_left > 0 and (nx, ny, obstacles_left - 1) not in visited:
                        visited.add((nx, ny, obstacles_left - 1))
                        queue.append((nx, ny, obstacles_left - 1, steps + 1))
                    elif grid[nx][ny] == 0 and (nx, ny, obstacles_left) not in visited:
                        visited.add((nx, ny, obstacles_left))
                        queue.append((nx, ny, obstacles_left, steps + 1))
        return -1