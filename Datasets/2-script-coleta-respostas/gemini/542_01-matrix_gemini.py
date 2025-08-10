class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        queue = [(i, j, 0) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        visited = set(queue)
        result = [[float('inf')] * n for _ in range(m)]
        for i, j, dist in queue:
            result[i][j] = dist
        while queue:
            i, j, dist = queue.pop(0)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    result[x][y] = dist + 1
                    queue.append((x, y, dist + 1))
                    visited.add((x, y))
        return result