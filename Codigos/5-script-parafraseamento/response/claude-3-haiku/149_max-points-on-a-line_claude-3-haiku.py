class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            same_point = 1
            same_slope = 0
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same_point += 1
                else:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    if x1 == x2:
                        same_slope += 1
                    else:
                        slope = (y2 - y1) / (x2 - x1)
                        same_slope = max(same_slope, self.countSameSlope(points, i, j, slope))
            max_points = max(max_points, same_point + same_slope)
        return max_points

    def countSameSlope(self, points, i, j, slope):
        count = 2
        x1, y1 = points[i]
        x2, y2 = points[j]
        for k in range(j+1, len(points)):
            x3, y3 = points[k]
            if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
                count += 1
        return count