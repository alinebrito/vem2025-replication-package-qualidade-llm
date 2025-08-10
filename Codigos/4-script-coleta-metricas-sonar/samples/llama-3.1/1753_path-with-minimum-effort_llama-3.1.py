class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for _ in range(rows)]

        def can_reach(x, y, target):
            if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y]:
                return False
            if abs(heights[x][y] - target) > target:
                return False
            visited[x][y] = True
            for dx, dy in directions:
                if can_reach(x + dx, y + dy, target):
                    return True
            return False

        left, right = 1, max(max(row) for row in heights)
        while left < right:
            mid = (left + right) // 2
            if can_reach(0, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left