class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H = len(heights)
        W = len(heights[0])
        if H == 1 and W == 1:
            return 0
        difference = [[float('inf') for _ in range(W)] for _ in range(H)]
        difference[0][0] = 0
        queue = [(0, 0)]
        while queue:
            r, c = queue.pop(0)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    curr_diff = abs(heights[nr][nc] - heights[r][c])
                    max_diff = max(curr_diff, difference[r][c])
                    if difference[nr][nc] > max_diff:
                        difference[nr][nc] = max_diff
                        queue.append((nr, nc))
        return difference[-1][-1] 