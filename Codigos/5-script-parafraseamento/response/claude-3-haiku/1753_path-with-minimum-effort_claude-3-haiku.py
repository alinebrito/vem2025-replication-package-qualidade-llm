class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H, W = len(heights), len(heights[0])
        
        def dfs(i, j, max_diff):
            if i == H-1 and j == W-1:
                return max_diff
            
            heights[i][j] = float('inf')
            min_diff = float('inf')
            
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W:
                    diff = abs(heights[i][j] - heights[ni][nj])
                    min_diff = min(min_diff, dfs(ni, nj, max(max_diff, diff)))
            
            heights[i][j] = min_diff
            return min_diff
        
        return dfs(0, 0, 0)