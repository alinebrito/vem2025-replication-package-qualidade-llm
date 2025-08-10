class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')] * n for _ in range(m)]
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        return dist