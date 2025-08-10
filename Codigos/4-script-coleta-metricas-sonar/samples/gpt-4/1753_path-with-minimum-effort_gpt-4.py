class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H, W = len(heights), len(heights[0])
        left, right = 0, max(max(row) for row in heights) - min(min(row) for row in heights)

        def canCross(mid):
            visited = [[False] * W for _ in range(H)]
            stack = [(0, 0)]
            visited[0][0] = True
            while stack:
                x, y = stack.pop()
                if x == H - 1 and y == W - 1:
                    return True
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and abs(heights[nx][ny] - heights[x][y]) <= mid:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return False

        while left < right:
            mid = (left + right) // 2
            if canCross(mid):
                right = mid
            else:
                left = mid + 1
        return left