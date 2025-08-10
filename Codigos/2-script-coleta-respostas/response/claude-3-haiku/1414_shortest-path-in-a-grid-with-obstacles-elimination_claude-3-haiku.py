class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, k)])
        visited = set()
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j, remaining_k = queue.popleft()
                if i == m - 1 and j == n - 1:
                    return steps
                if (i, j, remaining_k) in visited:
                    continue
                visited.add((i, j, remaining_k))
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 0:
                            queue.append((ni, nj, remaining_k))
                        elif remaining_k > 0:
                            queue.append((ni, nj, remaining_k - 1))
            steps += 1
        return -1