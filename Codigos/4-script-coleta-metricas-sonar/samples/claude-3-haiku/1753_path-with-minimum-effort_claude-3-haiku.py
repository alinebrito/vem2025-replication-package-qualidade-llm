class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H, W = len(heights), len(heights[0])
        
        def dfs(x, y, max_diff):
            if x == H-1 and y == W-1:
                return max_diff
            
            visited.add((x, y))
            min_effort = float('inf')
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited:
                    new_max_diff = max(max_diff, abs(heights[nx][ny] - heights[x][y]))
                    min_effort = min(min_effort, dfs(nx, ny, new_max_diff))
            
            return min_effort
        
        visited = set()
        return dfs(0, 0, 0)