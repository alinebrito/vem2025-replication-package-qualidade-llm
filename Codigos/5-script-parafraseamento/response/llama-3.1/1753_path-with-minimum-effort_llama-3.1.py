class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H, W = len(heights), len(heights[0])
        left, right = 0, max(max(row) for row in heights) - min(min(row) for row in heights)

        def canReachPath(maxDiff):
            visited = [[False] * W for _ in range(H)]
            queue = [(0, 0)]
            visited[0][0] = True
            while queue:
                x, y = queue.pop(0)
                if x == H - 1 and y == W - 1:
                    return True
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                        if abs(heights[nx][ny] - heights[x][y]) <= maxDiff:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            return False

        while left < right:
            mid = (left + right) // 2
            if canReachPath(mid):
                right = mid
            else:
                left = mid + 1
        return left