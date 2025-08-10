class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = [(0, 0, 1)]
        visited = set([(0, 0)])
        while queue:
            row, col, distance = queue.pop(0)
            if row == n - 1 and col == n - 1:
                return distance
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, distance + 1))
        return -1