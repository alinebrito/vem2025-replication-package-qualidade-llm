class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        queue = [(0, 0, k, 0)]
        visited = set([(0, 0, k)])
        while queue:
            row, col, eliminate, steps = queue.pop(0)
            if row == m - 1 and col == n - 1:
                return steps
            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate - 1) not in visited:
                        visited.add((new_row, new_col, eliminate - 1))
                        queue.append((new_row, new_col, eliminate - 1, steps + 1))
                    elif grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        visited.add((new_row, new_col, eliminate))
                        queue.append((new_row, new_col, eliminate, steps + 1))
        return -1