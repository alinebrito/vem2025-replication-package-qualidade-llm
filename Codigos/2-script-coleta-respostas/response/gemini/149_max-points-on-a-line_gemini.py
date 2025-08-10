class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_count = 2
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                count = 2
                for k in range(j + 1, len(points)):
                    if (points[j][1] - points[i][1]) * (points[k][0] - points[i][0]) == (points[k][1] - points[i][1]) * (points[j][0] - points[i][0]):
                        count += 1
                max_count = max(max_count, count)
        return max_count