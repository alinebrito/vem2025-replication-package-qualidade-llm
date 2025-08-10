class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            line_points = 1
            same_point = 0
            slopes = {}
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same_point += 1
                else:
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]
                    slope = (dy, dx) if dx != 0 else float('inf')
                    slopes[slope] = slopes.get(slope, 0) + 1
                    line_points = max(line_points, slopes[slope] + same_point + 1)
            max_points = max(max_points, line_points)
        return max_points