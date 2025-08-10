class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            hashmap = {}
            same = 1
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                else:
                    slope = float('inf')
                    if points[i][0]!= points[j][0]:
                        slope = (points[j][1] - points[i][1]) * 1.0 / (points[j][0] - points[i][0])
                    hashmap[slope] = hashmap.get(slope, 0) + 1
            res = max(res, max(hashmap.values(), default=0) + same)