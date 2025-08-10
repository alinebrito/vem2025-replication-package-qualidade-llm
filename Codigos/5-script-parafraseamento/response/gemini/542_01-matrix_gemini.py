class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = []
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        return dist