class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    self.bfs(matrix, i, j, dist)

        return dist

    def bfs(self, matrix, i, j, dist):
        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(i, j)]
        dist[i][j] = 0

        while queue:
            x, y = queue.pop(0)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))