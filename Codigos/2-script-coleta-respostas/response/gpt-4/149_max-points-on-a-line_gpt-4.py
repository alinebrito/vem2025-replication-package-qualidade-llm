class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            slopes = {}
            for j in range(len(points)):
                if i != j:
                    slope = (points[j][1] - points[i][1], points[j][0] - points[i][0])
                    gcd = self.gcd(slope[0], slope[1])
                    slope = (slope[0] // gcd, slope[1] // gcd)
                    if slope not in slopes:
                        slopes[slope] = 1
                    slopes[slope] += 1
            max_points = max(max_points, max(slopes.values(), default=1))
        return max_points

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)