class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
        if fresh == 0:
            return 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        while queue:
            i, j, minutes = queue.popleft()
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    queue.append((x, y, minutes + 1))
        return minutes if fresh == 0 else -1