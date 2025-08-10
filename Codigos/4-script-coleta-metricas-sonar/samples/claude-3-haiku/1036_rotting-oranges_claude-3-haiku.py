class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh, rotten = 0, []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        time = 0
        while rotten:
            new_rotten = []
            for x, y in rotten:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        new_rotten.append((nx, ny))
            rotten = new_rotten
            time += 1 if new_rotten else 0
        return time if fresh == 0 else -1