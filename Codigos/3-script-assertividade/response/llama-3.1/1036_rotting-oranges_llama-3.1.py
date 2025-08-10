class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
 m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1,0), (-1,0)]
        queue = []
        fresh_count = 0
        for i in range(m):
 for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        minutes = 0
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
            minutes += 1
        return minutes if fresh_count == 0 else -1